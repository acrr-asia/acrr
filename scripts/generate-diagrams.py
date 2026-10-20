# Generates the inline SVG diagrams in src/components/diagrams/*.astro.
# Plot curves are computed from the formulas in the articles, not hand-drawn.
# Usage: python3 scripts/generate-diagrams.py src/components/diagrams
# Styling (colours, fonts) lives in src/styles/prose.css under .diagram-svg.
import math, cmath, os, sys
OUT = sys.argv[1]

def svg(name, w, h, title, desc, body):
    pid = name.lower()
    s = f'''---
// Generated diagram (inline SVG). Colours come from CSS tokens via the classes styled in
// src/styles/prose.css (.diagram), so it follows light and dark mode.
---
<svg class="diagram-svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="{pid}-title {pid}-desc" data-pagefind-ignore>
  <title id="{pid}-title">{title}</title>
  <desc id="{pid}-desc">{desc}</desc>
  <defs>
    <marker id="{pid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path class="arrowhead" d="M0,0 L10,5 L0,10 z" />
    </marker>
  </defs>
{body.replace("ARROW", f"url(#{pid}-arrow)")}
</svg>
'''
    open(os.path.join(OUT, name + '.astro'), 'w').write(s)

def arrow(pts, cls='ln'):
    d = ' '.join(('M' if i == 0 else 'L') + f'{x:.1f},{y:.1f}' for i, (x, y) in enumerate(pts))
    return f'  <path class="{cls}" d="{d}" marker-end="ARROW" />\n'
def line(pts, cls='ln', extra=''):
    d = ' '.join(('M' if i == 0 else 'L') + f'{x:.1f},{y:.1f}' for i, (x, y) in enumerate(pts))
    return f'  <path class="{cls}" d="{d}"{extra} />\n'
def box(x, y, w, h, label, sub=None):
    s = f'  <rect class="box" x="{x}" y="{y}" width="{w}" height="{h}" rx="3" />\n'
    if sub:
        s += f'  <text x="{x+w/2}" y="{y+h/2-3}" text-anchor="middle">{label}</text>\n'
        s += f'  <text class="small" x="{x+w/2}" y="{y+h/2+13}" text-anchor="middle">{sub}</text>\n'
    else:
        s += f'  <text x="{x+w/2}" y="{y+h/2+5}" text-anchor="middle">{label}</text>\n'
    return s
def text(x, y, t, anchor='start', cls=None):
    c = f' class="{cls}"' if cls else ''
    return f'  <text{c} x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}">{t}</text>\n'
def summing(cx, cy, r=13):
    return (f'  <circle class="box" cx="{cx}" cy="{cy}" r="{r}" />\n'
            + line([(cx-6, cy), (cx+6, cy)]) + line([(cx, cy-6), (cx, cy+6)]))
def var(t):
    return f'<tspan class="var">{t}</tspan>'

# ---------- 1. Closed control loop (introduction) ----------
b = ''
cy = 95
b += text(14, cy-8, var('r'))
b += arrow([(14, cy), (77, cy)])
b += summing(90, cy)
b += text(96, cy+30, '−', cls='sign')
b += arrow([(103, cy), (150, cy)])
b += text(126, cy-8, var('e'), 'middle')
b += box(150, cy-24, 110, 48, 'Controller')
b += arrow([(260, cy), (300, cy)])
b += text(280, cy-8, var('u'), 'middle')
b += box(300, cy-24, 100, 48, 'Actuator')
b += arrow([(400, cy), (440, cy)])
b += box(440, cy-24, 100, 48, 'Plant')
b += arrow([(540, cy), (634, cy)])
b += text(628, cy-8, var('y'), 'end')
b += f'  <circle class="dot" cx="590" cy="{cy}" r="3" />\n'
b += text(490, 28, 'disturbance ' + var('d'), 'middle', 'small')
b += arrow([(490, 36), (490, cy-24)])
sy = 185
b += arrow([(590, cy), (590, sy), (420, sy)])
b += box(320, sy-22, 100, 44, 'Sensor')
b += arrow([(320, sy), (90, sy), (90, cy+13)])
b += text(205, sy-8, 'measured output', 'middle', 'small')
b += text(370, 252, 'noise ' + var('n'), 'middle', 'small')
b += arrow([(370, 240), (370, sy+22)])
svg('ControlLoop', 640, 262, 'Block diagram of a closed-loop control system',
    'The reference r and the measured output meet at a summing junction that forms the error e. The controller turns e into a command u, the actuator applies it to the plant, and the plant produces the output y. A disturbance d acts on the plant. A sensor, corrupted by noise n, measures y and feeds it back with a negative sign.',
    b)

# ---------- plot helper ----------
class Plot:
    def __init__(s, x0, y0, w, h, xr, yr):
        s.x0, s.y0, s.w, s.h, s.xr, s.yr = x0, y0, w, h, xr, yr
    def X(s, v): return s.x0 + (v - s.xr[0]) / (s.xr[1] - s.xr[0]) * s.w
    def Y(s, v): return s.y0 + s.h - (v - s.yr[0]) / (s.yr[1] - s.yr[0]) * s.h
    def curve(s, f, n=240, cls='acc', extra=''):
        pts = [(s.X(s.xr[0] + i*(s.xr[1]-s.xr[0])/n), s.Y(f(s.xr[0] + i*(s.xr[1]-s.xr[0])/n))) for i in range(n+1)]
        return line(pts, cls, extra)
    def axes(s, xticks, yticks, xlabel, ylabel):
        o = ''
        for v in yticks:
            o += line([(s.x0, s.Y(v)), (s.x0+s.w, s.Y(v))], 'grid')
            o += text(s.x0-6, s.Y(v)+4, f'{v:g}', 'end', 'small')
        for v in xticks:
            o += text(s.X(v), s.y0+s.h+16, f'{v:g}', 'middle', 'small')
        o += line([(s.x0, s.y0), (s.x0, s.y0+s.h), (s.x0+s.w, s.y0+s.h)])
        o += text(s.x0+s.w, s.y0+s.h+34, xlabel, 'end', 'small')
        o += text(s.x0, s.y0-10, ylabel, 'start', 'small')
        return o

# ---------- 2. Second-order step response ----------
z, wn = 0.5, 2.0
wd = wn*math.sqrt(1-z*z); ph = math.acos(z)
step2 = lambda t: 1 - math.exp(-z*wn*t)/math.sqrt(1-z*z)*math.sin(wd*t+ph)
P = Plot(56, 30, 540, 200, (0, 6), (0, 1.3))
b = P.axes([0,1,2,3,4,5,6], [0, 0.5, 1.0], 'time  ' + var('t') + '  (s)', 'output  ' + var('y(t)'))
b += f'  <rect class="band" x="{P.X(0):.1f}" y="{P.Y(1.02):.1f}" width="{P.w:.1f}" height="{P.Y(0.98)-P.Y(1.02):.1f}" />\n'
b += line([(P.X(0), P.Y(1)), (P.X(6), P.Y(1))], 'mut', ' stroke-dasharray="4 4"')
b += P.curve(step2)
tp = math.pi/wd; Mp = math.exp(-math.pi*z/math.sqrt(1-z*z))
b += line([(P.X(tp), P.Y(1)), (P.X(tp), P.Y(1+Mp))], 'mut')
b += f'  <circle class="dot" cx="{P.X(tp):.1f}" cy="{P.Y(1+Mp):.1f}" r="3" />\n'
b += text(P.X(tp)+8, P.Y(1+Mp)-6, var('M') + '<tspan class="sub" dy="3">p</tspan><tspan dy="-3"> ≈ 16.3%</tspan>', 'start', 'small')
Ts = 4/(z*wn)
b += line([(P.X(Ts), P.Y(0)), (P.X(Ts), P.Y(1.25))], 'mut', ' stroke-dasharray="3 3"')
b += text(P.X(Ts)+6, P.Y(0.3), var('T') + '<tspan class="sub" dy="3">s</tspan><tspan dy="-3"> ≈ 4 s</tspan>', 'start', 'small')
b += text(P.X(6)-4, P.Y(1.02)-6, '±2% band', 'end', 'small')
svg('StepResponse', 620, 270, 'Unit-step response of a second-order system with damping ratio 0.5',
    'The output rises from 0, overshoots the final value 1 by about 16.3 percent at roughly 1.8 seconds, oscillates with decreasing amplitude, and stays within a band of plus or minus 2 percent of the final value from about 4 seconds on. Natural frequency 2 radians per second.',
    b)

# ---------- 3. Proportional feedback loop ----------
b = ''
cy = 60
b += text(14, cy-8, var('r'))
b += arrow([(14, cy), (77, cy)])
b += summing(90, cy)
b += text(96, cy+30, '−', cls='sign')
b += arrow([(103, cy), (160, cy)])
b += text(131, cy-8, var('r') + ' − ' + var('x'), 'middle', 'small')
b += box(160, cy-24, 70, 48, var('k'))
b += arrow([(230, cy), (290, cy)])
b += text(260, cy-8, var('u'), 'middle')
b += box(290, cy-28, 170, 56, 'Plant', var('ẋ') + ' = −' + var('a') + var('x') + ' + ' + var('b') + var('u'))
b += arrow([(460, cy), (556, cy)])
b += text(550, cy-8, var('x'), 'end')
b += f'  <circle class="dot" cx="510" cy="{cy}" r="3" />\n'
b += arrow([(510, cy), (510, 128), (90, 128), (90, cy+13)])
svg('ProportionalLoop', 560, 145, 'Proportional feedback around a first-order plant',
    'The output x is subtracted from the reference r. The error is multiplied by the gain k to give the input u, which drives the plant x-dot equals minus a x plus b u.',
    b)

