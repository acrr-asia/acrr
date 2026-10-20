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

# ==================== Bayesian Deep Learning series ====================

# ---------- 01-bayesian-inference-for-neural-networks ----------

# ---------- BDL entry 1: posterior predictive of Bayesian linear regression ----------
import numpy as _bdl_np

def bdl_bi_model():
    rng = _bdl_np.random.default_rng(seed=0)
    sigma, s0 = 0.25, 1.0
    centers = _bdl_np.arange(-5.0, 5.5, 1.0)
    feats = lambda x: _bdl_np.exp(-(x[:, None] - centers[None, :]) ** 2)
    x = _bdl_np.concatenate([rng.uniform(-3, -1, 10), rng.uniform(1, 3, 10)])
    y = _bdl_np.sin(x) + rng.normal(0.0, sigma, size=x.size)
    Phi = feats(x)
    S = _bdl_np.linalg.inv(Phi.T @ Phi / sigma**2 + _bdl_np.eye(centers.size) / s0**2)
    m = S @ Phi.T @ y / sigma**2
    return x, y, feats, m, S, sigma

def bdl_bi_band_path(P, xs, lo, hi):
    pts = [(P.X(a), P.Y(b)) for a, b in zip(xs, hi)] + [(P.X(a), P.Y(b)) for a, b in zip(xs[::-1], lo[::-1])]
    return ' '.join(('M' if i == 0 else 'L') + f'{px:.1f},{py:.1f}' for i, (px, py) in enumerate(pts)) + ' Z'

bx, by, bfeats, bm, bS, bsig = bdl_bi_model()
g = _bdl_np.linspace(-5, 5, 201)
F = bfeats(g)
mu = F @ bm
epi = _bdl_np.einsum('ij,jk,ik->i', F, bS, F)
tot = _bdl_np.sqrt(epi + bsig**2)
epi = _bdl_np.sqrt(epi)
P = Plot(56, 30, 540, 230, (-5, 5), (-3, 3))
b = P.axes([-4, -2, 0, 2, 4], [-2, 0, 2], 'input  ' + var('x'), 'output  ' + var('y'))
b += f'  <path class="region" d="{bdl_bi_band_path(P, g, mu - 2*tot, mu + 2*tot)}" />\n'
b += f'  <path class="band" d="{bdl_bi_band_path(P, g, mu - 2*epi, mu + 2*epi)}" />\n'
b += P.curve(math.sin, cls='mut', extra=' stroke-dasharray="5 4"')
b += line([(P.X(a), P.Y(c)) for a, c in zip(g, mu)], 'acc')
for a, c in zip(bx, by):
    b += f'  <circle class="dot" cx="{P.X(a):.1f}" cy="{P.Y(c):.1f}" r="3" />\n'
# legend
lx, ly = 62, 322
b += f'  <rect class="band" x="{lx}" y="{ly-9}" width="22" height="10" />\n'
b += text(lx+28, ly, '±2 epistemic sd', 'start', 'small')
b += f'  <rect class="region" x="{lx+150}" y="{ly-9}" width="22" height="10" />\n'
b += text(lx+178, ly, '±2 total sd', 'start', 'small')
b += line([(lx+290, ly-4), (lx+312, ly-4)], 'acc')
b += text(lx+318, ly, 'predictive mean', 'start', 'small')
b += line([(lx+436, ly-4), (lx+458, ly-4)], 'mut', ' stroke-dasharray="5 4"')
b += text(lx+464, ly, 'sin ' + var('x'), 'start', 'small')
svg("BdlPredictiveBand", 640, 332, 'Posterior predictive of Bayesian linear regression with 11 Gaussian features',
    'Twenty noisy observations of sin x lie in two clusters, between minus 3 and minus 1 and between 1 and 3. The predictive mean follows the sine inside the clusters with a narrow band. In the gap between the clusters the epistemic band widens, and beyond the data, near x equal to plus or minus 5, the mean returns to 0 and the band widens to the prior width of about plus or minus 2.',
    b)

# ---------- 02-sampling-the-posterior-mcmc ----------

# ---------- BDL entry 2: random-walk Metropolis versus HMC on a correlated Gaussian ----------
import numpy as _bdl_np2

bdl_mc_C = _bdl_np2.array([[1.0, 0.95], [0.95, 1.0]])
bdl_mc_A = _bdl_np2.linalg.inv(bdl_mc_C)

def bdl_mc_U(t):
    return 0.5 * t @ bdl_mc_A @ t

def bdl_mc_rw(n, step, start, rng):
    t, out = start.copy(), [start.copy()]
    for _ in range(n):
        q = t + step * rng.normal(size=2)
        if _bdl_np2.log(rng.uniform()) < bdl_mc_U(t) - bdl_mc_U(q):
            t = q
        out.append(t.copy())
    return out

def bdl_mc_hmc(n, eps, L, start, rng):
    t, states, trajs = start.copy(), [start.copy()], []
    for _ in range(n):
        r0 = rng.normal(size=2)
        q, r = t.copy(), r0 - 0.5 * eps * bdl_mc_A @ t
        path = [q.copy()]
        for l in range(L):
            q = q + eps * r
            path.append(q.copy())
            if l < L - 1:
                r = r - eps * bdl_mc_A @ q
        r = r - 0.5 * eps * bdl_mc_A @ q
        dH = bdl_mc_U(q) + r @ r / 2 - bdl_mc_U(t) - r0 @ r0 / 2
        if _bdl_np2.log(rng.uniform()) < -dH:
            t = q
        trajs.append(path)
        states.append(t.copy())
    return states, trajs