# ---------- 4. Step responses with feedback ----------
P = Plot(56, 30, 470, 210, (0, 4), (0, 1.1))
b = P.axes([0,1,2,3,4], [0, 0.5, 0.8, 0.9, 1.0], 'time  ' + var('t'), 'output  ' + var('x(t)') + ',  ' + var('r') + ' = 1')
b += P.curve(lambda t: 1-math.exp(-t), cls='mut', extra=' stroke-dasharray="6 4"')
for k, dash in ((1, ' stroke-dasharray="2 3"'), (4, ' stroke-dasharray="8 3"'), (9, '')):
    g = k/(1+k)
    b += P.curve(lambda t, k=k, g=g: g*(1-math.exp(-(1+k)*t)), extra=dash)
lab = [('open loop, ' + var('u') + ' = ' + var('r'), 1-math.exp(-4), 0), (var('k') + ' = 9', 0.9, 0), (var('k') + ' = 4', 0.8, 0), (var('k') + ' = 1', 0.5, 0)]
for t_, v, _ in lab:
    b += text(P.X(4)+8, P.Y(v)+4, t_, 'start', 'small')
svg('FeedbackStepResponses', 640, 280, 'Step responses of the first-order plant with and without feedback',
    'With a equal to b equal to 1 and r equal to 1, the open-loop response rises to 1 with time constant 1. Proportional feedback with gains 1, 4 and 9 settles at 0.5, 0.8 and 0.9 with time constants 0.5, 0.2 and 0.1: faster, but with a steady-state offset.',
    b)

# ---------- 5. Mass-spring-damper ----------
b = ''
b += line([(40, 30), (40, 190)])
for yy in range(34, 190, 12):
    b += line([(40, yy), (28, yy+10)], 'mut')
b += line([(40, 190), (420, 190)])
for xx in range(48, 420, 14):
    b += line([(xx, 190), (xx-10, 200)], 'mut')
# spring at y=80
ys = 80
pts = [(40, ys), (70, ys)]
n = 8
for i in range(n):
    pts.append((70 + (i+0.5)*(110/n), ys + (-12 if i % 2 == 0 else 12)))
pts += [(180, ys), (220, ys)]
b += line(pts)
b += text(130, ys-22, var('k'), 'middle')
# damper at y=140
yd = 140
b += line([(40, yd), (110, yd)])
b += line([(110, yd-14), (110, yd+14)], 'thick')
b += line([(96, yd-18), (150, yd-18), (150, yd+18), (96, yd+18)])  # cylinder
b += line([(150, yd), (220, yd)])
b += text(125, yd+38, var('c'), 'middle')
b += box(220, 55, 110, 110, var('m'))
b += f'  <circle class="ln" cx="245" cy="178" r="11" /><circle class="ln" cx="305" cy="178" r="11" />\n'
b += arrow([(330, 110), (410, 110)])
b += text(380, 100, 'force ' + var('u'), 'middle', 'small')
b += line([(275, 40), (275, 22)], 'mut')
b += arrow([(275, 30), (345, 30)])
b += text(352, 34, 'displacement ' + var('q'), 'start', 'small')
svg('MassSpringDamper', 470, 215, 'Mass-spring-damper system',
    'A mass m on rollers is connected to a fixed wall by a spring of stiffness k and a damper with coefficient c. A force u pushes the mass to the right, and q is its displacement.',
    b)

# ---------- 6. Eigenvalues in the complex plane ----------
P = Plot(60, 20, 380, 260, (-1.5, 0.5), (-2.5, 2.5))
b = f'  <rect class="band" x="{P.X(-1.5):.1f}" y="{P.y0}" width="{P.X(0)-P.X(-1.5):.1f}" height="{P.h}" />\n'
for v in (-2, -1, 1, 2):
    b += line([(P.x0, P.Y(v)), (P.x0+P.w, P.Y(v))], 'grid')
    b += text(P.X(0)+6, P.Y(v)+4, f'{v:g}' + var('j'), 'start', 'small')
for v in (-1.5, -1, -0.5, 0.5):
    b += line([(P.X(v), P.y0), (P.X(v), P.y0+P.h)], 'grid')
    b += text(P.X(v), P.Y(0)+16, f'{v:g}', 'middle', 'small')
b += arrow([(P.x0, P.Y(0)), (P.x0+P.w+10, P.Y(0))])
b += arrow([(P.X(0), P.y0+P.h), (P.X(0), P.y0-8)])
b += text(P.x0+P.w+10, P.Y(0)-8, 'Re ' + var('s'), 'end', 'small')
b += text(P.X(0)+8, P.y0+2, 'Im ' + var('s'), 'start', 'small')
im = math.sqrt(4*4-0.25)/2
for sgn in (1, -1):
    x, y = P.X(-0.25), P.Y(sgn*im)
    b += line([(x-6, y-6), (x+6, y+6)], 'acc thick') + line([(x-6, y+6), (x+6, y-6)], 'acc thick')
    b += text(x-12, y+5, f'−0.25 {"+" if sgn > 0 else "−"} 1.984' + var('j'), 'end', 'small')
b += text(P.X(-1.45), P.Y(-2.3), 'stable: Re ' + var('s') + ' &lt; 0', 'start', 'small')
svg('EigenvaluePlot', 480, 310, 'Eigenvalues of the example system in the complex plane',
    'The two eigenvalues, minus 0.25 plus and minus 1.984 j, lie in the shaded left half of the complex plane, where every eigenvalue has a negative real part and the response decays.',
    b)

# ---------- 7. Stability regions ----------
R = lambda z: 1 + z + z*z/2 + z**3/6 + z**4/24
c = -1.0
pts = []
for i in range(721):
    phi = 2*math.pi*i/720
    d = cmath.exp(1j*phi)
    rho, step = 0.0, 0.01
    while abs(R(c + (rho+step)*d)) <= 1 and rho < 5: rho += step
    lo, hi = rho, rho+step
    for _ in range(40):
        mid = (lo+hi)/2
        if abs(R(c+mid*d)) <= 1: lo = mid
        else: hi = mid
    pts.append(c + lo*d)
P = Plot(56, 20, 400, 320, (-3.2, 0.8), (-3.2, 3.2))
d = ' '.join(('M' if i == 0 else 'L') + f'{P.X(p.real):.1f},{P.Y(p.imag):.1f}' for i, p in enumerate(pts)) + ' Z'
b = f'  <path class="region" d="{d}" />\n'
for v in (-3, -2, -1):
    b += line([(P.X(v), P.y0), (P.X(v), P.y0+P.h)], 'grid')
    b += text(P.X(v)+(-5 if v > -3 else 0), P.Y(0)+16, f'{v:g}', 'end' if v > -3 else 'middle', 'small')
for v in (-3, -2, -1, 1, 2, 3):
    b += line([(P.x0, P.Y(v)), (P.x0+P.w, P.Y(v))], 'grid')
    b += text(P.x0-6, P.Y(v)+4, f'{v:g}' + var('j'), 'end', 'small')
b += f'  <path class="acc" d="{d}" />\n'
r = P.X(0) - P.X(-1)
b += f'  <circle class="region2" cx="{P.X(-1):.1f}" cy="{P.Y(0):.1f}" r="{r:.1f}" />\n'
b += arrow([(P.x0, P.Y(0)), (P.x0+P.w+10, P.Y(0))])
b += arrow([(P.X(0), P.y0+P.h), (P.X(0), P.y0-8)])
b += text(P.x0+P.w+10, P.Y(0)-8, 'Re ' + var('hλ'), 'end', 'small')
b += text(P.X(0)+8, P.y0+2, 'Im ' + var('hλ'), 'start', 'small')
b += text(P.X(-1), P.Y(0.35), 'Euler', 'middle', 'small')
b += text(P.X(-1.4), P.Y(2.45), 'RK4', 'middle', 'small')
x, y = P.X(-2.5), P.Y(0)
b += f'  <circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="4" />\n'
b += text(x+17, y-22, var('hλ') + ' = −2.5', 'middle', 'small')
b += line([(x+3, y-5), (x+10, y-17)], 'mut')
svg('StabilityRegions', 480, 365, 'Stability regions of explicit Euler and classical RK4',
    'In the complex h-lambda plane, explicit Euler is stable inside the disc of radius 1 centered at minus 1. The RK4 region is larger: it reaches about minus 2.79 on the real axis and about plus and minus 2.83 j on the imaginary axis. The point h-lambda equal to minus 2.5, from lambda equal to minus 50 and h equal to 0.05, lies outside the Euler disc but inside the RK4 region.',
    b)

# ---------- 8. Planar two-link arm: workspace and the two inverse-kinematics solutions ----------
# Values from "Forward and Inverse Kinematics of a Planar Arm": l1 = 1.0, l2 = 0.7, target from
# forward kinematics at theta1 = 30 deg, theta2 = 45 deg; the second solution is computed by the
# article's inverse-kinematics formulas.
l1, l2 = 1.0, 0.7
fk = lambda t1, t2: (l1*math.cos(t1) + l2*math.cos(t1+t2), l1*math.sin(t1) + l2*math.sin(t1+t2))
tx, ty = fk(math.radians(30), math.radians(45))
def ik(x, y, sign):
    c = (x*x + y*y - l1*l1 - l2*l2) / (2*l1*l2)
    t2 = math.atan2(sign*math.sqrt(1 - c*c), c)
    return math.atan2(y, x) - math.atan2(l2*math.sin(t2), l1 + l2*math.cos(t2)), t2
sc, ox, oy = 150, 280, 300
X = lambda v: ox + v*sc
Y = lambda v: oy - v*sc
b = ''
ro, ri = (l1+l2)*sc, abs(l1-l2)*sc
b += (f'  <path class="region" fill-rule="evenodd" d="M{ox-ro:.1f},{oy} a{ro:.1f},{ro:.1f} 0 1,0 {2*ro:.1f},0 a{ro:.1f},{ro:.1f} 0 1,0 {-2*ro:.1f},0 '
      f'M{ox-ri:.1f},{oy} a{ri:.1f},{ri:.1f} 0 1,0 {2*ri:.1f},0 a{ri:.1f},{ri:.1f} 0 1,0 {-2*ri:.1f},0 z" />\n')
b += f'  <circle class="mut" cx="{ox}" cy="{oy}" r="{ro:.1f}" stroke-dasharray="4 4" />\n'
b += f'  <circle class="mut" cx="{ox}" cy="{oy}" r="{ri:.1f}" stroke-dasharray="4 4" />\n'
b += line([(X(-1.8), oy), (X(1.85), oy)], 'grid')
b += line([(ox, Y(-0.4)), (ox, Y(1.8))], 'grid')
b += text(X(1.85), oy-6, var('x'), 'end', 'small')
b += text(ox+6, Y(1.75), var('y'), 'start', 'small')
for sign, cls, extra in ((1, 'acc', ''), (-1, 'ln', ' stroke-dasharray="6 4"')):
    t1, t2 = ik(tx, ty, sign)
    ex, ey = l1*math.cos(t1), l1*math.sin(t1)
    b += line([(ox, oy), (X(ex), Y(ey)), (X(tx), Y(ty))], cls, extra)
    b += f'  <circle class="box" cx="{X(ex):.1f}" cy="{Y(ey):.1f}" r="4" />\n'
    label = var('θ') + '<tspan class="sub" dy="3">2</tspan><tspan dy="-3"> = ' + ('' if sign > 0 else '−') + f'{abs(math.degrees(t2)):.0f}°</tspan>'
    b += text(X(ex) + (10 if sign > 0 else -10), Y(ey) + (16 if sign > 0 else -6), label, 'start' if sign > 0 else 'end', 'small')
b += f'  <circle class="box" cx="{ox}" cy="{oy}" r="5" />\n'
b += f'  <circle class="dot" cx="{X(tx):.1f}" cy="{Y(ty):.1f}" r="4.5" />\n'
b += text(X(tx)-8, Y(ty)-12, f'target ({tx:.2f}, {ty:.2f})', 'end', 'small')
b += text(ox-8, oy+18, 'base', 'end', 'small')
b += text(X(-0.95), Y(0.8), 'reachable workspace', 'middle', 'small')
b += text(X(-0.95), Y(0.8)+16, f'{abs(l1-l2):g} ≤ ' + var('r') + f' ≤ {l1+l2:g}', 'middle', 'small')
svg('PlanarArmIK', 580, 360, 'Workspace of a two-link planar arm and the two joint solutions for one target',
    f'The shaded ring between radius {abs(l1-l2):g} and radius {l1+l2:g} around the base is the set of points the arm can reach. '
    f'A target at ({tx:.2f}, {ty:.2f}) is reached in two ways: with theta2 = 45 degrees and the elbow below the line from base to target (solid), '
    f'or with theta2 = −45 degrees and the elbow above it (dashed).',
    b)

# ---------- 9. One-dimensional fusion of a prediction and a measurement ----------
# Values from "Sensing and State Estimation: An Overview": predicted position 10.0 m with variance
# 0.25 m^2, range measurement 10.6 m with variance 0.09 m^2; the fused estimate uses the article's
# formulas K = P / (P + R), x = x_pred + K (z - x_pred), P' = (1 - K) P.
xp, Pp, zm, Rm = 10.0, 0.25, 10.6, 0.09
Kg = Pp / (Pp + Rm); xf = xp + Kg*(zm - xp); Pf = (1 - Kg)*Pp
gauss = lambda m, v: (lambda x: math.exp(-(x - m)**2 / (2*v)) / math.sqrt(2*math.pi*v))
P = Plot(56, 30, 540, 200, (8.8, 11.8), (0, 1.7))
b = P.axes([9, 9.5, 10, 10.5, 11, 11.5], [0, 0.5, 1.0, 1.5], 'position  ' + var('x') + '  (m)', 'probability density')
b += P.curve(gauss(xp, Pp), cls='ln')
b += P.curve(gauss(zm, Rm), cls='mut', extra=' stroke-dasharray="5 4"')
b += P.curve(gauss(xf, Pf))
for m, v, label, dx, anchor in ((xp, Pp, 'prediction', -10, 'end'), (zm, Rm, 'measurement', 14, 'start'), (xf, Pf, 'fused estimate', 0, 'middle')):
    peak = gauss(m, v)(m)
    b += text(P.X(m) + dx, P.Y(peak) - 8, label, anchor, 'small')
    b += line([(P.X(m), P.Y(0)), (P.X(m), P.Y(peak))], 'grid')
svg('GaussianFusion', 620, 280, 'Fusing a predicted position with a range measurement',
    f'Three bell-shaped curves over position. The prediction is centered at {xp:g} meters with standard deviation {math.sqrt(Pp):.2f} meters; '
    f'the measurement is centered at {zm:g} meters with standard deviation {math.sqrt(Rm):.2f} meters. The fused estimate is centered at {xf:.2f} meters, '
    f'between the two and closer to the more precise measurement, and is narrower than either, with standard deviation {math.sqrt(Pf):.2f} meters.',
    b)

# ---------- 10. Nonlinearity of a platinum resistance sensor (PT100) ----------
# Values from "Measurement Systems and Sensor Characteristics": R(T) = R0 (1 + A T + B T^2) with the
# IEC 60751 coefficients for 0 to 100 degC; the plotted error is the deviation of R(T) from the
# straight line through its end points, expressed in degC by dividing by the average sensitivity.
R0, Ac, Bc = 100.0, 3.9083e-3, -5.775e-7
Rpt = lambda T: R0*(1 + Ac*T + Bc*T*T)
Savg = (Rpt(100) - Rpt(0)) / 100
nl = lambda T: (Rpt(T) - (Rpt(0) + Savg*T)) / Savg
P = Plot(60, 30, 520, 190, (0, 100), (0, 0.45))
b = P.axes([0, 20, 40, 60, 80, 100], [0, 0.1, 0.2, 0.3, 0.4], 'temperature  ' + var('T') + '  (°C)', 'nonlinearity error  (°C)')
b += P.curve(nl)
b += f'  <circle class="dot" cx="{P.X(50):.1f}" cy="{P.Y(nl(50)):.1f}" r="3.5" />\n'
b += text(P.X(50), P.Y(nl(50)) - 10, f'maximum {nl(50):.3f} °C at 50 °C', 'middle', 'small')
b += text(P.X(50), P.Y(0.08), f'average sensitivity {Savg:.4f} Ω/°C', 'middle', 'small')
svg('SensorNonlinearity', 620, 270, 'Nonlinearity error of a PT100 sensor between 0 and 100 degrees Celsius',
    f'A curve of the difference between the PT100 resistance and the straight line joining its values at 0 and 100 degrees Celsius, '
    f'expressed in degrees Celsius. The error is zero at both ends and rises to a maximum of about {nl(50):.2f} degrees at 50 degrees Celsius.',
    b)

# ---------- 11. Wheatstone bridge ----------
# Arm names follow "Signal Conditioning: Bridges, Amplifiers and Analog Filters":
# V_out = V_A - V_B = V_ex (R2 / (R1 + R2) - R4 / (R3 + R4)); R2 is the sensor in a quarter bridge.
def resistor(p, q, label, lx, ly, anchor, sensor=False):
    (x1, y1), (x2, y2) = p, q
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    hl, hw = 22, 8
    o = line([(x1, y1), (cx - ux*hl, cy - uy*hl)]) + line([(cx + ux*hl, cy + uy*hl), (x2, y2)])
    o += f'  <rect class="box" x="{cx-hl:.1f}" y="{cy-hw:.1f}" width="{2*hl}" height="{2*hw}" transform="rotate({ang:.1f} {cx:.1f} {cy:.1f})" />\n'
    if sensor:
        # variable-resistor arrow drawn across the body
        o += arrow([(cx - 24, cy + 24), (cx + 24, cy - 24)], 'acc')
    o += text(lx, ly, label, anchor)
    return o
T, Lf, Rt, Bt = (230, 50), (130, 150), (330, 150), (230, 250)
sub = lambda v, s: var(v) + f'<tspan class="sub" dy="3">{s}</tspan><tspan dy="-3"> </tspan>'
b = ''
b += resistor(T, Lf, sub('R', '1'), 160, 88, 'end')
b += resistor(Lf, Bt, sub('R', '2') + ' (sensor)', 142, 214, 'end', sensor=True)
b += resistor(T, Rt, sub('R', '3'), 300, 88, 'start')
b += resistor(Rt, Bt, sub('R', '4'), 300, 222, 'start')
b += line([T, (T[0], 18)]) + text(T[0] + 10, 24, '+' + sub('V', 'ex'))
b += line([Bt, (Bt[0], 278)]) + line([(Bt[0]-14, 278), (Bt[0]+14, 278)]) + text(Bt[0] + 20, 283, '0 V')
for (x, y) in (T, Lf, Rt, Bt):
    b += f'  <circle class="dot" cx="{x}" cy="{y}" r="3.5" />\n'
b += line([Lf, (60, 150)]) + f'  <circle class="box" cx="56" cy="150" r="4" />\n' + text(56, 136, sub('V', 'A'), 'middle')
b += line([Rt, (400, 150)]) + f'  <circle class="box" cx="404" cy="150" r="4" />\n' + text(404, 136, sub('V', 'B'), 'middle')
b += text(230, 155, sub('V', 'out') + '= ' + sub('V', 'A') + '− ' + sub('V', 'B'), 'middle', 'small')
svg('WheatstoneBridge', 460, 296, 'Wheatstone bridge with a resistive sensor in one arm',
    'Four resistors form a diamond between the excitation voltage at the top and 0 volts at the bottom. '
    'R1 and R2 form the left divider, whose midpoint is A; R3 and R4 form the right divider, whose midpoint is B. '
    'R2 is the sensor. The output is the difference between the voltages at A and B.',
    b)