def bdl_mc_ellipse(P, k):
    w, V = _bdl_np2.linalg.eigh(bdl_mc_C)
    pts = []
    for i in range(121):
        a = 2 * math.pi * i / 120
        v = V @ (k * _bdl_np2.sqrt(w) * _bdl_np2.array([math.cos(a), math.sin(a)]))
        pts.append((P.X(v[0]), P.Y(v[1])))
    return line(pts, 'grid', ' stroke-width="1.5"')

def bdl_mc_panel(P, title):
    o = bdl_mc_ellipse(P, 1) + bdl_mc_ellipse(P, 2)
    o += line([(P.x0, P.y0), (P.x0, P.y0+P.h), (P.x0+P.w, P.y0+P.h)])
    for v in (-2, 0, 2):
        o += text(P.X(v), P.y0+P.h+16, f'{v:g}', 'middle', 'small')
        o += text(P.x0-6, P.Y(v)+4, f'{v:g}', 'end', 'small')
    o += text(P.x0+P.w, P.y0+P.h+34, var('θ') + '<tspan class="sub" dy="3">1</tspan>', 'end', 'small')
    o += text(P.x0, P.y0-10, var('θ') + '<tspan class="sub" dy="3">2</tspan>', 'start', 'small')
    o += text(P.x0+P.w/2, P.y0-10, title, 'middle')
    return o

start = _bdl_np2.array([-2.2, -1.6])
rw = bdl_mc_rw(120, 0.25, start, _bdl_np2.random.default_rng(seed=0))
hs, ht = bdl_mc_hmc(8, 0.15, 15, start, _bdl_np2.random.default_rng(seed=0))
P1 = Plot(46, 30, 250, 250, (-3, 3), (-3, 3))
P2 = Plot(366, 30, 250, 250, (-3, 3), (-3, 3))
b = bdl_mc_panel(P1, 'random-walk Metropolis')
b += line([(P1.X(p[0]), P1.Y(p[1])) for p in rw], 'acc', ' stroke-width="1.5"')
b += f'  <circle class="dot" cx="{P1.X(rw[-1][0]):.1f}" cy="{P1.Y(rw[-1][1]):.1f}" r="4" />\n'
b += bdl_mc_panel(P2, 'Hamiltonian Monte Carlo')
for path in ht:
    b += line([(P2.X(p[0]), P2.Y(p[1])) for p in path], 'mut', ' stroke-dasharray="3 3"')
for p in hs:
    b += f'  <circle class="dot" cx="{P2.X(p[0]):.1f}" cy="{P2.Y(p[1]):.1f}" r="3.5" />\n'
b += f'  <circle class="ln" cx="{P1.X(start[0]):.1f}" cy="{P1.Y(start[1]):.1f}" r="6" />\n'
b += f'  <circle class="ln" cx="{P2.X(start[0]):.1f}" cy="{P2.Y(start[1]):.1f}" r="6" />\n'
b += text(330, 342, 'random walk: 120 proposals; HMC: 8 transitions of 15 leapfrog steps; ellipses at 1 and 2 standard deviations', 'middle', 'small')
svg('BdlSamplerPaths', 650, 352, 'Random-walk Metropolis and Hamiltonian Monte Carlo on a correlated two-dimensional Gaussian',
    'Both samplers start at the same point in the lower left of a narrow Gaussian whose ellipses lie along the diagonal. With 120 proposals, random-walk Metropolis moves in short steps and covers only a small part of the long axis. With the same number of gradient evaluations, Hamiltonian Monte Carlo makes 8 transitions whose leapfrog trajectories, drawn dashed, sweep along the ellipse, so its 8 states spread along most of the long axis, while the random walk stays in the lower half.',
    b)

# ---------- 03-laplace-approximations ----------

# ---------- BDL entry 3: Laplace approximation of 1-D logistic regression ----------
# Recomputes the toy problem of /blog/laplace-approximations (seed 8, N = 20, alpha = 1):
# left, the exact marginal posterior of the slope w (grid) against the Laplace Gaussian;
# right, the predictive probability: plug-in MAP, Laplace (Gauss-Hermite over f ~ N(mu, s2)) and exact.
import numpy as np

def bdl_la_sig(z):
    return 1 / (1 + np.exp(-z))

def bdl_la_problem():
    rng = np.random.default_rng(8)
    N = 20
    x = rng.uniform(-3, 3, N)
    y = (rng.uniform(size=N) < bdl_la_sig(0.5 + 1.5 * x)).astype(float)
    X = np.column_stack([np.ones(N), x])
    alpha = 1.0
    t = np.zeros(2)
    for _ in range(50):
        p = bdl_la_sig(X @ t)
        g = X.T @ (y - p) - alpha * t
        H = X.T @ (X * (p * (1 - p))[:, None]) + alpha * np.eye(2)
        t = t + np.linalg.solve(H, g)
    p = bdl_la_sig(X @ t)
    H = X.T @ (X * (p * (1 - p))[:, None]) + alpha * np.eye(2)
    S = np.linalg.inv(H)
    g1 = np.linspace(-6, 8, 601)
    B, W = np.meshgrid(g1, g1, indexing='ij')
    G = np.stack([B.ravel(), W.ravel()], 1)
    Z = G @ X.T
    lj = (Z * y - np.logaddexp(0, Z)).sum(1) - 0.5 * alpha * (G**2).sum(1)
    post = np.exp(lj - lj.max()); post /= post.sum()
    return x, y, t, S, g1, G, post