# ---------- 12. Butterworth low-pass magnitude responses ----------
# Values from "Signal Conditioning: Bridges, Amplifiers and Analog Filters":
# |H(f)| = 1 / sqrt(1 + (f / fc)^(2n)) for n = 1, 2, 4, plotted in dB against f / fc on a log axis;
# the marked points are the attenuations at f = 5 fc (50 Hz with fc = 10 Hz).
mag = lambda r, n: 20*math.log10(1/math.sqrt(1 + r**(2*n)))
P = Plot(60, 30, 520, 210, (-1, 1.5), (-70, 5))
b = ''
for v in (0, -20, -40, -60):
    b += line([(P.x0, P.Y(v)), (P.x0+P.w, P.Y(v))], 'grid')
    b += text(P.x0-6, P.Y(v)+4, f'{v:g}' if v == 0 else f'−{-v:g}', 'end', 'small')
for v, lab in ((-1, '0.1'), (0, '1'), (1, '10')):
    b += line([(P.X(v), P.y0), (P.X(v), P.y0+P.h)], 'grid')
    b += text(P.X(v), P.y0+P.h+16, lab, 'middle', 'small')
b += line([(P.x0, P.y0), (P.x0, P.y0+P.h), (P.x0+P.w, P.y0+P.h)])
b += text(P.x0+P.w, P.y0+P.h+34, 'frequency relative to cut-off  ' + var('f') + ' / ' + sub('f', 'c'), 'end', 'small')
b += text(P.x0, P.y0-10, 'magnitude  (dB)', 'start', 'small')
b += line([(P.X(0), P.Y(-3.01)), (P.X(-1), P.Y(-3.01))], 'mut', ' stroke-dasharray="3 3"')
b += text(P.X(-1)+6, P.Y(-3.01)+16, '−3 dB', 'start', 'small')
x5 = math.log10(5)
b += line([(P.X(x5), P.y0), (P.X(x5), P.y0+P.h)], 'mut', ' stroke-dasharray="4 4"')
b += text(P.X(x5)+6, P.y0+12, var('f') + ' = 5' + sub('f', 'c'), 'start', 'small')
for n, cls in ((1, 'ln'), (2, 'ln'), (4, 'acc')):
    # sample the curve and stop it where it leaves the plotted range
    pts = [(P.X(u), P.Y(mag(10**u, n))) for u in (-1 + i*2.5/400 for i in range(401)) if mag(10**u, n) >= -70]
    b += line(pts, cls, ' stroke-dasharray="6 4"' if n == 1 else '')
    m5 = mag(5, n)
    b += f'  <circle class="dot" cx="{P.X(x5):.1f}" cy="{P.Y(m5):.1f}" r="3.5" />\n'
    if n == 1:  # above right of the marker, clear of the falling first-order curve
        b += text(P.X(x5)+8, P.Y(m5)-8, f'−{-m5:.1f} dB', 'start', 'small')
    else:
        b += text(P.X(x5)+8, P.Y(m5)+4, f'−{-m5:.1f} dB', 'start', 'small')
for n, lx, ly in ((1, 1.5, mag(10**1.5, 1)+3), (2, 1.5, mag(10**1.5, 2)+3)):
    b += text(P.X(lx), P.Y(ly)+18, f'{["", "first", "second"][n]} order', 'end', 'small')
b += text(P.X(0.5)-8, P.Y(-40)+4, 'fourth order', 'end', 'small')
svg('ButterworthResponse', 620, 286, 'Magnitude responses of first-, second- and fourth-order Butterworth low-pass filters',
    'Magnitude in decibels against frequency relative to the cut-off frequency, on a logarithmic axis from 0.1 to about 30. '
    'All three curves are flat below the cut-off and pass through minus 3 decibels at the cut-off. Above it they fall at 20, 40 and 80 decibels per decade. '
    f'At five times the cut-off frequency the attenuations are {-mag(5,1):.1f}, {-mag(5,2):.1f} and {-mag(5,4):.1f} decibels.',
    b)

# ---------- 13. Aliasing: a 9 Hz sinusoid sampled at 10 Hz ----------
# Values from "Sampling, Quantization and Data Conversion": cos(2 pi 9 t) sampled at fs = 10 Hz
# (t = n / 10) gives cos(2 pi 0.9 n) = cos(2 pi 0.1 n), the same samples as a 1 Hz sinusoid.
fs, fhi, flo = 10.0, 9.0, 1.0
P = Plot(60, 30, 520, 180, (0, 1), (-1.25, 1.25))
b = P.axes([0, 0.2, 0.4, 0.6, 0.8, 1.0], [-1, 0, 1], 'time  ' + var('t') + '  (s)', 'amplitude')
b += P.curve(lambda t: math.cos(2*math.pi*fhi*t), n=600, cls='ln')
b += P.curve(lambda t: math.cos(2*math.pi*flo*t), n=300, cls='acc', extra=' stroke-dasharray="7 4"')
for k in range(int(fs) + 1):
    t = k / fs
    b += f'  <circle class="dot" cx="{P.X(t):.1f}" cy="{P.Y(math.cos(2*math.pi*fhi*t)):.1f}" r="4.5" />\n'
b += text(P.X(0.5), P.Y(-1.25) + 52, f'samples every 0.1 s ({fs:g} Hz)', 'middle', 'small')
b += text(P.x0+P.w, P.y0-10, f'solid: {fhi:g} Hz signal · dashed: {flo:g} Hz alias · dots: samples', 'end', 'small')
svg('Aliasing', 620, 290, 'A 9 hertz sinusoid sampled at 10 hertz produces the same samples as a 1 hertz sinusoid',
    'Over one second, a solid curve oscillates nine times and a dashed curve once. Eleven sample points, taken every 0.1 seconds, '
    'lie on both curves, so the samples alone cannot tell the 9 hertz signal from its 1 hertz alias.',
    b)

# ---------- 14. Voltage noise density with a 1/f corner ----------
# Values from "Noise, Interference and the Limits of Detection": e(f) = e_w sqrt(1 + f_nc / f) with
# white density e_w = 10 nV/sqrt(Hz) and corner frequency f_nc = 10 Hz, on log-log axes.
ew, fcorner = 10.0, 10.0
dens = lambda f: ew*math.sqrt(1 + fcorner/f)
P = Plot(70, 30, 510, 200, (-2, 3), (0.5, 2.7))   # log10(f / Hz), log10(e / nV/sqrt(Hz))
b = ''
for v, lab in ((1, '10'), (2, '100')):
    b += line([(P.x0, P.Y(v)), (P.x0+P.w, P.Y(v))], 'grid')
    b += text(P.x0-6, P.Y(v)+4, lab, 'end', 'small')
for v, lab in ((-2, '0.01'), (-1, '0.1'), (0, '1'), (1, '10'), (2, '100'), (3, '1000')):
    b += line([(P.X(v), P.y0), (P.X(v), P.y0+P.h)], 'grid')
    b += text(P.X(v), P.y0+P.h+16, lab, 'middle', 'small')
b += line([(P.x0, P.y0), (P.x0, P.y0+P.h), (P.x0+P.w, P.y0+P.h)])
b += text(P.x0+P.w, P.y0+P.h+34, 'frequency  ' + var('f') + '  (Hz)', 'end', 'small')
b += text(P.x0, P.y0-10, 'noise density  (nV/√Hz)', 'start', 'small')
# asymptotes: white floor and the 1/f line e_w sqrt(f_nc / f)
b += line([(P.X(-2), P.Y(1)), (P.X(3), P.Y(1))], 'mut', ' stroke-dasharray="4 4"')
b += line([(P.X(-2), P.Y(math.log10(ew*math.sqrt(fcorner/0.01)))), (P.X(1.6), P.Y(math.log10(ew*math.sqrt(fcorner/10**1.6))))], 'mut', ' stroke-dasharray="4 4"')
b += P.curve(lambda u: math.log10(dens(10**u)), n=300)
b += f'  <circle class="dot" cx="{P.X(1):.1f}" cy="{P.Y(math.log10(dens(10))):.1f}" r="3.5" />\n'
b += text(P.X(1)+8, P.Y(math.log10(dens(10)))-10, 'corner ' + sub('f', 'nc') + '= 10 Hz', 'start', 'small')
b += text(P.X(2.6), P.Y(1)-8, 'white: 10 nV/√Hz', 'middle', 'small')
b += text(P.X(-1.0)+6, P.Y(math.log10(dens(0.1)))-14, '1/' + var('f') + ' region', 'start', 'small')
svg('NoiseDensity', 620, 286, 'Voltage noise density of an amplifier with a 1/f corner at 10 hertz',
    'On logarithmic axes, the noise density is flat at 10 nanovolts per root hertz above about 10 hertz and rises '
    'with falling frequency below it, as one over the square root of frequency, reaching about 316 nanovolts per root hertz at 0.01 hertz. '
    'The corner frequency, where the two asymptotes meet, is 10 hertz; there the density is the square root of two times the white level.',
    b)

# ---------- 15. Capacitive MEMS accelerometer (schematic) ----------
# Geometry of "Smart Sensors and MEMS": a proof mass on springs between two fixed electrodes. When the
# case accelerates, the mass lags behind, one gap closes to d - x and the other opens to d + x, and
# the difference between the two capacitances measures x and hence the acceleration.
b = ''
def zigzag_v(x, y0, y1, n=6, w=10):
    pts = [(x, y0), (x, y0 + 8)]
    h = (y1 - y0 - 16) / n
    for i in range(n):
        pts.append((x + (w if i % 2 == 0 else -w), y0 + 8 + (i + 0.5) * h))
    pts += [(x, y1 - 8), (x, y1)]
    return line(pts)
# anchors (hatched) at top and bottom
for ya, sgn in ((34, -1), (226, 1)):
    b += line([(215, ya), (305, ya)])
    for xx in range(219, 305, 10):
        b += line([(xx, ya), (xx - 8, ya + sgn * 8)], 'mut')
b += zigzag_v(260, 34, 90)
b += zigzag_v(260, 170, 226)
b += text(278, 66, 'spring ' + var('k'), 'start', 'small')
# proof mass and fixed electrodes
b += box(190, 90, 140, 80, 'proof mass', var('m'))
for x0 in (110, 398):
    b += f'  <rect class="region" x="{x0}" y="80" width="12" height="100" />\n'
    b += line([(x0, 80), (x0 + 12, 80), (x0 + 12, 180), (x0, 180), (x0, 80)])
b += text(116, 72, 'fixed electrode', 'middle', 'small')
b += text(404, 72, 'fixed electrode', 'middle', 'small')
b += text(156, 126, sub('C', '1'), 'middle')
b += text(364, 126, sub('C', '2'), 'middle')
b += text(156, 148, var('d') + ' + ' + var('x'), 'middle', 'small')
b += text(364, 148, var('d') + ' − ' + var('x'), 'middle', 'small')
# motion arrows: the mass moves right (x) relative to the case when the case accelerates left
b += arrow([(320, 188), (370, 188)], 'acc')
b += text(345, 206, 'mass displacement ' + var('x'), 'middle', 'small')
b += arrow([(300, 252), (220, 252)])
b += text(210, 256, 'case acceleration ' + var('a'), 'end', 'small')
svg('MemsAccelerometer', 520, 266, 'Schematic of a capacitive MEMS accelerometer',
    'A proof mass m hangs on springs between two anchors and sits between two fixed electrodes, forming capacitances C1 and C2. '
    'When the case accelerates to the left, the mass lags behind and moves to the right relative to it by x: the gap to the left electrode '
    'widens to d plus x and the gap to the right electrode narrows to d minus x, so C1 falls and C2 rises.',
    b)

# ==================== Critical Thinking and Reasoning series ====================

# ---------- 02-meaning-clarity-and-definitions ----------

# ---------- Critical thinking series, entry 2: necessary and sufficient conditions ----------
def ct_mcd_ellipse(cx, cy, rx, ry, cls):
    return f'  <ellipse class="{cls}" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" />\n'
def ct_mcd_dot(cx, cy):
    return f'  <circle class="dot" cx="{cx}" cy="{cy}" r="4" />\n'
b = ''
b += f'  <rect class="ln" x="10" y="10" width="580" height="250" rx="4" />\n'
b += text(22, 30, 'All integers', 'start', 'small')
b += ct_mcd_ellipse(250, 140, 200, 100, 'region')
b += ct_mcd_ellipse(250, 140, 200, 100, 'ln')
b += text(250, 62, 'Even integers (' + var('Y') + ')', 'middle')
b += ct_mcd_ellipse(220, 152, 92, 54, 'region')
b += ct_mcd_ellipse(220, 152, 92, 54, 'ln')
b += text(220, 140, 'Multiples of 6', 'middle')
b += text(220, 158, '(' + var('X') + ')', 'middle')
b += ct_mcd_dot(220, 182)
b += text(232, 186, '12', 'start', 'small')
b += ct_mcd_dot(370, 140)
b += text(382, 144, '4', 'start', 'small')
b += ct_mcd_dot(520, 200)
b += text(532, 204, '9', 'start', 'small')
b += text(522, 80, var('X') + ' is sufficient for ' + var('Y'), 'middle', 'small')
b += text(522, 98, var('Y') + ' is necessary for ' + var('X'), 'middle', 'small')
svg('CtNecessarySufficient', 600, 270, 'Euler diagram of a sufficient and a necessary condition',
    'Inside the rectangle of all integers, a large region holds the even integers and a smaller region inside it holds the multiples of 6. The number 12 lies in both regions, the number 4 lies in the even region only, and the number 9 lies outside both. Because the smaller region is entirely inside the larger one, being a multiple of 6 is sufficient for being even, and being even is necessary for being a multiple of 6. The number 4 shows that being a multiple of 6 is not necessary for being even.',
    b)

# ---------- 05-categorical-logic-and-venn-diagrams ----------

# ---------- Critical thinking 5: categorical logic and Venn diagrams ----------
# Helpers prefixed ct_venn_. A region of a Venn diagram is given by a membership tuple
# (one entry per circle: 1 inside, 0 outside). Region outlines are traced from the circle
# arcs that bound them, so shading always follows the drawn circles exactly.

def ct_venn_inside(c, x, y):
    return (x - c[0]) ** 2 + (y - c[1]) ** 2 < c[2] ** 2

def ct_venn_arcs(circles, i):
    """Split circle i at its intersections with the others; return (a0, a1) angle pairs."""
    cx, cy, r = circles[i]
    angs = []
    for j, (dx, dy, rr) in enumerate(circles):
        if j == i:
            continue
        d = math.hypot(dx - cx, dy - cy)
        if d >= r + rr or d <= abs(r - rr):
            continue
        a = (r * r - rr * rr + d * d) / (2 * d)
        base = math.atan2(dy - cy, dx - cx)
        off = math.acos(max(-1.0, min(1.0, a / r)))
        angs += [(base + off) % (2 * math.pi), (base - off) % (2 * math.pi)]
    angs.sort()
    if not angs:
        return [(0.0, 2 * math.pi)]
    return [(angs[k], angs[k + 1] if k + 1 < len(angs) else angs[0] + 2 * math.pi) for k in range(len(angs))]

def ct_venn_pt(c, a):
    return (c[0] + c[2] * math.cos(a), c[1] + c[2] * math.sin(a))

def ct_venn_boundary(circles, m):
    """Boundary arcs of region m, each oriented so that the region lies on one consistent side."""
    arcs = []
    for i, c in enumerate(circles):
        for a0, a1 in ct_venn_arcs(circles, i):
            px, py = ct_venn_pt(c, (a0 + a1) / 2)
            if all(ct_venn_inside(circles[j], px, py) == bool(m[j]) for j in range(len(circles)) if j != i):
                n = 48
                pts = [ct_venn_pt(c, a0 + (a1 - a0) * k / n) for k in range(n + 1)]
                arcs.append(pts if m[i] else pts[::-1])
    return arcs

def ct_venn_chain(circles, m):
    """Closed outline of region m as a list of points, its boundary arcs joined end to start."""
    arcs = ct_venn_boundary(circles, m)
    chain = list(arcs.pop(0))
    while arcs:
        end = chain[-1]
        k = min(range(len(arcs)), key=lambda q: math.hypot(arcs[q][0][0] - end[0], arcs[q][0][1] - end[1]))
        chain += arcs.pop(k)[1:]
    return chain

def ct_venn_path(circles, m):
    return 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in ct_venn_chain(circles, m)) + ' Z'

def ct_venn_shade(circles, m):
    return f'  <path class="region" d="{ct_venn_path(circles, m)}" />\n'

def ct_venn_outline(circles, m, k=0.84):
    """Dashed outline of region m, shrunk toward its center so that it stays visible inside the circles."""
    cx, cy = ct_venn_center(circles, m)
    chain = ct_venn_chain(circles, m)
    d = 'M' + ' L'.join(f'{cx + k * (x - cx):.1f},{cy + k * (y - cy):.1f}' for x, y in chain) + ' Z'
    return f'  <path class="region2" d="{d}" />\n'

def ct_venn_center(circles, m, step=2.0):
    """Point of region m farthest from every circle boundary (a good place for a mark or label)."""
    xs = [c[0] - c[2] for c in circles] + [c[0] + c[2] for c in circles]
    ys = [c[1] - c[2] for c in circles] + [c[1] + c[2] for c in circles]
    best, bp = -1.0, None
    y = min(ys)
    while y <= max(ys):
        x = min(xs)
        while x <= max(xs):
            if all(ct_venn_inside(c, x, y) == bool(m[j]) for j, c in enumerate(circles)):
                dist = min(abs(math.hypot(x - c[0], y - c[1]) - c[2]) for c in circles)
                if dist > best:
                    best, bp = dist, (x, y)
            x += step
        y += step
    return bp

def ct_venn_on_line(circles, m1, m2):
    """Midpoint of the arc that separates two regions differing in one circle."""
    j = [k for k in range(len(m1)) if m1[k] != m2[k]][0]
    inner = m1 if m1[j] else m2
    for a0, a1 in ct_venn_arcs(circles, j):
        px, py = ct_venn_pt(circles[j], (a0 + a1) / 2)
        if all(ct_venn_inside(circles[k], px, py) == bool(inner[k]) for k in range(len(circles)) if k != j):
            return (px, py)

def ct_venn_x(p, s=7):
    x, y = p
    return line([(x - s, y - s), (x + s, y + s)], 'thick') + line([(x - s, y + s), (x + s, y - s)], 'thick')

def ct_venn_frame(x, y, w, h, circles, names, label_pos):
    o = f'  <rect class="ln" x="{x}" y="{y}" width="{w}" height="{h}" />\n'
    for c in circles:
        o += f'  <circle class="ln" cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{c[2]:.1f}" />\n'
    for nm, (lx, ly, anc) in zip(names, label_pos):
        o += text(lx, ly, var(nm), anc)
    return o

# --- Figure 1: the four categorical forms on two-circle diagrams ---
def ct_venn_two(ox, oy, kind, head, sub):
    r = 46
    cs = [(ox + 92, oy + 92, r), (ox + 152, oy + 92, r)]
    o = text(ox + 122, oy + 16, head, 'middle')
    o += text(ox + 122, oy + 32, sub, 'middle', 'small')
    if kind == 'A':
        o += ct_venn_shade(cs, (1, 0))
    if kind == 'E':
        o += ct_venn_shade(cs, (1, 1))
    o += ct_venn_frame(ox + 20, oy + 40, 204, 106, cs, ['S', 'P'],
                       [(ox + 36, oy + 60, 'start'), (ox + 208, oy + 60, 'end')])
    if kind == 'I':
        o += ct_venn_x(ct_venn_center(cs, (1, 1)))
    if kind == 'O':
        o += ct_venn_x(ct_venn_center(cs, (1, 0)))
    return o