bx, by, bt, bS, bg1, bG, bpost = bdl_la_problem()
dw = bg1[1] - bg1[0]
marg_w = bpost.reshape(601, 601).sum(0) / dw          # density of w on the grid

b = ''
# left panel: marginal posterior of w
P = Plot(52, 34, 236, 196, (0, 3.5), (0, 0.9))
b += P.axes([0, 1, 2, 3], [0, 0.4, 0.8], 'slope ' + var('w'), 'density')
sel = (bg1 >= 0) & (bg1 <= 3.5)
b += line([(P.X(v), P.Y(d)) for v, d in zip(bg1[sel], marg_w[sel])], 'thick')
mu, sd = bt[1], math.sqrt(bS[1, 1])
b += P.curve(lambda v: math.exp(-0.5 * ((v - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi)), cls='acc', extra=' stroke-dasharray="6 4"')
b += line([(P.X(mu), P.Y(0)), (P.X(mu), P.Y(0.86))], 'mut', ' stroke-dasharray="2 3"')
b += text(P.X(mu) - 4, P.Y(0.86) + 2, 'MAP', 'end', 'small')
pm = float((bpost @ bG)[1])
b += f'  <circle class="dot" cx="{P.X(pm):.1f}" cy="{P.Y(0):.1f}" r="3.5" />\n'
b += text(P.X(pm) + 6, P.Y(0) - 6, 'exact mean', 'start', 'small')

# right panel: predictive probability
Q = Plot(380, 34, 242, 196, (1.5, 8), (0.85, 1))
b += Q.axes([2, 4, 6, 8], [0.85, 0.9, 0.95, 1], 'input ' + var('x') + '*', 'p(' + var('y') + '* = 1 | ' + var('x') + '*, ' + '𝒟)')
gh_x, gh_w = np.polynomial.hermite_e.hermegauss(40)
gh_w = gh_w / gh_w.sum()
def lap_pred(xs):
    phi = np.array([1.0, xs]); m = phi @ bt; s = math.sqrt(phi @ bS @ phi)
    return float(gh_w @ bdl_la_sig(m + s * gh_x))
def exact_pred(xs):
    return float(bpost @ bdl_la_sig(bG @ np.array([1.0, xs])))
b += Q.curve(lambda v: float(bdl_la_sig(bt[0] + bt[1] * v)), n=160, cls='mut', extra=' stroke-dasharray="3 3"')
b += Q.curve(exact_pred, n=160, cls='thick')
b += Q.curve(lap_pred, n=160, cls='acc', extra=' stroke-dasharray="6 4"')
for xi, yi in zip(bx, by):
    if xi >= 1.5 and yi == 1:
        b += f'  <circle class="dot" cx="{Q.X(xi):.1f}" cy="{Q.Y(yi):.1f}" r="2.5" />\n'

# legend (shared)
ly = 296
b += line([(60, ly), (88, ly)], 'thick') + text(94, ly + 4, 'exact posterior', 'start', 'small')
b += line([(214, ly), (242, ly)], 'acc', ' stroke-dasharray="6 4"') + text(248, ly + 4, 'Laplace', 'start', 'small')
b += line([(326, ly), (354, ly)], 'mut', ' stroke-dasharray="3 3"') + text(360, ly + 4, 'plug-in MAP (right only)', 'start', 'small')
svg('BdlLaplaceLogistic', 640, 308,
    'Laplace approximation of a two-parameter logistic regression compared with the exact posterior',
    'Left: the exact marginal posterior density of the slope w is skewed to the right, with its mean near 1.48, while the '
    'Laplace Gaussian is centered at the MAP value 1.33 with standard deviation 0.50. Right: predictive probability of class 1 '
    'for inputs from 1.5 to 8, on a vertical axis from 0.85 to 1, with the training points of class 1 in that range marked at 1. '
    'The plug-in MAP curve approaches 1 fastest, the exact predictive lies just below it, and the Laplace predictive levels off lowest, near 0.98.',
    b)

# ---------- 04-variational-inference-for-neural-networks ----------

# ---------- BDL entry 4: mean-field Gaussian VI on Bayesian linear regression ----------
# Recomputes the toy problem of /blog/variational-inference-for-neural-networks (seed 1, N = 20,
# noise sd 0.5, prior N(0, I)). The mean-field optimum is known in closed form: mean = exact posterior
# mean, variances = 1 / diag(posterior precision); the listing in the article converges to it.
# Left: 2-sd ellipses of the exact posterior and the mean-field optimum in the (b, w) plane.
# Right: standard deviation of f(x) = b + w x under each, against x, with the data range shaded.
import numpy as np

def bdl_vi_problem():
    rng = np.random.default_rng(1)
    N, s2 = 20, 0.5**2
    x = rng.uniform(0, 4, N)
    y = 1.0 + 0.8 * x + rng.normal(0, 0.5, N)
    X = np.column_stack([np.ones(N), x])
    Lam = X.T @ X / s2 + np.eye(2)
    Sig = np.linalg.inv(Lam)
    m = Sig @ X.T @ y / s2
    return x, m, Lam, Sig

bvx, bvm, bvLam, bvSig = bdl_vi_problem()
bvQ = np.diag(1 / np.diag(bvLam))                     # optimal mean-field covariance

def bdl_vi_ellipse(P, mean, cov, k=2.0, n=120):
    vals, vecs = np.linalg.eigh(cov)
    A = vecs @ np.diag(np.sqrt(vals)) * k
    pts = []
    for i in range(n + 1):
        a = 2 * math.pi * i / n
        v = mean + A @ np.array([math.cos(a), math.sin(a)])
        pts.append((P.X(v[0]), P.Y(v[1])))
    return pts

b = ''
P = Plot(56, 34, 220, 200, (0.1, 1.3), (0.7, 1.2))
b += P.axes([0.2, 0.6, 1.0], [0.8, 1.0, 1.2], 'intercept ' + var('b'), 'slope ' + var('w'))
b += line(bdl_vi_ellipse(P, bvm, bvSig), 'thick')
b += line(bdl_vi_ellipse(P, bvm, bvQ), 'acc', ' stroke-dasharray="6 4"')
b += f'  <circle class="dot" cx="{P.X(bvm[0]):.1f}" cy="{P.Y(bvm[1]):.1f}" r="3" />\n'

Q = Plot(372, 34, 250, 200, (-2, 6), (0, 0.5))
b += Q.axes([-2, 0, 2, 4, 6], [0, 0.25, 0.5], 'input ' + var('x') + '*', 'sd of ' + var('f') + '(' + var('x') + '*)')
b += f'  <rect class="region" x="{Q.X(bvx.min()):.1f}" y="{Q.y0}" width="{Q.X(bvx.max()) - Q.X(bvx.min()):.1f}" height="{Q.h}" />\n'
b += text((Q.X(bvx.min()) + Q.X(bvx.max())) / 2, Q.y0 + 14, 'data range', 'middle', 'small')
b += Q.curve(lambda v: math.sqrt(np.array([1.0, v]) @ bvSig @ np.array([1.0, v])), n=160, cls='thick')
b += Q.curve(lambda v: math.sqrt(np.array([1.0, v]) @ bvQ @ np.array([1.0, v])), n=160, cls='acc', extra=' stroke-dasharray="6 4"')

ly = 296
b += line([(150, ly), (178, ly)], 'thick') + text(184, ly + 4, 'exact posterior', 'start', 'small')
b += line([(330, ly), (358, ly)], 'acc', ' stroke-dasharray="6 4"') + text(364, ly + 4, 'mean-field optimum', 'start', 'small')
svg('BdlMeanFieldVi', 640, 308,
    'Mean-field Gaussian variational approximation of a Bayesian linear regression compared with the exact posterior',
    'Left: in the plane of intercept b and slope w, the exact posterior two-standard-deviation ellipse is long, narrow and tilted, '
    'because the two parameters have correlation minus 0.86. The mean-field ellipse has the same center but is axis-aligned and only about '
    'as wide as the narrow direction of the exact ellipse, so its marginal standard deviations are about half the exact ones. Right: standard '
    'deviation of the regression function against the input from minus 2 to 6, with the range of the training inputs, about 0.1 to 3.8, shaded. The exact curve has '
    'a minimum of about 0.11 inside the data range and rises to above 0.4 at both ends; the mean-field curve is flatter, higher than '
    'the exact curve over most of the data range and much lower outside it.',
    b)

# ---------- 05-deep-ensembles ----------

# ---------- BDL 5. Deep ensemble of five tanh networks on 1-D regression ----------
# Recomputes the toy ensemble of the article "Deep Ensembles and Their Bayesian Interpretation"
# (same data, seeds, architecture and training loop as its first listing).
import numpy as np

def bdl_de_train():
    rng = np.random.default_rng(0)
    N, sigma = 40, 0.1
    x = np.concatenate([rng.uniform(-3, -1, N // 2), rng.uniform(1, 3, N // 2)])
    y = np.sin(x) + sigma * rng.normal(size=N)
    X = x[:, None]
    def init(seed, H=50):
        r = np.random.default_rng(seed)
        return [r.normal(0, 1, (1, H)), r.normal(0, 1, H),
                r.normal(0, 1 / np.sqrt(H), (H, 1)), np.zeros(1)]
    def forward(p, X):
        W1, b1, W2, b2 = p
        h = np.tanh(X @ W1 + b1)
        return h, (h @ W2 + b2).ravel()
    def train(seed, steps=20_000, lr=0.1, lam=1e-4):
        p = init(seed)
        for _ in range(steps):
            h, f = forward(p, X)
            r = (f - y)[:, None] / N
            dh = (r @ p[2].T) * (1 - h ** 2)
            g = [X.T @ dh, dh.sum(0), h.T @ r, r.sum(0)]
            p = [w - lr * (gw + lam * w) for w, gw in zip(p, g)]
        return p
    members = [train(s) for s in range(1, 6)]
    return x, y, sigma, members, forward

def bdl_de_figure():
    x, y, sigma, members, forward = bdl_de_train()
    xs = np.linspace(-6, 6, 241)
    F = np.array([forward(p, xs[:, None])[1] for p in members])
    mean = F.mean(0); sd = np.sqrt(sigma ** 2 + F.var(0))
    P = Plot(56, 24, 548, 230, (-6, 6), (-2.5, 2.5))
    b = ''
    for lo, hi in [(-3, -1), (1, 3)]:
        b += f'  <rect class="region" x="{P.X(lo):.1f}" y="{P.y0}" width="{P.X(hi)-P.X(lo):.1f}" height="{P.h}" />\n'
    b += P.axes([-6, -4, -2, 0, 2, 4, 6], [-2, -1, 0, 1, 2], 'input  ' + var('x'), 'output  ' + var('y'))
    clip = lambda v: max(-2.5, min(2.5, v))
    up = [(P.X(a), P.Y(clip(m + 2 * s))) for a, m, s in zip(xs, mean, sd)]
    dn = [(P.X(a), P.Y(clip(m - 2 * s))) for a, m, s in zip(xs, mean, sd)]
    d = 'M' + ' L'.join(f'{px:.1f},{py:.1f}' for px, py in up + dn[::-1]) + ' Z'
    b += f'  <path class="band" d="{d}" />\n'
    for f in F:
        b += line([(P.X(a), P.Y(clip(v))) for a, v in zip(xs, f)], 'mut')
    b += line([(P.X(a), P.Y(np.sin(a))) for a in xs], 'ln', ' stroke-dasharray="5 4"')
    b += line([(P.X(a), P.Y(clip(m))) for a, m in zip(xs, mean)], 'acc')
    for a, v in zip(x, y):
        b += f'  <circle class="dot" cx="{P.X(a):.1f}" cy="{P.Y(v):.1f}" r="2.6" />\n'
    b += text(P.X(-2), P.y0 + 14, 'data', 'middle', 'small')
    b += text(P.X(2), P.y0 + 14, 'data', 'middle', 'small')
    b += text(P.X(0), P.y0 + 14, 'gap', 'middle', 'small')
    svg('BdlEnsembleDisagreement', 620, 300,
        'Five independently trained networks agree on the data and disagree away from it',
        'Forty noisy samples of sin(x) lie in two shaded intervals, from -3 to -1 and from 1 to 3. '
        'Five tanh networks trained from different random initializations pass through the data almost '
        'identically. Between the intervals and beyond them their curves fan apart, and the band of '
        'plus or minus two predictive standard deviations around the ensemble mean widens, but not enough: '
        'from about x = 3.3 to 4.9, and below about x = -5, the dashed true function lies outside the band.',
        b)

bdl_de_figure()

# ---------- 06-gaussian-processes-and-kernels ----------

# ---------- BDL 6. Gaussian-process prior samples and posterior ----------
# Recomputes the GP example of "Gaussian Processes, Kernels and Infinitely Wide Networks":
# same data (seed 4), squared-exponential kernel, signal sd 1, noise sd 0.1, lengthscale 1.6
# (the grid maximizer of the log marginal likelihood printed by the article's listing).
import numpy as np

def bdl_gp_k(a, b, ell=1.6):
    return np.exp(-0.5 * (a[:, None] - b[None, :]) ** 2 / ell ** 2)

def bdl_gp_figure():
    rng = np.random.default_rng(4)
    x = np.array([-4.0, -3.2, -2.5, -1.0, 0.5, 1.2, 3.5])
    sn = 0.1
    y = np.sin(x) + sn * rng.normal(size=x.size)
    xs = np.linspace(-6, 8, 141)
    Kss = bdl_gp_k(xs, xs)
    # prior samples (seeded separately so they do not depend on the data draw)
    r = np.random.default_rng(6)
    Lp = np.linalg.cholesky(Kss + 1e-8 * np.eye(xs.size))
    prior = (Lp @ r.normal(size=(xs.size, 3))).T
    # posterior of the latent function
    K = bdl_gp_k(x, x) + sn ** 2 * np.eye(x.size)
    L = np.linalg.cholesky(K)
    Ks = bdl_gp_k(x, xs)
    mean = Ks.T @ np.linalg.solve(L.T, np.linalg.solve(L, y))
    V = np.linalg.solve(L, Ks)
    cov = Kss - V.T @ V
    sd = np.sqrt(np.clip(np.diag(cov), 0, None))
    Lq = np.linalg.cholesky(cov + 1e-6 * np.eye(xs.size))
    post = (mean[:, None] + Lq @ r.normal(size=(xs.size, 3))).T

    def panel(P, m, s, samples, title, data):
        b = P.axes([-6, -3, 0, 3, 6], [-2, 0, 2], 'input  ' + var('x'), title)
        clip = lambda v: max(-3, min(3, v))
        up = [(P.X(a), P.Y(clip(mm + 2 * ss))) for a, mm, ss in zip(xs, m, s)]
        dn = [(P.X(a), P.Y(clip(mm - 2 * ss))) for a, mm, ss in zip(xs, m, s)]
        b += '  <path class="band" d="M' + ' L'.join(f'{px:.1f},{py:.1f}' for px, py in up + dn[::-1]) + ' Z" />\n'
        for f in samples:
            b += line([(P.X(a), P.Y(clip(v))) for a, v in zip(xs, f)], 'mut')
        b += line([(P.X(a), P.Y(clip(v))) for a, v in zip(xs, m)], 'acc')
        if data:
            for a, v in zip(x, y):
                b += f'  <circle class="dot" cx="{P.X(a):.1f}" cy="{P.Y(v):.1f}" r="3" />\n'
        return b

    b = panel(Plot(44, 28, 250, 200, (-6, 8), (-3, 3)), np.zeros(xs.size), np.ones(xs.size), prior, 'prior', False)
    b += panel(Plot(358, 28, 250, 200, (-6, 8), (-3, 3)), mean, sd, post, 'posterior', True)
    svg('BdlGpPriorPosterior', 620, 280,
        'Samples and two-standard-deviation bands of a Gaussian-process prior and posterior',
        'Left: three random functions drawn from a Gaussian-process prior with a squared-exponential kernel, '
        'lengthscale 1.6, around a zero mean with a constant band from -2 to 2. Right: after conditioning on seven '
        'noisy observations of sin(x) between x = -4 and x = 3.5, the posterior band is narrow at the data, widens slightly '
        'in the gap between x = 1.2 and x = 3.5, and grows back toward the prior width away from the data on both sides. Three posterior '
        'samples pass close to every observation.',
        b)

bdl_gp_figure()

# ---------- 07-priors-symmetries-and-identifiability ----------

# ---------- BDL entry 7: prior predictive samples for three weight scales ----------
import numpy as _bdl_np

def bdl_pri_functions(s, n_fun, seed, H=50):
    """f(x) = sum_j v_j tanh(u_j x + b_j), u, b ~ N(0, s^2), v ~ N(0, 1/H) (entry 7, Section 2)."""
    r = _bdl_np.random.default_rng(seed)
    xs = _bdl_np.linspace(-3, 3, 241)
    u = r.normal(0, s, size=(n_fun, H, 1))
    b = r.normal(0, s, size=(n_fun, H, 1))
    v = r.normal(0, 1 / _bdl_np.sqrt(H), size=(n_fun, 1, H))
    return xs, (v @ _bdl_np.tanh(u * xs + b)).squeeze(1)

def bdl_pri_panel(x0, s, seed):
    P = Plot(x0, 40, 170, 190, (-3, 3), (-2.5, 2.5))
    o = ''
    for v in (-2, 0, 2):
        o += line([(P.X(-3), P.Y(v)), (P.X(3), P.Y(v))], 'grid')
    for v in (-3, 0, 3):
        o += text(P.X(v), P.Y(-2.5) + 16, f'{v:g}'.replace('-', '−'), 'middle', 'small')
    o += line([(P.x0, P.y0), (P.x0, P.y0 + P.h), (P.x0 + P.w, P.y0 + P.h)])
    xs, F = bdl_pri_functions(s, 6, seed)
    for k, f in enumerate(F):
        pts = [(P.X(a), P.Y(max(-2.5, min(2.5, c)))) for a, c in zip(xs, f)]
        o += line(pts, 'acc' if k == 0 else 'mut')
    o += text(P.x0 + P.w / 2, 26, var('s') + f' = {s:g}', 'middle')
    o += text(P.x0 + P.w / 2, P.y0 + P.h + 34, var('x'), 'middle', 'small')
    return o, P

b = ''
for i, (s, seed) in enumerate([(0.5, 11), (2.0, 12), (8.0, 13)]):
    o, P = bdl_pri_panel(60 + i * 200, s, seed)
    b += o
    if i == 0:
        for v in (-2, 0, 2):
            b += text(P.x0 - 6, P.Y(v) + 4, f'{v:g}'.replace('-', '−'), 'end', 'small')
        b += text(P.x0 - 44, P.y0 - 14, var('f') + '(' + var('x') + ')', 'start', 'small')
svg('BdlPriorSamples', 640, 280,
    'Functions drawn from the prior of a one-hidden-layer tanh network for three weight scales',
    'Three panels show six functions each, drawn from the prior of a network with 50 tanh hidden units on inputs from minus 3 to 3. '
    'With input-weight scale s equal to 0.5 the functions are smooth, close to straight lines. With s equal to 2 they bend a few times. '
    'With s equal to 8 they look like sums of steps and change direction often. The output-weight variance is 1/50 in all panels, so the vertical range stays similar.',
    b)

# ---------- 08-scaling-bayesian-deep-learning ----------

# ---------- BDL entry 8: last-layer Bayesian linear regression on random features ----------
import numpy as _bdl_np

def bdl_ll_fit():
    """Same data, features and posterior as the listing in entry 8, Section 2 (seed 3, alpha = 1)."""
    r = _bdl_np.random.default_rng(3)
    N, K, sigma, alpha = 40, 200, 0.1, 1.0
    x = _bdl_np.r_[r.uniform(-3, -1, N // 2), r.uniform(1, 3, N // 2)]
    y = _bdl_np.sin(2 * x) + sigma * r.normal(size=N)
    omega = r.normal(0, 1.0, size=K)
    phase = r.uniform(0, 2 * _bdl_np.pi, size=K)
    feat = lambda t: _bdl_np.sqrt(2 / K) * _bdl_np.cos(_bdl_np.outer(t, omega) + phase)
    Phi = feat(x)
    A = alpha * _bdl_np.eye(K) + Phi.T @ Phi / sigma**2
    m = _bdl_np.linalg.solve(A, Phi.T @ y) / sigma**2
    xs = _bdl_np.linspace(-6, 6, 361)
    Fs = feat(xs)
    sd = _bdl_np.sqrt(sigma**2 + _bdl_np.einsum('ij,ji->i', Fs, _bdl_np.linalg.solve(A, Fs.T)))
    return x, y, xs, Fs @ m, sd

x, y, xs, mu, sd = bdl_ll_fit()
P = Plot(56, 24, 556, 210, (-6, 6), (-3, 3))
b = ''
up = [(P.X(a), P.Y(min(3, c + 2 * s))) for a, c, s in zip(xs, mu, sd)]
lo = [(P.X(a), P.Y(max(-3, c - 2 * s))) for a, c, s in zip(xs, mu, sd)]
d = 'M' + ' L'.join(f'{a:.1f},{c:.1f}' for a, c in up + lo[::-1]) + ' Z'
b += f'  <path class="band" d="{d}" />\n'
b += P.axes([-6, -4, -2, 0, 2, 4, 6], [-2, 0, 2], 'input  ' + var('x') + '*', 'prediction')
b = b.replace('>-', '>−')
b += P.curve(lambda t: math.sin(2 * t), cls='mut', extra=' stroke-dasharray="4 4"')
b += line([(P.X(a), P.Y(c)) for a, c in zip(xs, mu)], 'acc')
for a, c in zip(x, y):
    b += f'  <circle class="dot" cx="{P.X(a):.1f}" cy="{P.Y(c):.1f}" r="2.6" />\n'
b += text(P.X(0), P.Y(2.55), 'gap', 'middle', 'small')
b += text(P.X(5.9), P.Y(2.55), 'far from data', 'end', 'small')
svg('BdlLastLayer', 640, 280,
    'Posterior predictive of Bayesian linear regression on 200 fixed random features',
    'Forty noisy observations of sin(2x) lie in two clusters, from minus 3 to minus 1 and from 1 to 3. '
    'The predictive mean follows the data inside the clusters with a narrow band of plus or minus two standard deviations. '
    'In the gap around zero the band widens, and beyond about plus or minus 3.5 the mean no longer follows sin(2x) and the band widens to about plus or minus 2, the prior scale.',
    b)

# ---------- 09-evaluating-and-using-uncertainty ----------

# ---------- BDL 9. Evaluating and using predictive uncertainty ----------
# Recomputes the synthetic predictions of the article's first listing (seed 7) and draws
# the reliability diagram and the risk-coverage curves from them.
import numpy as _bdl_np

def bdl_eval_data():
    np = _bdl_np
    rng = np.random.default_rng(seed=7)
    n, k = 6000, 4
    z = rng.normal(0.0, 1.5, size=(n, k))
    p_true = np.exp(z) / np.exp(z).sum(axis=1, keepdims=True)
    y = np.array([rng.choice(k, p=p) for p in p_true])
    logits = 2.5 * (z + rng.normal(0.0, 0.5, size=(n, k)))
    def softmax(a):
        e = np.exp(a - a.max(axis=1, keepdims=True))
        return e / e.sum(axis=1, keepdims=True)
    def nll(p, yy):
        return -np.mean(np.log(p[np.arange(len(yy)), yy]))
    val, test = slice(0, 3000), slice(3000, n)
    temps = np.linspace(0.5, 5.0, 451)
    T = temps[int(np.argmin([nll(softmax(logits[val] / t), y[val]) for t in temps]))]
    return softmax(logits[test]), softmax(logits[test] / T), p_true[test], y[test], T

def bdl_eval_bins(p, y, bins=10, min_count=20):
    np = _bdl_np
    conf, pred = p.max(axis=1), p.argmax(axis=1)
    correct = (pred == y).astype(float)
    edges = np.linspace(0.0, 1.0, bins + 1)
    b = np.clip(np.digitize(conf, edges[1:-1]), 0, bins - 1)
    out = []
    for j in range(bins):
        m = b == j
        if m.sum() >= min_count:
            out.append((j, edges[j], edges[j + 1], conf[m].mean(), correct[m].mean()))
    return out

def bdl_eval_reliability_panel(P, rows, heading):
    o = P.axes([0, 0.5, 1], [0, 0.5, 1], 'confidence', 'accuracy')
    o += text(P.x0 + P.w / 2, 18, heading, 'middle')
    for (_, lo, hi, c, a) in rows:
        o += f'  <rect class="band" x="{P.X(lo) + 1:.1f}" y="{P.Y(a):.1f}" width="{P.X(hi) - P.X(lo) - 2:.1f}" height="{P.Y(0) - P.Y(a):.1f}" />\n'
    o += line([(P.X(0), P.Y(0)), (P.X(1), P.Y(1))], 'mut', ' stroke-dasharray="4 4"')
    o += line([(P.X(c), P.Y(a)) for (_, _, _, c, a) in rows], 'acc')
    for (_, _, _, c, a) in rows:
        o += f'  <circle class="dot" cx="{P.X(c):.1f}" cy="{P.Y(a):.1f}" r="3.5" />\n'
    return o

_p_raw, _p_cal, _p_true, _y, _T = bdl_eval_data()
_P1 = Plot(52, 56, 240, 210, (0, 1), (0, 1))
_P2 = Plot(372, 56, 240, 210, (0, 1), (0, 1))
b = bdl_eval_reliability_panel(_P1, bdl_eval_bins(_p_raw, _y), 'Trained model')
b += bdl_eval_reliability_panel(_P2, bdl_eval_bins(_p_cal, _y), f'After temperature scaling, T = {_T:.2f}')
svg('BdlReliabilityDiagram', 640, 312, 'Reliability diagrams before and after temperature scaling',
    'Ten equal-width confidence bins on 3000 synthetic test predictions; bins with fewer than 20 predictions are omitted. '
    'Bars and dots show the accuracy in each bin against its mean confidence; the dashed diagonal is perfect calibration. '
    'Before scaling the dots lie well below the diagonal, for example 70 percent accuracy at 97 percent mean confidence in the top bin. '
    f'After dividing the logits by T = {_T:.2f} the dots lie close to the diagonal.',
    b)

def bdl_eval_risk_coverage(score, correct):
    np = _bdl_np
    order = np.argsort(-score, kind='stable')
    errors = np.cumsum(~correct[order])
    kept = np.arange(1, len(order) + 1)
    return kept / len(order), errors / kept

_c_cal = _p_cal.argmax(axis=1) == _y
_c_true = _p_true.argmax(axis=1) == _y
_cov, _r_cal = bdl_eval_risk_coverage(_p_cal.max(axis=1), _c_cal)
_, _r_true = bdl_eval_risk_coverage(_p_true.max(axis=1), _c_true)
_, _r_orc = bdl_eval_risk_coverage(_c_cal.astype(float), _c_cal)
P = Plot(60, 30, 540, 220, (0, 1), (0, 0.45))
b = P.axes([0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.1, 0.2, 0.3, 0.4], 'coverage (fraction of inputs answered)', 'selective risk (error rate on answered inputs)')
_start = int(0.05 * len(_cov))
_step = 15
def _pts(r):
    idx = list(range(_start, len(_cov), _step)) + [len(_cov) - 1]
    return [(P.X(_cov[i]), P.Y(r[i])) for i in idx]
b += line([(P.X(0), P.Y(1 - _c_cal.mean())), (P.X(1), P.Y(1 - _c_cal.mean()))], 'mut', ' stroke-dasharray="2 4"')
b += line(_pts(_r_orc), 'ln')
b += line(_pts(_r_true), 'mut', ' stroke-dasharray="6 4"')
b += line(_pts(_r_cal), 'acc')
b += text(P.X(0.02), P.Y(1 - _c_cal.mean()) - 6, 'random order', 'start', 'small')
b += text(P.X(0.30), P.Y(_r_cal[int(0.30 * len(_cov))]) - 10, 'scaled model', 'end', 'small')
b += text(P.X(0.50), P.Y(_r_true[int(0.50 * len(_cov))]) + 18, 'true probabilities', 'start', 'small')
b += text(P.X(0.66), P.Y(0.02), 'oracle', 'start', 'small')
svg('BdlRiskCoverage', 640, 290, 'Risk-coverage curves for selective classification',
    'Selective risk against coverage on the 3000 synthetic test predictions when the least confident inputs are rejected first. '
    'Ranking by the temperature-scaled confidence lowers the risk from 0.41 at full coverage to 0.29 at half coverage. '
    'Ranking by the true class probabilities does a little better; an oracle that rejects exactly the errors reaches zero risk at coverage 0.59. '
    'Rejecting in random order leaves the risk at 0.41.',
    b)

# ---------- 10-frontiers-of-bayesian-deep-learning ----------

# ---------- BDL 10. Frontiers: free energy of a regular and a singular model ----------
# Recomputes the article's listing: F(n) = -log Z(n) with Z(n) the integral over [-1, 1]^2 of
# exp(-n K(a, b)) / 4, for K = (a^2 + b^2) / 2 (regular) and K = (a b)^2 / 2 (singular).
import numpy as _bdl_np10

def bdl_slt_free_energy(n, singular):
    np = _bdl_np10
    a = np.concatenate([[0.0], np.logspace(-9, 0, 20001)])
    if singular:
        g = np.full_like(a, 2.0)
        s = a[1:] * np.sqrt(n / 2)
        g[1:] = np.sqrt(np.pi) * np.array([math.erf(v) for v in s]) / s
    else:
        g = np.exp(-n * a**2 / 2) * np.sqrt(2 * np.pi / n) * math.erf(np.sqrt(n / 2))
    return -np.log(2 * np.trapezoid(g, a) / 4)

_lg = [1 + 0.1 * i for i in range(71)]                    # log10 n from 1 to 8
_Freg = [bdl_slt_free_energy(10 ** v, False) for v in _lg]
_Fsin = [bdl_slt_free_energy(10 ** v, True) for v in _lg]
P = Plot(60, 30, 470, 220, (1, 8), (0, 20))
b = P.axes([1, 2, 3, 4, 5, 6, 7, 8], [0, 5, 10, 15, 20], 'sample size  log' + '<tspan class="sub" dy="3">10</tspan><tspan dy="-3"> </tspan>' + var('n'), 'free energy  ' + var('F') + '(' + var('n') + ') = −log ' + var('Z') + '(' + var('n') + ')')
b += line([(P.X(v), P.Y(f)) for v, f in zip(_lg, _Freg)], 'mut', ' stroke-dasharray="6 4"')
b += line([(P.X(v), P.Y(f)) for v, f in zip(_lg, _Fsin)], 'acc')
b += text(P.X(8) + 8, P.Y(_Freg[-1]) + 4, 'regular: about log ' + var('n'), 'start', 'small')
b += text(P.X(8) + 8, P.Y(_Fsin[-1]) + 4, 'singular: about ½ log ' + var('n'), 'start', 'small')
b += text(P.X(4.6), P.Y(_Freg[36]) - 12, var('K') + ' = (' + var('a') + '² + ' + var('b') + '²)/2', 'end', 'small')
b += text(P.X(4.6), P.Y(_Fsin[36]) + 22, var('K') + ' = (' + var('a') + var('b') + ')²/2', 'start', 'small')
svg('BdlSingularFreeEnergy', 680, 290, 'Free energy of a regular and a singular two-parameter model',
    'The negative log marginal likelihood F of two models with two parameters and a uniform prior on the square from minus 1 to 1, '
    'plotted against the base-10 logarithm of the sample size n from 10 to 100 million. '
    'For the regular model, with K equal to a squared plus b squared over 2, F grows like the natural logarithm of n, as the Bayesian information criterion predicts for two parameters. '
    'For the singular model, with K equal to the square of a times b over 2, F grows much more slowly, like one half of the natural logarithm of n minus a log log n correction.',
    b)