b = ''
b += ct_venn_two(0, 0, 'A', 'A: All S are P', 'S outside P is empty')
b += ct_venn_two(256, 0, 'E', 'E: No S are P', 'S inside P is empty')
b += ct_venn_two(0, 168, 'I', 'I: Some S are P', 'something is in S and P')
b += ct_venn_two(256, 168, 'O', 'O: Some S are not P', 'something is in S outside P')
svg('CtVennFourForms', 500, 322, 'Venn diagrams of the four categorical forms',
    'Four two-circle diagrams, each with circle S on the left and circle P on the right inside a rectangle. '
    'A, all S are P: the part of S outside P is shaded. E, no S are P: the overlap of S and P is shaded. '
    'I, some S are P: an X in the overlap. O, some S are not P: an X in the part of S outside P.',
    b)

# --- three-circle layout shared by the remaining figures ---
CT_VENN_R = 62
def ct_venn_three(ox, oy):
    return [(ox + 110, oy + 98, CT_VENN_R), (ox + 186, oy + 98, CT_VENN_R), (ox + 148, oy + 164, CT_VENN_R)]
def ct_venn_three_frame(ox, oy, cs, names=('S', 'P', 'M')):
    return ct_venn_frame(ox + 20, oy + 14, 256, 238, cs, names,
                         [(ox + 44, oy + 44, 'start'), (ox + 252, oy + 44, 'end'), (ox + 148, oy + 244, 'middle')])

# --- Figure 2: the eight regions of a three-circle diagram ---
cs = ct_venn_three(0, 0)
b = ct_venn_three_frame(0, 0, cs)
order = [(1, 0, 0), (1, 1, 0), (0, 1, 0), (1, 0, 1), (1, 1, 1), (0, 1, 1), (0, 0, 1)]
for k, m in enumerate(order):
    x, y = ct_venn_center(cs, m)
    b += text(x, y + 5, str(k + 1), 'middle')
b += text(36, 238, '8', 'middle')
rows = ['1  S, not P, not M', '2  S and P, not M', '3  P, not S, not M', '4  S and M, not P',
        '5  S, P and M', '6  P and M, not S', '7  M, not S, not P', '8  none of the three']
for k, t in enumerate(rows):
    b += text(300, 46 + 26 * k, t, 'start', 'small')
svg('CtVennRegions', 470, 262, 'The eight regions of a three-circle Venn diagram',
    'Three overlapping circles S (upper left), P (upper right) and M (bottom) inside a rectangle divide it into eight regions, '
    'numbered 1 to 7 inside the circles and 8 outside them. A key lists each region: 1 S only, 2 S and P but not M, 3 P only, '
    '4 S and M but not P, 5 all three, 6 P and M but not S, 7 M only, 8 none.',
    b)

def ct_venn_numbers(cs, shift=None):
    """Small region numbers (as in CtVennRegions); regions in `shift` move their number below a mark."""
    shift = shift or {}
    o = ''
    for k, m in enumerate([(1, 0, 0), (1, 1, 0), (0, 1, 0), (1, 0, 1), (1, 1, 1), (0, 1, 1), (0, 0, 1)]):
        x, y = ct_venn_center(cs, m)
        dx, dy = shift.get(k + 1, (0, 0))
        o += text(x + dx, y + 4 + dy, str(k + 1), 'middle', 'small')
    return o

def ct_venn_side(lines, x=300, y=40):
    o = ''
    for k, (t, cls) in enumerate(lines):
        o += text(x, y + 22 * k, t, 'start', cls)
    return o

# --- Figure 3: a valid syllogism (All M are P; some S are M; so some S are P) ---
cs = ct_venn_three(0, 0)
b = ''
b += ct_venn_shade(cs, (1, 0, 1))   # All M are P: M outside P is empty (S, M, not P)
b += ct_venn_shade(cs, (0, 0, 1))   # (M only)
b += ct_venn_three_frame(0, 0, cs)
b += ct_venn_outline(cs[:2], (1, 1))
cx5, cy5 = ct_venn_center(cs, (1, 1, 1))
b += ct_venn_x((cx5, cy5 - 9), 5.5)
b += ct_venn_numbers(cs, {5: (0, 8)})
b += ct_venn_side([('Premise 1: All M are P', None), ('  shade M outside P', 'small'),
                   ('Premise 2: Some S are M', None), ('  X in S and M; the only', 'small'),
                   ('  unshaded part is region 5', 'small'),
                   ('Conclusion: Some S are P', None), ('  dashed: S and P', 'small'),
                   ('An X lies inside the dashed', 'small'), ('region, so the form is valid.', 'small')])
svg('CtVennValid', 500, 262, 'Venn diagram test of a valid syllogism',
    'Circles S, P and M. Premise 1, all M are P, shades the two parts of M outside P. Premise 2, some S are M, puts an X in the '
    'overlap of S and M; because the part of that overlap outside P is shaded, the X goes in the region common to S, P and M. '
    'The conclusion, some S are P, needs an X in the overlap of S and P, outlined with a dashed line. The X is there, so the argument form is valid.',
    b)

# --- Figure 4: an invalid syllogism (All P are M; some S are M; so some S are P) ---
cs = ct_venn_three(0, 0)
b = ''
b += ct_venn_shade(cs, (1, 1, 0))   # All P are M: P outside M is empty
b += ct_venn_shade(cs, (0, 1, 0))
b += ct_venn_three_frame(0, 0, cs)
b += ct_venn_outline(cs[:2], (1, 1))
b += ct_venn_x(ct_venn_on_line(cs, (1, 0, 1), (1, 1, 1)))
b += ct_venn_numbers(cs, {4: (-6, 4), 5: (8, -6)})
b += ct_venn_side([('Premise 1: All P are M', None), ('  shade P outside M', 'small'),
                   ('Premise 2: Some S are M', None), ('  X in S and M, on the line:', 'small'),
                   ('  region 4 or region 5', 'small'),
                   ('Conclusion: Some S are P', None), ('  dashed: S and P', 'small'),
                   ('The X may lie outside P, so', 'small'), ('the form is invalid.', 'small')])
svg('CtVennInvalid', 500, 262, 'Venn diagram test of an invalid syllogism',
    'Circles S, P and M. Premise 1, all P are M, shades the two parts of P outside M. Premise 2, some S are M, puts an X in the '
    'overlap of S and M; neither part of that overlap is shaded, so the X sits on the boundary of P, between the region of S and M only '
    'and the region common to all three. The conclusion, some S are P, needs an X inside the dashed overlap of S and P. The X may lie '
    'outside it, so the argument form is invalid.',
    b)

# ---------- 06-sentential-logic ----------

# ---------- Critical thinking 6: parse tree of a sentential-logic WFF ----------
def ct_sl_f(s):
    # set sentence letters in italics
    return ''.join(var(c) if c in 'PQR' else c for c in s)
def ct_sl_node(cx, cy, label, w):
    return (f'  <rect class="box" x="{cx-w/2:.1f}" y="{cy-16:.1f}" width="{w}" height="32" rx="3" />\n'
            + text(cx, cy+5, ct_sl_f(label), 'middle'))
ct_sl_nodes = {
    'root': (300, 34, '¬(P ∧ Q) → (¬P ∨ R)', 190),
    'l':    (160, 112, '¬(P ∧ Q)', 96),
    'r':    (440, 112, '¬P ∨ R', 84),
    'll':   (160, 190, 'P ∧ Q', 76),
    'rl':   (380, 190, '¬P', 50),
    'rr':   (500, 190, 'R', 40),
    'lll':  (110, 268, 'P', 40),
    'llr':  (210, 268, 'Q', 40),
    'rll':  (380, 268, 'P', 40),
}
ct_sl_edges = [('root','l','→'), ('root','r','→'), ('l','ll','¬'), ('r','rl','∨'), ('r','rr','∨'),
               ('ll','lll','∧'), ('ll','llr','∧'), ('rl','rll','¬')]
b = ''
for a, c, _ in ct_sl_edges:
    x1, y1 = ct_sl_nodes[a][0], ct_sl_nodes[a][1] + 16
    x2, y2 = ct_sl_nodes[c][0], ct_sl_nodes[c][1] - 16
    b += line([(x1, y1), (x2, y2)], 'mut')
for k, (cx, cy, lab, w) in ct_sl_nodes.items():
    b += ct_sl_node(cx, cy, lab, w)
# main-connective labels beside each compound node
for k, mc in [('root', '→'), ('l', '¬'), ('r', '∨'), ('ll', '∧'), ('rl', '¬')]:
    cx, cy, lab, w = ct_sl_nodes[k]
    b += text(cx + w/2 + 8, cy + 5, 'main: ' + mc, 'start', 'small')
b += text(300, 306, 'Leaves: sentence letters', 'middle', 'small')
svg('CtSlParseTree', 600, 318, 'Parse tree of the formula not (P and Q) implies (not P or R)',
    'The whole formula is a conditional, so its main connective is the arrow. It splits into the antecedent not (P and Q) and the consequent not P or R. The antecedent is a negation of the conjunction P and Q, which splits into P and Q. The consequent is a disjunction of not P and R, and not P is the negation of P. Every branch ends in a sentence letter.',
    b)

# ---------- 07-predicate-logic ----------

# ---------- Critical thinking 7: two small counter-models ----------
def ct_pl_ellipse(cx, cy, rx, ry, cls):
    return f'  <ellipse class="{cls}" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" />\n'
def ct_pl_dot(cx, cy, lab):
    return f'  <circle class="dot" cx="{cx}" cy="{cy}" r="5" />\n' + text(cx, cy + 22, lab, 'middle')
b = ''
# panel A: monadic counter-model, domain {1, 2}
b += text(150, 24, '(a) Domain &#123;1, 2&#125;', 'middle', 'small')
b += ct_pl_ellipse(150, 130, 128, 72, 'region2')     # G holds of both objects
b += ct_pl_ellipse(102, 130, 42, 42, 'region')        # F = {1}
b += ct_pl_ellipse(198, 130, 42, 42, 'region')        # H = {2}
b += ct_pl_dot(102, 126, '1')
b += ct_pl_dot(198, 126, '2')
b += text(76, 102, var('F'), 'middle')
b += text(224, 102, var('H'), 'middle')
b += text(150, 72, var('G') + ' (dashed)', 'middle')
b += text(150, 228, var('F') + ' = &#123;1&#125;,  ' + var('G') + ' = &#123;1, 2&#125;,  ' + var('H') + ' = &#123;2&#125;', 'middle', 'small')
# panel B: relational counter-model, domain {1, 2}
b += text(470, 24, '(b) Domain &#123;1, 2&#125;', 'middle', 'small')
x1, x2, y = 405, 535, 126
b += ct_pl_dot(x1, y, '1')
b += ct_pl_dot(x2, y, '2')
b += f'  <path class="ln" d="M{x1+8},{y-8} Q{(x1+x2)/2},{y-62} {x2-8},{y-8}" marker-end="ARROW" />\n'
b += f'  <path class="ln" d="M{x2-8},{y+8} Q{(x1+x2)/2},{y+62} {x1+8},{y+8}" marker-end="ARROW" />\n'
b += text((x1+x2)/2, y-44, var('R') + '(1, 2)', 'middle', 'small')
b += text((x1+x2)/2, y+56, var('R') + '(2, 1)', 'middle', 'small')
b += text(470, 228, var('R') + ' = &#123;(1, 2), (2, 1)&#125;; no loops', 'middle', 'small')
b += line([(310, 40), (310, 236)], 'grid')
svg('CtPlCounterModels', 620, 244, 'Two counter-models with a two-element domain',
    'Panel a: objects 1 and 2. The predicate F holds of 1 only, H holds of 2 only, and G holds of both. Something is both F and G, and something is both G and H, but nothing is both F and H. Panel b: objects 1 and 2 with arrows for the relation R from 1 to 2 and from 2 to 1 and no arrow from an object to itself. Every object has an arrow pointing into it, but no object has arrows to every object.',
    b)

# ---------- 08-scientific-reasoning-and-causation ----------

# ---------- Critical thinking 8: fishbone (Ishikawa) diagram ----------
def ct_sci_fishbone():
    b = ''
    sy = 170                      # spine height
    b += arrow([(20, sy), (536, sy)], 'thick')
    b += box(538, sy - 26, 96, 52, 'Parts', 'dropped')
    bones = [
        (200, -1, 'Machine', ['worn suction cup', 'vacuum hose leak']),
        (360, -1, 'Method', ['approach too fast', 'stale pick offset']),
        (520, -1, 'Material', ['oily part surface', 'tray out of spec']),
        (200, 1, 'People', ['skipped cleaning', 'wrong recipe']),
        (360, 1, 'Measurement', ['camera drift', 'loose vacuum limit']),
        (520, 1, 'Environment', ['press vibration', 'dust on nozzle']),
    ]
    run, rise = 70, 115
    for xs, sgn, name, causes in bones:
        tip = (xs - run, sy + sgn * rise)
        b += arrow([tip, (xs - 3, sy + sgn * 3)])
        ly = tip[1] - 10 if sgn < 0 else tip[1] + 20
        b += text(tip[0], ly, name, 'middle')
        for frac in (0.3, 0.65):
            y = sy + sgn * rise * (1 - frac)
            x = xs - run * (1 - frac)
            b += arrow([(x - 112, y), (x - 3, y)], 'mut')
            b += text(x - 20, y - 5, causes[0 if frac == 0.3 else 1], 'end', 'small')
    return b

svg('CtSciFishbone', 640, 320, 'Fishbone diagram for a gripper that drops parts',
    'A horizontal spine leads to the effect, parts dropped by a pick-and-place gripper. Six bones branch from the spine, three above and three below, '
    'one for each category of cause: machine (worn suction cup, vacuum hose leak), method (approach too fast, stale pick offset), '
    'material (oily part surface, tray out of specification), people (skipped cleaning, wrong recipe), measurement (camera drift, loose vacuum limit) '
    'and environment (press vibration, dust on nozzle).',
    ct_sci_fishbone())

# ---------- 09-probability-and-statistical-reasoning ----------

# ---------- Critical thinking 9: standard normal curve with two shaded tails ----------
def ct_stat_phi(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)

def ct_stat_normal_tails():
    P = Plot(56, 34, 540, 196, (-4, 4), (0, 0.42))
    b = P.axes([-4, -3, -2, -1, 0, 1, 2, 3, 4], [0, 0.1, 0.2, 0.3, 0.4], 'standardized value  ' + var('z'), 'density  ' + var('φ(z)'))
    zc = 1.96
    for lo, hi in ((-4, -zc), (zc, 4)):
        n = 60
        pts = [(P.X(lo + i * (hi - lo) / n), P.Y(ct_stat_phi(lo + i * (hi - lo) / n))) for i in range(n + 1)]
        d = f'M{P.X(lo):.1f},{P.Y(0):.1f} ' + ' '.join(f'L{x:.1f},{y:.1f}' for x, y in pts) + f' L{P.X(hi):.1f},{P.Y(0):.1f} Z'
        b += f'  <path class="band" d="{d}" />\n'
    for zz in (-zc, zc):
        b += line([(P.X(zz), P.Y(0)), (P.X(zz), P.Y(0.3))], 'mut', ' stroke-dasharray="4 4"')
        b += text(P.X(zz), P.Y(0.3) - 6, ('−' if zz < 0 else '') + '1.96', 'middle', 'small')
    b += P.curve(ct_stat_phi)
    b += text(P.X(0), P.Y(0.17), '95%', 'middle')
    b += text(P.X(-2.75), P.Y(0.06), '2.5%', 'middle', 'small')
    b += text(P.X(2.75), P.Y(0.06), '2.5%', 'middle', 'small')
    return b

svg('CtStatNormalTails', 620, 276, 'Standard normal density with the two 2.5 percent tails shaded',
    'The bell-shaped standard normal density, computed from phi of z equals the exponential of minus z squared over 2 divided by the square root of 2 pi, '
    'is plotted from z equals minus 4 to 4. Dashed lines at minus 1.96 and plus 1.96 enclose 95 percent of the area; the shaded tails beyond them hold 2.5 percent each.',
    ct_stat_normal_tails())

# ---------- Critical thinking 9: posterior probability against prior for three likelihood ratios ----------
def ct_stat_posterior(prior, lr):
    return lr * prior / (lr * prior + 1 - prior)

def ct_stat_bayes_plot():
    P = Plot(56, 34, 520, 210, (-3, 0), (0, 1))
    b = ''
    for v in (0, 0.25, 0.5, 0.75, 1):
        b += line([(P.x0, P.Y(v)), (P.x0 + P.w, P.Y(v))], 'grid')
        b += text(P.x0 - 6, P.Y(v) + 4, f'{v:g}', 'end', 'small')
    for e, lab in ((-3, '0.001'), (-2, '0.01'), (-1, '0.1'), (0, '1')):
        b += text(P.X(e), P.y0 + P.h + 16, lab, 'middle', 'small')
    b += line([(P.x0, P.y0), (P.x0, P.y0 + P.h), (P.x0 + P.w, P.y0 + P.h)])
    b += text(P.x0 + P.w, P.y0 + P.h + 34, 'prior  ' + var('P(D)') + '  (log scale)', 'end', 'small')
    b += text(P.x0, P.y0 - 12, 'posterior  ' + var('P(D | alarm)'), 'start', 'small')
    for lr, cls in ((1, 'mut'), (49, 'acc'), (2401, 'acc')):
        b += P.curve(lambda e, lr=lr: ct_stat_posterior(10 ** e, lr), cls=cls)
    b += text(P.X(-0.55) - 10, P.Y(ct_stat_posterior(10 ** -0.55, 1)), 'LR = 1', 'end', 'small')
    b += text(P.X(-1.9) + 8, P.Y(ct_stat_posterior(10 ** -1.9, 49)) + 14, 'LR = 49', 'start', 'small')
    b += text(P.X(-1.6), P.Y(ct_stat_posterior(10 ** -1.6, 2401)) + 22, 'LR = 2401', 'start', 'small')
    pr = 0.005
    b += line([(P.X(math.log10(pr)), P.Y(0)), (P.X(math.log10(pr)), P.Y(1))], 'mut', ' stroke-dasharray="3 3"')
    for lr in (49, 2401):
        q = ct_stat_posterior(pr, lr)
        b += f'  <circle class="dot" cx="{P.X(math.log10(pr)):.1f}" cy="{P.Y(q):.1f}" r="3.5" />\n'
        b += text(P.X(math.log10(pr)) + 8, P.Y(q) + 4, f'{q:.2f}', 'start', 'small')
    b += text(P.X(math.log10(pr)) + 8, P.Y(0.04), 'prior 0.005', 'start', 'small')
    return b

svg('CtStatBayesPosterior', 600, 290, 'Posterior probability of a defect as a function of the prior',
    'Three curves show the posterior probability P of D given the evidence, computed from the odds form of Bayes theorem, against the prior P of D on a logarithmic axis from 0.001 to 1. '
    'With a likelihood ratio of 1 the posterior equals the prior. With a likelihood ratio of 49, one alarm, a prior of 0.005 becomes 0.20; with 2401, two independent alarms, it becomes 0.92.',
    ct_stat_bayes_plot())

# ---------- 10-reasoning-about-values ----------

# ---------- Critical thinking 10: Hohfeld's jural relations ----------
def ct_val_square(ox, title, tl, tr, bl, br):
    bw, bh, gap = 120, 40, 150
    yt, yb = 62, 182
    o = text(ox + (gap + bw) / 2, 36, title, 'middle')
    o += box(ox, yt, bw, bh, tl)
    o += box(ox + gap, yt, bw, bh, tr)
    o += box(ox, yb, bw, bh, bl)
    o += box(ox + gap, yb, bw, bh, br)
    # correlatives: vertical solid lines
    for cx in (ox + bw / 2, ox + gap + bw / 2):
        o += line([(cx, yt + bh), (cx, yb)])
    # opposites: dashed diagonals
    o += line([(ox + bw, yt + bh), (ox + gap, yb)], 'region2')
    o += line([(ox + gap, yt + bh), (ox + bw, yb)], 'region2')
    return o

b = ''
b += ct_val_square(80, 'Conduct', 'Claim-right', 'Privilege', 'Duty', 'No-right')
b += ct_val_square(370, 'Changing positions', 'Power', 'Immunity', 'Liability', 'Disability')
b += line([(80, 252), (120, 252)])
b += text(128, 256, 'correlatives: if A holds the upper position against B, B holds the lower one', 'start', 'small')
b += line([(80, 276), (120, 276)], 'region2')
b += text(128, 280, 'opposites: two positions of the same party; whoever holds one lacks the other', 'start', 'small')
svg('CtValHohfeld', 650, 292, "Hohfeld's eight jural positions",
    "Two squares. Vertical lines join correlatives, one relation seen from each party: a claim-right of A against B goes with a duty of B to A, a privilege of A with a no-right of B, a power of A with a liability of B, an immunity of A with a disability of B. Dashed diagonals join opposites, two positions of the same party that exclude each other: claim-right and no-right, privilege and duty, power and disability, immunity and liability.",
    b)

# ---------- 11-strategic-thinking-and-decisions ----------

# ---------- Critical thinking 11: SWOT grid for a hypothetical robotics startup ----------
def ct_strat_cell(x, y, w, h, title, items):
    o = f'  <rect class="box" x="{x}" y="{y}" width="{w}" height="{h}" rx="3" />\n'
    o += text(x + 12, y + 24, title)
    for i, it in enumerate(items):
        o += text(x + 12, y + 50 + 21 * i, '• ' + it, 'start', 'small')
    return o

b = ''
x0, y0, cw, ch = 84, 44, 272, 132
b += text(x0 + cw / 2, 30, 'Helpful to the goal', 'middle', 'small')
b += text(x0 + cw * 1.5 + 8, 30, 'Harmful to the goal', 'middle', 'small')
b += text(14, y0 + ch / 2 - 4, 'Internal', 'start', 'small')
b += text(14, y0 + ch / 2 + 12, '(the team)', 'start', 'small')
b += text(14, y0 + ch * 1.5 + 4, 'External', 'start', 'small')
b += text(14, y0 + ch * 1.5 + 20, '(the market)', 'start', 'small')
b += ct_strat_cell(x0, y0, cw, ch, 'Strengths',
                   ['Navigation stack written in-house', 'Two pilot sites already running', 'Low hardware cost per robot', 'Fast release cycle'])
b += ct_strat_cell(x0 + cw + 8, y0, cw, ch, 'Weaknesses',
                   ['No certified safety case yet', 'One person knows the firmware', 'No dedicated sales staff', 'Thin test coverage on hardware'])
b += ct_strat_cell(x0, y0 + ch + 8, cw, ch, 'Opportunities',
                   ['Integrator looking for a robot partner', 'Cheaper lidar modules appearing', 'Night shifts hard to staff', 'Customers asking for open APIs'])
b += ct_strat_cell(x0 + cw + 8, y0 + ch + 8, cw, ch, 'Threats',
                   ['Large vendor entering the segment', 'Customer IT forbids cloud links', 'Long lead times on motor drivers', 'Liability if a robot hurts someone'])
svg('CtStratSwot', 650, y0 + 2 * ch + 20, 'SWOT grid for a hypothetical warehouse-robot startup',
    'A two-by-two grid. Columns separate factors helpful and harmful to the goal; rows separate internal factors, which the team controls, from external factors in the market. Strengths include an in-house navigation stack and two pilot sites; weaknesses include no certified safety case and a single person who knows the firmware; opportunities include an integrator seeking a partner and cheaper lidar; threats include a large vendor entering and customer bans on cloud links.',
    b)

# ---------- Critical thinking 11: expected value versus P(high demand) ----------
def ct_strat_ev(name, q):
    return {'Small': 47 - 20 * q, 'Medium': 59 - 10 * q, 'Large': 33 + 60 * q}[name]

P = Plot(60, 30, 470, 210, (0, 0.7), (20, 80))
b = P.axes([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], [20, 40, 60, 80],
           'probability of high demand  ' + var('q') + '  (P(low) = 0.3)', 'expected payoff (thousand dollars)')
qb = 26 / 70
b += line([(P.X(qb), P.Y(20)), (P.X(qb), P.Y(80))], 'mut', ' stroke-dasharray="3 3"')
b += line([(P.X(0.2), P.Y(20)), (P.X(0.2), P.Y(80))], 'grid', ' stroke-dasharray="2 3"')
b += P.curve(lambda q: ct_strat_ev('Small', q), cls='mut', extra=' stroke-dasharray="6 4"')
b += P.curve(lambda q: ct_strat_ev('Medium', q), cls='ln')
b += P.curve(lambda q: ct_strat_ev('Large', q), cls='acc')
b += f'  <circle class="dot" cx="{P.X(qb):.1f}" cy="{P.Y(ct_strat_ev("Medium", qb)):.1f}" r="3.5" />\n'
b += text(P.X(qb) + 6, P.Y(24), var('q') + ' ≈ 0.37', 'start', 'small')
b += text(P.X(0.2) + 4, P.Y(77), 'estimate 0.2', 'start', 'small')
b += text(P.X(0.7) + 6, P.Y(ct_strat_ev('Large', 0.7)) + 4, 'Large', 'start', 'small')
b += text(P.X(0.7) + 6, P.Y(ct_strat_ev('Medium', 0.7)) + 4, 'Medium', 'start', 'small')
b += text(P.X(0.7) + 6, P.Y(ct_strat_ev('Small', 0.7)) + 4, 'Small', 'start', 'small')
svg('CtStratSensitivity', 600, 290, 'Expected payoff of three capacity options as the probability of high demand varies',
    'Three straight lines. Medium falls slowly from 59 to 52, Small falls from 47 to 33, Large rises steeply from 33 to 75 as the probability of high demand goes from 0 to 0.7 with the probability of low demand held at 0.3. Large overtakes Medium at about 0.37; at the estimate 0.2 Medium is best.',
    b)

# ---------- 13-creativity-and-generating-ideas ----------

# ---------- Critical thinking 13: divergent and convergent phases ----------

def ct_cr_diamond(x0, x1, cy, half_h):
    """Outline of one diverge-converge phase: a point at x0 widens to +-half_h at the midpoint and narrows to x1."""
    xm = (x0 + x1) / 2
    return line([(x0, cy), (xm, cy - half_h), (x1, cy), (xm, cy + half_h), (x0, cy)], 'ln')

def ct_cr_dots(x0, x1, cy, half_h):
    """Idea dots in columns: the count grows across the divergent half and shrinks to one across the convergent half."""
    xm = (x0 + x1) / 2
    cols = [(0.12, 1), (0.28, 2), (0.44, 3), (0.60, 4), (0.78, 5), (1.22, 3), (1.50, 2), (1.80, 1)]
    out = ''
    for f, n in cols:
        x = x0 + f * (xm - x0)
        lim = (x - x0) / (xm - x0) * half_h if f <= 1 else (x1 - x) / (x1 - xm) * half_h
        span = min(lim - 12, 13 * (n - 1))
        for i in range(n):
            y = cy if n == 1 else cy - span + 2 * span * i / (n - 1)
            out += f'  <circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="3.5" />\n'
    return out

b = ''
cy, hh = 120, 70
phases = [(30, 290, 'Understand the problem', 'Define it'), (330, 590, 'Generate solutions', 'Select and test')]
for k, (x0, x1, left, right) in enumerate(phases):
    xm = (x0 + x1) / 2
    b += ct_cr_diamond(x0, x1, cy, hh)
    b += line([(xm, cy - hh), (xm, cy + hh)], 'mut', ' stroke-dasharray="4 4"')
    b += ct_cr_dots(x0, x1, cy, hh)
    b += text((x0 + xm) / 2, cy - hh - 26, 'diverge', 'middle')
    b += text((x0 + xm) / 2, cy - hh - 10, left, 'middle', 'small')
    b += text((xm + x1) / 2, cy - hh - 26, 'converge', 'middle')
    b += text((xm + x1) / 2, cy - hh - 10, right, 'middle', 'small')
b += arrow([(290, cy), (330, cy)])
b += arrow([(590, cy), (606, cy), (606, cy + hh + 30), (30, cy + hh + 30), (30, cy + 8)], 'mut')
b += text(318, cy + hh + 46, 'a test exposes a new problem: start again with what was learned', 'middle', 'small')
svg('CtDivergeConverge', 620, 250, 'Two diverge-converge phases in sequence',
    'Two diamond shapes side by side. In each, the left half widens from a point and holds many idea dots: this is divergent thinking, where options are generated and judgment is deferred. The right half narrows to a point and holds only a few dots: this is convergent thinking, where options are evaluated and selected. The first diamond is about understanding and defining the problem, the second about generating and selecting solutions. An arrow from the end of the second diamond returns to the start of the first, because testing a solution often exposes a new problem.',
    b)
