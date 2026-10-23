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
        'from about x = 3.2 to 5.0, below about x = -5.1 and above about x = 5.8, the dashed true function lies outside the band.',
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

# ==================== Bayesian Deep Learning: book chapters ====================

# ---------- 01-introduction-to-sampling ----------

# ---------- Chapter 1 (introduction-to-sampling): Figures 1.1 to 1.3 ----------
import random as bdl01_random

def bdl01_xticks(P, ticks, labels):
    o = ''
    for v, l in zip(ticks, labels):
        o += text(P.X(v), P.y0 + P.h + 16, l, 'middle', 'small')
    return o

def bdl01_frame(P, xticks, xlabels, yticks, ylabels, xlabel, ylabel):
    o = ''
    for v, l in zip(yticks, ylabels):
        o += line([(P.x0, P.Y(v)), (P.x0 + P.w, P.Y(v))], 'grid')
        o += text(P.x0 - 6, P.Y(v) + 4, l, 'end', 'small')
    o += bdl01_xticks(P, xticks, xlabels)
    o += line([(P.x0, P.y0), (P.x0, P.y0 + P.h), (P.x0 + P.w, P.y0 + P.h)])
    o += text(P.x0 + P.w / 2, P.y0 + P.h + 34, xlabel, 'middle', 'small')
    o += text(P.x0, P.y0 - 10, ylabel, 'start', 'small')
    return o

# Figure 1.1: rejection sampling from Beta(2,2) with a uniform proposal (exact formulas).
beta22 = lambda y: 6 * y * (1 - y)
beta33 = lambda y: 30 * y * y * (1 - y) ** 2
xt = [0, 0.25, 0.5, 0.75, 1]
xl = ['0', '0.25', '0.5', '0.75', '1']
L = Plot(50, 34, 240, 200, (0, 1), (0, 1.9))
b = bdl01_frame(L, xt, xl, [0, 0.5, 1.0, 1.5], ['0.0', '0.5', '1.0', '1.5'], var('y'), var('f') + '(' + var('y') + ')')
b += line([(L.X(0), L.Y(1.5)), (L.X(1), L.Y(1.5))], 'mut', ' stroke-dasharray="1.5 3"')
b += line([(L.X(0), L.Y(1.0)), (L.X(1), L.Y(1.0))], 'ln', ' stroke-dasharray="6 4"')
b += L.curve(beta22)
b += text(L.X(0.98), L.Y(1.5) - 8, var('c') + var('q') + '(' + var('y') + ')', 'end', 'small')
b += text(L.X(0.98), L.Y(1.0) - 8, var('q') + '(' + var('y') + ')', 'end')
b += text(L.X(0.5), L.Y(1.5) + 22, var('π') + '(' + var('y') + ')', 'middle')
R = Plot(380, 34, 240, 200, (0, 1), (0, 1.1))
b += bdl01_frame(R, xt, xl, [0, 0.5, 1.0], ['0.0', '0.5', '1.0'], var('y'), var('k') + '(' + var('y') + ')')
b += R.curve(lambda y: beta22(y) / 1.5)
b += R.curve(lambda y: beta33(y) / (15 / 8), cls='mut', extra=' stroke-dasharray="6 4"')
b += text(R.X(0.42), R.Y(0.45), 'Beta(2,2)', 'start')
b += text(R.X(0.42), R.Y(0.2), 'Beta(3,3)', 'start', 'small')
b += line([(R.X(0.3), R.Y(0.45) - 5), (R.X(0.39), R.Y(0.45) - 5)], 'acc')
b += line([(R.X(0.3), R.Y(0.2) - 4), (R.X(0.39), R.Y(0.2) - 4)], 'mut', ' stroke-dasharray="6 4"')
svg('Bdl01RejectionBeta', 640, 280,
    'Rejection sampling from a Beta(2,2) target with a uniform proposal',
    'Left panel: the Beta(2,2) density 6y(1 minus y) rises from 0 at y equals 0 to 1.5 at y equals 0.5 and falls back to 0 at y equals 1. The uniform proposal q(y) equals 1 lies below the peak, so q alone does not dominate the target, while the envelope c q(y) equals 1.5 touches the peak and lies above the density everywhere. Right panel: the acceptance probability k(y), which is 4y(1 minus y) for the Beta(2,2) target and 16 y squared (1 minus y) squared for a Beta(3,3) target with c equals 15/8. Both reach 1 at y equals 0.5; the Beta(3,3) curve is lower everywhere else.',
    b)

# Figures 1.2 and 1.3: random-walk Metropolis on N(0,1), lambda = 0.9 and 0.01, 5000 iterations.
def bdl01_rwm(lam, n, seed):
    rng = bdl01_random.Random(seed)
    x, out = 0.0, []
    for _ in range(n):
        y = x + lam * rng.gauss(0, 1)
        if rng.random() < min(1.0, __import__('math').exp(-0.5 * (y * y - x * x))):
            x = y
        out.append(x)
    return out

def bdl01_acf(xs, kmax):
    n = len(xs); m = sum(xs) / n
    d = [v - m for v in xs]
    c0 = sum(v * v for v in d) / n
    return [sum(d[i] * d[i + k] for i in range(n - k)) / n / c0 for k in range(kmax + 1)]

N = 5000
chainA = bdl01_rwm(0.9, N, 11)
chainB = bdl01_rwm(0.01, N, 12)

def bdl01_ticks(lo, hi, step):
    import math as _m
    t = _m.ceil(lo / step) * step
    out = []
    while t <= hi + 1e-12:
        out.append(round(t, 10)); t += step
    return out

def bdl01_fmt(v, step):
    dec = max(0, -int(__import__('math').floor(__import__('math').log10(step) + 1e-9)))
    v = round(v, dec) + 0.0
    if v == 0: v = 0.0
    s = f'{v:.{dec}f}'
    return s.replace('-', '−') if v < 0 else s

# Figure 1.2: trace plots.
b = ''
A = Plot(56, 30, 240, 200, (0, N), (-4.2, 4.2))
yt = [-3, -1.5, 0, 1.5, 3]
b += bdl01_frame(A, [0, 1000, 2000, 3000, 4000, 5000], ['0', '1000', '2000', '3000', '4000', '5000'], yt, [bdl01_fmt(v, 0.5) for v in yt], 'Index', var('x'))
d = ''.join(f'M{A.X(i):.1f},{A.Y(v):.1f}h0' for i, v in enumerate(chainA) if i % 2 == 0)
b += f'  <path class="ln" d="{d}" stroke-width="2.2" stroke-linecap="round" />\n'
lo, hi = min(chainB), max(chainB)
pad = 0.08 * (hi - lo)
B = Plot(384, 30, 240, 200, (0, N), (lo - pad, hi + pad))
span = hi - lo
step = 0.1 if span < 0.6 else 0.2 if span < 1.2 else 0.5
ytB = bdl01_ticks(lo - pad, hi + pad, step)
b += bdl01_frame(B, [0, 1000, 2000, 3000, 4000, 5000], ['0', '1000', '2000', '3000', '4000', '5000'], ytB, [bdl01_fmt(v, step) for v in ytB], 'Index', var('x'))
b += line([(B.X(i), B.Y(v)) for i, v in enumerate(chainB) if i % 2 == 0], 'acc')
svg('Bdl01TracePlots', 640, 270,
    'Trace plots of random-walk Metropolis chains for a standard normal target',
    f'Left (every second iteration drawn): with step size 0.9 the 5000 states scatter densely between about minus 3 and 3 around 0 with no visible trend, a well-mixed chain. Right: with step size 0.01 the chain started at 0 drifts slowly as a smooth random walk, covering only the range from about minus {-lo:.2f} to {hi:.2f} in 5000 iterations, a poorly mixing chain.',
    b)

# Figure 1.3: autocorrelation functions with approximate 95 percent bands.
K = 36
acfA, acfB = bdl01_acf(chainA, K), bdl01_acf(chainB, K)
band = 1.96 / N ** 0.5
b = ''
for P, acf in ((Plot(56, 30, 240, 200, (-1.5, K + 1.5), (-0.08, 1.05)), acfA),
               (Plot(384, 30, 240, 200, (-1.5, K + 1.5), (-0.08, 1.05)), acfB)):
    b += bdl01_frame(P, [0, 5, 10, 15, 20, 25, 30, 35], ['0', '5', '10', '15', '20', '25', '30', '35'],
                     [0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0.0', '0.2', '0.4', '0.6', '0.8', '1.0'], 'Lag', 'ACF')
    b += text(P.x0 + P.w / 2, P.y0 - 10, 'Series ' + var('x'), 'middle')
    b += line([(P.x0, P.Y(0)), (P.x0 + P.w, P.Y(0))], 'mut')
    for s in (band, -band):
        b += line([(P.x0, P.Y(s)), (P.x0 + P.w, P.Y(s))], 'mut', ' stroke-dasharray="3 3"')
    for k, r in enumerate(acf):
        b += line([(P.X(k), P.Y(0)), (P.X(k), P.Y(r))], 'acc', ' stroke-width="1.5"')
lagA = next((k for k, r in enumerate(acfA) if r < band), K)
svg('Bdl01AcfPlots', 640, 270,
    'Autocorrelation functions of the two random-walk Metropolis chains',
    f'Bars give the sample autocorrelation at lags 0 to {K}; dashed lines mark plus and minus 1.96 over the square root of 5000. Left, step size 0.9: the autocorrelation falls from 1 at lag 0 to {acfA[1]:.2f} at lag 1 and decays geometrically, entering the band at about lag {lagA}. Right, step size 0.01: the autocorrelation stays close to 1 (about {acfB[K]:.2f} at lag {K}) at every lag shown.',
    b)

# ---------- 02-stochastic-gradient-mcmc ----------

# ===================== Chapter 2: Stochastic Gradient MCMC =====================

def bdl02_contours(f, x0, y0, w, h, levels, nx=110, ny=90):
    # Marching squares on f(u, v), u, v in [0, 1] (v upwards); returns one path string per level.
    X = lambda u: x0 + u * w
    Y = lambda v: y0 + h - v * h
    grid = [[f(i / nx, j / ny) for i in range(nx + 1)] for j in range(ny + 1)]
    out = []
    for lev in levels:
        segs = []
        for j in range(ny):
            for i in range(nx):
                c = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
                vals = [grid[b][a] for a, b in c]
                pts = []
                for k in range(4):
                    (a1, b1), (a2, b2) = c[k], c[(k + 1) % 4]
                    v1, v2 = vals[k], vals[(k + 1) % 4]
                    if (v1 < lev) != (v2 < lev):
                        t = (lev - v1) / (v2 - v1)
                        pts.append((X((a1 + t * (a2 - a1)) / nx), Y((b1 + t * (b2 - b1)) / ny)))
                if len(pts) == 2:
                    segs.append(pts)
                elif len(pts) == 4:
                    segs.append(pts[:2]); segs.append(pts[2:])
        d = ' '.join(f'M{p[0][0]:.1f},{p[0][1]:.1f} L{p[1][0]:.1f},{p[1][1]:.1f}' for p in segs)
        out.append(d)
    return out

def bdl02_sub(t):
    return f'<tspan class="sub" dy="4">{t}</tspan><tspan dy="-4"> </tspan>'

# ---------- Figure 2.1: cyclical and decaying step-size schedules ----------
P = Plot(70, 56, 530, 210, (0, 200), (0, 0.1))
b = P.axes([0, 25, 50, 75, 100, 125, 150, 175, 200], [0, 0.02, 0.04, 0.06, 0.08, 0.1], 'Epochs', 'Step size')
for c in range(4):
    t0 = 50 * c
    cyc = lambda t, t0=t0: 0.05 * (math.cos(math.pi * (t - t0) / 50) + 1)
    pe = [(P.X(t0 + i * 25 / 60), P.Y(cyc(t0 + i * 25 / 60))) for i in range(61)]
    ps = [(P.X(t0 + 25 + i * 25 / 60), P.Y(cyc(t0 + 25 + i * 25 / 60))) for i in range(61)]
    b += line(pe, 'ln', ' stroke-dasharray="6 4"')
    b += line(ps, 'thick')
decay = lambda t: 0.1 * (1 + t) ** -0.55
b += P.curve(decay, n=400, cls='acc')
ly = 24
b += line([(80, ly), (114, ly)], 'ln', ' stroke-dasharray="6 4"')
b += text(120, ly + 4, 'Exploration stage', 'start', 'small')
b += line([(260, ly), (294, ly)], 'thick')
b += text(300, ly + 4, 'Sampling stage', 'start', 'small')
b += line([(420, ly), (454, ly)], 'acc')
b += text(460, ly + 4, 'Decaying step size', 'start', 'small')
svg('Bdl02CyclicalSchedule', 640, 310, 'Cyclical and decaying step-size schedules over 200 epochs',
    'Four cosine cycles of 50 epochs each start at a step size of 0.1 and fall to 0. The first half of each cycle, where the step size is above 0.05, is drawn dashed and labeled exploration stage; the second half is drawn solid and labeled sampling stage. A decaying schedule drops quickly from 0.1 to about 0.02 by epoch 25 and then slowly to about 0.005 by epoch 200.',
    b)

# ---------- Figure 2.2: Entropy-MCMC sampling dynamics ----------
FX, FY, FW, FH = 20, 20, 470, 360
def bdl02_f(u, v):
    sharp = -2.2 * math.exp(-((u - 0.86) ** 2 / (2 * 0.075 ** 2) + (v - 0.04) ** 2 / (2 * 0.05 ** 2)))
    flat = -1.1 * math.exp(-((u - 0.82) ** 2 / (2 * 0.24 ** 2) + (v - 1.0) ** 2 / (2 * 0.22 ** 2)))
    return -0.9 * u + sharp + flat
levels = [-0.25, -0.4, -0.55, -0.7, -0.85, -1.0, -1.15, -1.35, -1.6, -1.9, -2.2, -2.5]
b = '  <defs><clipPath id="bdl02-ent-clip"><rect x="%d" y="%d" width="%d" height="%d" /></clipPath></defs>\n' % (FX, FY, FW, FH)
b += '  <g clip-path="url(#bdl02-ent-clip)">\n'
for d in bdl02_contours(bdl02_f, FX, FY, FW, FH, levels):
    if d:
        b += f'  <path class="mut" d="{d}" />\n'
b += '  </g>\n'
b += f'  <rect class="ln" x="{FX}" y="{FY}" width="{FW}" height="{FH}" />\n'
U = lambda u: FX + u * FW
V = lambda v: FY + FH - v * FH
def bdl02_theta(x, y):
    return f'  <circle class="thick" cx="{x:.1f}" cy="{y:.1f}" r="9" />\n'
def bdl02_aux(x, y):
    return f'  <circle class="thick" cx="{x:.1f}" cy="{y:.1f}" r="9" stroke-dasharray="10 5" />\n'
dash = ' stroke-dasharray="5 4"'
# left particle
t1, a1 = (U(0.13), V(0.23)), (U(0.067), V(0.70))
gf, gc, gu = (U(0.50), V(0.25)), (U(0.11), V(0.385)), (U(0.477), V(0.385))
b += line([a1, gc], 'mut', dash)
b += line([gc, gu], 'mut', dash)
b += line([gu, gf], 'mut', dash)
b += arrow([t1, gf])
b += arrow([t1, gc])
b += arrow([t1, gu])
b += bdl02_theta(*t1)
b += bdl02_aux(*a1)
b += text(gc[0] - 2, gc[1] - 26, '(1/' + var('η') + ')(' + var('θ') + ' − ' + var('θ') + bdl02_sub('a') + ')', 'start')
b += text(gu[0] - 6, gu[1] - 12, '∇' + var('U') + '(' + var('θ') + ')', 'start')
b += text(gu[0] - 6, gu[1] + 24, 'flatness-aware gradient direction', 'start', 'small')
b += text(gf[0] - 20, gf[1] + 30, '∇' + var('f') + '(' + var('θ') + ')', 'start')
b += text(gf[0] - 20, gf[1] + 48, 'original gradient direction', 'start', 'small')
# right particle
t2, a2 = (U(0.75), V(0.50)), (U(0.616), V(0.70))
e1, e2, e3 = (U(0.70), V(0.585)), (U(0.75), V(0.70)), (U(0.795), V(0.66))
b += line([gu, t2], 'mut', dash)
b += line([a2, e1], 'mut', dash)
b += line([e1, e2], 'mut', dash)
b += line([e2, e3], 'mut', dash)
b += arrow([t2, e1])
b += arrow([t2, e2])
b += arrow([t2, e3])
b += bdl02_theta(*t2)
b += bdl02_aux(*a2)
# legend
b += f'  <rect class="box" x="{FX+FW-110}" y="{FY+10}" width="98" height="64" rx="4" />\n'
b += bdl02_theta(FX + FW - 88, FY + 30)
b += text(FX + FW - 66, FY + 35, var('θ'))
b += bdl02_aux(FX + FW - 88, FY + 56)
b += text(FX + FW - 66, FY + 61, var('θ') + bdl02_sub('a'))
svg('Bdl02EntropyMcmc', 510, 400, 'Entropy-MCMC sampling dynamics on an energy landscape',
    'Contour lines show an energy landscape with a sharp, narrow minimum at the bottom right and a wide, flat basin at the top right. On the left, the parameter theta has an original gradient direction, gradient of f, pointing to the right; the coupling term one over eta times theta minus theta a points up toward the auxiliary variable theta a; their sum, the flatness-aware gradient direction, gradient of U, points up and to the right, away from the sharp minimum. A dashed path leads to a second position of theta, where the arrows again point upward toward the flat region and the nearby theta a.',
    b)

# ---------- 03-simulation-based-inference ----------

# ---------- 03-simulation-based-inference (full-text chapter 3) ----------
import numpy as _bdl03_np

def bdl03_sub(t):
    return f'<tspan class="sub" dy="3">{t}</tspan><tspan dy="-3"></tspan>'

def bdl03_ell(cx, cy, rx, ry, rot=0, cls='region', extra=''):
    return (f'  <ellipse class="{cls}" cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}"'
            f' transform="rotate({rot} {cx:.1f} {cy:.1f})"{extra} />\n')

def bdl03_blob(cx, cy, rx, ry, rot=0, levels=3):
    o = ''
    for k in range(levels):
        f = 1 - k / levels
        o += bdl03_ell(cx, cy, rx * f, ry * f, rot)
    return o

def bdl03_curve(x0, y0, cx, cy, x1, y1, cls='ln'):
    return f'  <path class="{cls}" d="M{x0:.1f},{y0:.1f} Q{cx:.1f},{cy:.1f} {x1:.1f},{y1:.1f}" marker-end="ARROW" />\n'

def bdl03_vtext(x, y, t, cls='small'):
    return f'  <text class="{cls}" x="{x:.1f}" y="{y:.1f}" text-anchor="middle" transform="rotate(-90 {x:.1f} {y:.1f})">{t}</text>\n'

def bdl03_dot(x, y, r=1.6, extra=''):
    return f'  <circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="{r}"{extra} />\n'

def bdl03_net(x0, y0, h, cols=2, gap=48, n=4, w=26):
    # columns of rounded units joined by all-to-all connections
    o = ''
    cell = (h - 8) / n
    centers = []
    for c in range(cols):
        x = x0 + c * gap
        o += f'  <rect class="ln" x="{x:.1f}" y="{y0:.1f}" width="{w}" height="{h}" rx="7" />\n'
        cs = []
        for i in range(n):
            yy = y0 + 4 + i * cell
            o += f'  <rect class="box" x="{x+3:.1f}" y="{yy+2:.1f}" width="{w-6}" height="{cell-4:.1f}" rx="5" />\n'
            cs.append((x, x + w, yy + cell / 2))
        centers.append(cs)
    for c in range(cols - 1):
        for a in centers[c]:
            for b_ in centers[c + 1]:
                o += line([(a[1], a[2]), (b_[0], b_[2])], 'mut', ' stroke-width="0.8"')
    return o, centers

# ---- Figure 3.1: Bayesian inference and simulation-based inference ----
rng = _bdl03_np.random.default_rng(3)
b = ''
b += text(8, 22, 'a')
b += text(165, 22, 'Bayesian inference', 'middle')
b += text(62, 52, 'parameter', 'middle', 'small') + text(62, 66, 'space', 'middle', 'small')
b += text(268, 52, 'observation', 'middle', 'small') + text(268, 66, 'space', 'middle', 'small')
b += bdl03_blob(62, 150, 44, 54, -20)
b += bdl03_dot(80, 98, 3)
b += text(88, 96, var('θ'), 'start')
b += bdl03_curve(92, 92, 165, 50, 222, 100)
b += text(165, 62, 'simulation', 'middle', 'small')
b += text(250, 100, var('p') + '(' + var('x') + ' | ' + var('θ') + ')', 'middle', 'small')
for k, cls in ((0, 'mut'), (1, 'ln')):
    pts = []
    for i in range(70):
        x = 212 + i * 1.4
        y = 152 + (14 if k else 10) * math.sin(i * (0.55 + 0.1 * k)) * (0.6 + 0.4 * rng.uniform()) + 6 * rng.normal()
        pts.append((x, y))
    b += line(pts, cls, ' stroke-width="1.1"')
b += text(250, 206, var('x') + bdl03_sub('o'), 'middle', 'small')
b += bdl03_curve(222, 214, 165, 262, 95, 214)
b += text(165, 248, 'inference', 'middle', 'small')
b += text(62, 228, var('p') + '(' + var('θ') + ' | ' + var('x') + bdl03_sub('o') + ')', 'middle', 'small')
# panel b
b += text(330, 22, 'b')
b += text(520, 22, 'Simulation-based inference', 'middle')
heads = [(375, ['prior']), (470, ['simulated', 'data']), (570, ['density', 'estimator']), (662, ['posterior', 'estimate'])]
for x, ls in heads:
    for j, s_ in enumerate(ls):
        b += text(x, 52 + 14 * j, s_, 'middle', 'small')
b += bdl03_blob(375, 150, 34, 34, 0)
b += arrow([(414, 150), (430, 150)])
th = rng.uniform(-1, 1, 160)
for t_ in th:
    px = 470 + 36 * t_ + 2 * rng.normal()
    py = 186 - 62 * t_ ** 2 - abs(8 * rng.normal()) * (0.4 + t_ ** 2)
    b += bdl03_dot(px, py, 1.4)
b += line([(436, 172), (436, 200), (452, 200)], 'mut')
b += text(432, 184, var('x'), 'end', 'small') + text(458, 214, var('θ'), 'start', 'small')
b += arrow([(512, 150), (528, 150)])
nb, _ = bdl03_net(534, 112, 76, cols=2, gap=46, n=4, w=26)
b += nb
b += arrow([(612, 150), (628, 150)])
b += bdl03_blob(662, 132, 15, 22, 25)
b += bdl03_blob(662, 184, 12, 7, 0)
b += text(375, 236, var('θ') + ' ∼ ' + var('p') + '(' + var('θ') + ')', 'middle', 'small')
b += text(470, 236, var('x') + ' ∼ ' + var('p') + '(' + var('x') + ' | ' + var('θ') + ')', 'middle', 'small')
b += text(570, 236, '𝔼[−log ' + var('q') + bdl03_sub('φ') + '(' + var('θ') + ' | ' + var('x') + ')]', 'middle', 'small')
b += text(664, 236, var('q') + bdl03_sub('φ') + '(' + var('θ') + ' | ' + var('x') + bdl03_sub('o') + ')', 'middle', 'small')
svg('Bdl03SbiOverview', 700, 250, 'Bayesian inference and simulation-based inference',
    'Panel a: a shaded posterior region in parameter space on the left and two noisy simulated traces in observation space on the right. A curved arrow labelled simulation goes from a parameter theta to the data distribution p of x given theta, and a curved arrow labelled inference goes back from the observation x o to the posterior p of theta given x o. Panel b: four stages from left to right joined by arrows: a prior drawn as concentric shaded discs, theta drawn from p of theta; a U-shaped cloud of simulated points, x drawn from p of x given theta; a neural network density estimator trained with the expected negative log q phi of theta given x; and a posterior estimate with two shaded blobs, q phi of theta given x o.',
    b)

# ---- Figure 3.2: Bayesian inference as supervised learning (assumed toy simulator) ----
def bdl03_f(t):
    return 16 * (t / 25) * _bdl03_np.exp(1 - t / 25)
def bdl03_sd(t):
    return 0.4 + 0.03 * t
def bdl03_post(xo, ts):
    p = _bdl03_np.exp(-0.5 * ((xo - bdl03_f(ts)) / bdl03_sd(ts)) ** 2) / bdl03_sd(ts)
    return p / p.max()

rng = _bdl03_np.random.default_rng(32)
P = Plot(62, 40, 230, 130, (0, 90), (0, 25))
b = text(177, 22, 'Simulated dataset', 'middle')
b += line([(P.x0, P.y0), (P.x0, P.y0 + P.h), (P.x0 + P.w, P.y0 + P.h)])
for v in (0, 25):
    b += text(P.x0 - 6, P.Y(v) + 4, f'{v}', 'end', 'small')
for v in (0, 90):
    b += text(P.X(v), P.y0 + P.h + 16, f'{v}', 'middle', 'small')
b += bdl03_vtext(P.x0 - 34, P.Y(12.5), var('x'))
xo = 13
for t_ in rng.uniform(0, 90, 320):
    xv = bdl03_f(t_) + bdl03_sd(t_) * rng.normal()
    if 0 <= xv <= 25:
        b += bdl03_dot(P.X(t_), P.Y(xv), 1.5)
b += line([(P.x0, P.Y(xo)), (P.x0 + P.w, P.Y(xo))], 'ln')
b += text(P.x0 + 6, P.Y(xo) - 6, var('x') + bdl03_sub('o'), 'start', 'small')
Q = Plot(62, 215, 230, 55, (0, 90), (0, 1.05))
ts = _bdl03_np.linspace(0, 90, 721)
pp = bdl03_post(xo, ts)
b += line([(Q.X(t_), Q.Y(v)) for t_, v in zip(ts, pp)], 'acc', ' stroke-width="1.6"')
b += line([(Q.x0, Q.y0), (Q.x0, Q.y0 + Q.h), (Q.x0 + Q.w, Q.y0 + Q.h)])
b += text(Q.X(0), Q.y0 + Q.h + 16, '0', 'middle', 'small') + text(Q.X(90), Q.y0 + Q.h + 16, '90', 'middle', 'small')
b += text(Q.X(45), Q.y0 + Q.h + 16, var('θ'), 'middle', 'small')
b += bdl03_vtext(Q.x0 - 34, Q.y0 + Q.h / 2 - 4, 'posterior')
b += bdl03_vtext(Q.x0 - 20, Q.y0 + Q.h / 2 - 4, var('p') + '(' + var('θ') + ' | ' + var('x') + bdl03_sub('o') + ')')
# right: amortized inference
b += text(520, 22, 'Amortized inference with NPE', 'middle')
b += text(616, 52, 'posterior ' + var('q') + bdl03_sub('ψ') + '(' + var('θ') + ' | ' + var('x') + bdl03_sub('o') + ')', 'middle', 'small')
b += f'  <rect class="ln" x="428" y="70" width="104" height="204" rx="14" />\n'
nb, _ = bdl03_net(444, 92, 160, cols=3, gap=26, n=5, w=20)
b += nb
for k, xv in enumerate((13, 15, 16)):
    y = 105 + 70 * k
    b += text(366, y + 4, var('x') + bdl03_sub('o') + ' = ' + str(xv), 'middle', 'small')
    b += arrow([(398, y), (426, y)])
    b += arrow([(534, y), (562, y)])
    R = Plot(568, y - 30, 100, 36, (0, 90), (0, 1.05))
    pk = bdl03_post(xv, ts)
    b += line([(R.X(t_), R.Y(v)) for t_, v in zip(ts, pk)], 'acc', ' stroke-width="1.4"')
    b += line([(R.x0, R.y0 + R.h), (R.x0 + R.w, R.y0 + R.h)])
b += text(568, 266, '0', 'middle', 'small') + text(618, 266, var('θ'), 'middle', 'small') + text(668, 266, '90', 'middle', 'small')
svg('Bdl03NpeSupervised', 690, 290, 'Framing Bayesian inference as a supervised learning problem',
    'Left, top: a scatter of 320 simulated pairs with theta from 0 to 90 on the horizontal axis and x from 0 to 25 on the vertical axis; x rises steeply to a maximum of about 16 near theta equal to 25 and then falls slowly, with a spread that grows with theta. A horizontal line marks the observation x o equal to 13. Left, bottom: the posterior for x o equal to 13, the horizontal cut through the joint distribution, with a narrow peak near theta equal to 10 and a wider peak near theta equal to 50. Right: three observations, x o equal to 13, 15 and 16, enter a single trained neural network, which returns a posterior for each: two separated peaks for 13, two closer peaks for 15 and one broad peak near theta equal to 25 for 16.',
    b)

# ---- Figure 3.3: normalizing flow transforming a Gaussian into a V-shaped target ----
rng = _bdl03_np.random.default_rng(7)
n = 650
def bdl03_panel(x0, pts, title=None):
    o = f'  <rect class="box" x="{x0}" y="46" width="104" height="104" rx="2" />\n'
    for (u, v) in pts:
        if -3 <= u <= 3 and -3 <= v <= 3:
            o += bdl03_dot(x0 + 52 + u * 17, 98 - v * 17, 1.1, ' fill-opacity="0.45"')
    if title:
        o += text(x0 + 52, 34, title, 'middle', 'small')
    return o
z = rng.normal(size=(n, 2))
tgt1 = rng.normal(size=n) * 1.05
target = list(zip(tgt1, 1.25 * _bdl03_np.abs(tgt1) - 1.6 + 0.22 * rng.normal(size=n)))
base = list(zip(0.5 * z[:, 0], 0.5 * z[:, 1]))
y1 = 1.1 * z[:, 0]
t1 = list(zip(y1, -0.45 * y1 + 0.2 * z[:, 1]))
t2 = list(zip(y1, -0.45 * y1 + 0.2 * z[:, 1] + 1.4 * _bdl03_np.maximum(y1, 0) * (0.6 + 0.5 * _bdl03_np.abs(z[:, 1]))))
fin = list(zip(y1, 1.25 * _bdl03_np.abs(y1) - 1.6 + 0.26 * z[:, 1]))
b = bdl03_panel(8, target, 'Target density')
b += bdl03_panel(150, base, var('𝒩') + '(0, 1)')
b += bdl03_panel(292, t1)
b += bdl03_panel(434, t2)
b += bdl03_panel(578, fin, var('q') + bdl03_sub('ψ') + '(' + var('θ') + ')')
b += arrow([(256, 98), (290, 98)]) + text(273, 88, var('T') + bdl03_sub('1'), 'middle', 'small')
b += arrow([(398, 98), (432, 98)]) + text(415, 88, var('T') + bdl03_sub('2'), 'middle', 'small')
b += line([(540, 98), (552, 98)]) + text(558, 102, '…', 'middle', 'small') + arrow([(564, 98), (576, 98)])
svg('Bdl03NormalizingFlow', 690, 160, 'A normalizing flow transforms a Gaussian into a V-shaped density',
    'Five square panels of samples. First, the target density, a V shape with two arms rising from a lowest point in the middle. Then a round standard Gaussian blob labelled N of 0 and 1, which a transformation T1 stretches into a thin tilted bar, which a transformation T2 bends so that one end turns upward, and after further transformations the result, labelled q psi of theta, is a V shape that matches the target.',
    b)

# ---- Figure 3.4: Gaussian, mixture and flow approximations of a two-moons posterior ----
def bdl03_moon(cx, cy, r, a0, a1, jitter=0.0, rng=None):
    pts = []
    for i in range(41):
        a = math.radians(a0 + (a1 - a0) * i / 40)
        rr = r + jitter * (math.sin(0.45 * i) + 0.4 * math.sin(1.3 * i + 1))
        pts.append((cx + rr * math.cos(a), cy - rr * math.sin(a)))
    return line(pts, 'thick', ' stroke-width="6" stroke-linecap="round" stroke-opacity="0.8"')
rng = _bdl03_np.random.default_rng(4)
b = ''
titles = ['Ground truth', 'Gaussian', 'Mixture of Gaussians', 'Normalizing flow']
for k, tt in enumerate(titles):
    x0 = 16 + 158 * k
    b += text(x0 + 70, 22, tt, 'middle', 'small')
    b += line([(x0, 34), (x0, 174), (x0 + 140, 174)])
    if k == 0:
        b += bdl03_moon(x0 + 92, 64, 13, -110, 100)
        b += bdl03_moon(x0 + 40, 136, 13, 70, 280)
    elif k == 1:
        for s_, cls in ((1.0, 'mut'), (0.7, 'ln'), (0.4, 'ln')):
            b += bdl03_ell(x0 + 68, 100, 68 * s_, 24 * s_, -48, cls)
    elif k == 2:
        for cx, cy in ((x0 + 90, 64), (x0 + 42, 138)):
            for s_, cls in ((1.0, 'mut'), (0.62, 'ln'), (0.3, 'ln')):
                b += bdl03_ell(cx, cy, 11 * s_, 8 * s_, -30, cls)
    else:
        b += bdl03_moon(x0 + 92, 64, 13, -105, 95, 0.6)
        b += bdl03_moon(x0 + 40, 136, 13, 75, 275, 0.6)
# shade bar
for j in range(3):
    for _ in range(3 - j):
        b += f'  <rect class="region" x="652" y="{40 + 44 * j}" width="12" height="44" />\n'
b += f'  <rect class="mut" x="652" y="40" width="12" height="132" />\n'
b += bdl03_vtext(680, 106, 'posterior probability')
svg('Bdl03PosteriorFamilies', 690, 186, 'Expressiveness of different generative models for a two-moons posterior',
    'Four panels. Ground truth: two small crescent-shaped regions, one in the upper right opening to the left and one in the lower left opening to the right, with nothing in between. Gaussian: one large tilted ellipse covering both crescents and the empty space between them. Mixture of Gaussians: two small elliptical blobs at the positions of the crescents, without their crescent shape. Normalizing flow: two crescents close to the ground truth. A grey scale bar on the right indicates posterior probability.',
    b)

# ---- Figure 3.5: NPE with an embedding network ----
rng = _bdl03_np.random.default_rng(5)
b = text(118, 24, 'High-dimensional data', 'middle')
b += text(392, 24, 'NPE with embedding network', 'middle')
b += text(618, 24, 'Posterior', 'middle')
b += text(8, 62, 'Time series')
pts = []
for i in range(260):
    x = 110 + i * 0.6
    env = math.exp(-((i - 150) / 55) ** 2)
    pts.append((x, 66 - 22 * env * math.sin(i * 0.9) - 2 * rng.normal() * (0.2 + env)))
b += line(pts, 'ln', ' stroke-width="1"')
b += text(8, 140, 'Images')
for k in range(3):
    x, y = 150 + 10 * k, 110 + 6 * k
    b += f'  <rect class="box" x="{x}" y="{y}" width="44" height="44" />\n'
b += bdl03_ell(192, 154, 9, 13, 15, 'thick')
b += text(8, 222, 'i.i.d. data')
b += text(136, 222, var('θ'), 'middle')
b += arrow([(146, 218), (174, 218)])
b += f'  <rect class="ln" x="176" y="194" width="46" height="46" rx="10" />\n'
b += f'  <circle class="ln" cx="199" cy="215" r="13" />\n'
b += text(199, 220, var('x'), 'middle') + text(217, 238, var('N'), 'end', 'small')
b += arrow([(246, 140), (282, 140)])
b += '  <path class="box" d="M290,46 L330,96 L330,190 L290,240 Z" />\n'
b += f'  <text x="314" y="143" text-anchor="middle" transform="rotate(-90 314 143)">Embedding net</text>\n'
nb, cs = bdl03_net(368, 88, 104, cols=2, gap=50, n=4, w=28)
b += nb
for c in cs[0]:
    for yy in (96, 120, 156, 180):
        b += line([(330, yy), (c[0], c[2])], 'mut', ' stroke-width="0.8"')
b += arrow([(452, 140), (540, 140)])
b += bdl03_blob(618, 104, 46, 34, -30)
b += bdl03_blob(618, 196, 24, 14, -10)
svg('Bdl03EmbeddingNet', 690, 252, 'Neural posterior estimation with an embedding network',
    'Left, three kinds of high-dimensional simulation output: a time series with an oscillating burst, a stack of images of a handwritten digit, and i.i.d. data drawn as a plate with N repeated observations x generated from one parameter theta. An arrow leads to the embedding net, drawn as a trapezoid that narrows the data, connected to the layers of the inference network. An arrow leads on to a posterior with two shaded blobs, a large one and a small one.',
    b)

# ---- Figure 3.6: coverage diagnostics ----
b = text(150, 22, 'Expected coverage (HPD)', 'middle')
b += text(505, 22, 'Marginal simulation-based calibration (SBC)', 'middle')
def bdl03_xo(x, y, k):
    return text(x, y + 4, var('x') + f'<tspan class="sub" dy="3">o</tspan><tspan class="sub" dy="-9">{k}</tspan><tspan dy="6"></tspan>', 'start')
b += bdl03_xo(8, 74, 1) + arrow([(34, 70), (58, 70)])
b += bdl03_blob(80, 70, 10, 24, 15)
b += bdl03_dot(88, 46, 3)
b += text(96, 42, var('θ') + '<tspan class="sub" dy="-6">*,1</tspan><tspan dy="6"></tspan>', 'start', 'small')
b += text(80, 116, var('q') + '(' + var('θ') + ' | ' + var('x') + '<tspan class="sub" dy="3">o</tspan><tspan class="sub" dy="-9">1</tspan><tspan dy="6">)</tspan>', 'middle', 'small')
b += bdl03_xo(8, 170, 2) + arrow([(34, 166), (54, 166)])
b += bdl03_blob(80, 166, 22, 14, 0)
b += bdl03_dot(78, 168, 3)
b += text(80, 198, var('θ') + '<tspan class="sub" dy="-6">*,2</tspan><tspan dy="6"></tspan>', 'middle', 'small')
b += text(80, 222, var('q') + '(' + var('θ') + ' | ' + var('x') + '<tspan class="sub" dy="3">o</tspan><tspan class="sub" dy="-9">2</tspan><tspan dy="6">)</tspan>', 'middle', 'small')
b += arrow([(120, 88), (156, 108)]) + arrow([(120, 158), (156, 140)])
P = Plot(178, 50, 112, 112, (0, 1), (0, 1))
b += line([(P.x0, P.y0), (P.x0, P.y0 + P.h), (P.x0 + P.w, P.y0 + P.h)])
b += line([(P.X(0), P.Y(0)), (P.X(1), P.Y(1))], 'ln', ' stroke-dasharray="5 4"')
b += P.curve(lambda u: u ** 2.4, cls='thick', extra=' stroke-width="2"')
mx, my = P.X(0.5), P.Y(0.5)
b += line([(mx + 4, my + 4), (mx + 22, my + 22)], 'ln', ' marker-start="ARROW" marker-end="ARROW"')
b += bdl03_vtext(P.x0 - 10, P.Y(0.5), 'posterior cov.')
b += text(P.X(0.5), P.y0 + P.h + 16, 'nominal', 'middle', 'small') + text(P.X(0.5), P.y0 + P.h + 30, 'coverage', 'middle', 'small')
# SBC side
def bdl03_marg(x0, y, w, sd, mu, star, cls):
    pts = []
    for i in range(61):
        u = i / 60
        pts.append((x0 + u * w, y - 18 * math.exp(-0.5 * ((u - mu) / sd) ** 2)))
    o = line([(x0 - 10, y)] + pts + [(x0 + w + 4, y)], cls, ' stroke-width="1.6"')
    o += line([(x0 + star * w, y + 2), (x0 + star * w, y - 24)], 'ln', ' stroke-width="1.6"')
    return o
b += bdl03_xo(352, 86, 1) + arrow([(378, 82), (392, 82)])
b += bdl03_marg(408, 72, 40, 0.12, 0.4, 0.55, 'mut') + text(460, 66, var('θ') + bdl03_sub('1'), 'start', 'small')
b += bdl03_marg(408, 104, 40, 0.15, 0.45, 0.62, 'mut') + text(460, 98, var('θ') + bdl03_sub('2'), 'start', 'small')
b += text(436, 42, var('θ') + '<tspan class="sub" dy="-6">*</tspan><tspan dy="6"></tspan>', 'middle', 'small')
b += bdl03_xo(352, 182, 2) + arrow([(378, 178), (392, 178)])
b += bdl03_marg(408, 168, 40, 0.14, 0.55, 0.6, 'mut') + text(460, 162, var('θ') + bdl03_sub('1'), 'start', 'small')
b += bdl03_marg(408, 200, 40, 0.08, 0.5, 0.2, 'mut') + text(460, 194, var('θ') + bdl03_sub('2'), 'start', 'small')
b += line([(408, 232), (424, 232)], 'mut', ' stroke-width="1.6"') + text(430, 236, 'posterior marginals', 'start', 'small')
b += arrow([(480, 92), (506, 112)]) + arrow([(480, 170), (506, 150)])
for k, (title, sub_, f) in enumerate((('Calibrated', '1', lambda u: u + 0.03 * math.sin(9 * u)),
                                      ('Overconfident', '2', lambda u: 0.5 + 0.5 * math.copysign(abs(2 * u - 1) ** 3, 2 * u - 1)))):
    P = Plot(538 + 84 * k, 76, 70, 86, (0, 1), (0, 1))
    b += text(P.X(0.5), 44, title, 'middle', 'small')
    b += text(P.X(0.5), 60, var('θ') + bdl03_sub(sub_), 'middle', 'small')
    b += line([(P.x0, P.y0), (P.x0, P.y0 + P.h), (P.x0 + P.w, P.y0 + P.h)])
    b += line([(P.X(0), P.Y(0)), (P.X(1), P.Y(1))], 'ln', ' stroke-dasharray="5 4"')
    b += P.curve(f, cls='thick', extra=' stroke-width="2"')
    b += text(P.X(0.5), P.y0 + P.h + 16, 'rank ' + var('θ') + bdl03_sub(sub_), 'middle', 'small')
b += bdl03_vtext(528, 119, 'posterior rank')
svg('Bdl03CoverageDiagnostics', 700, 250, 'Coverage diagnostics: expected coverage and marginal simulation-based calibration',
    'Left, expected coverage based on the highest-probability density region: two observations x o 1 and x o 2 each give a posterior q of theta given x o, drawn as a shaded region with the true parameter theta star marked as a dot. Their results feed a plot of posterior coverage against nominal coverage, where the dashed diagonal is the ideal and a solid curve lies below it, with a double arrow marking the gap. Right, marginal simulation-based calibration: for each observation the posterior marginals of theta 1 and theta 2 are drawn as grey curves with the true value as a vertical line. Their ranks feed two plots of posterior rank: for theta 1, labelled calibrated, the curve follows the diagonal; for theta 2, labelled overconfident, the curve is S-shaped, above the diagonal at low ranks and below it at high ranks.',
    b)

# ---------- 04-sequential-monte-carlo-samplers ----------
# ===================== Chapter 4: Sequential Monte Carlo samplers =====================
# Data points are read off the book's figures (log-log plots); the redraws are schematic.

def bdl04_pow(e):
    # "10" with a raised exponent; the exponent uses a real minus sign.
    e = str(e).replace('-', '−')
    return f'10<tspan class="sub" dy="-6">{e}</tspan>'

class Bdl04Log:
    # Plot area with optional log10 axes (lx, ly) given as exponent ranges.
    def __init__(s, x0, y0, w, h, xr, yr, lx=True, ly=True):
        s.x0, s.y0, s.w, s.h, s.xr, s.yr, s.lx, s.ly = x0, y0, w, h, xr, yr, lx, ly
    def X(s, v):
        v = math.log10(v) if s.lx else v
        return s.x0 + (v - s.xr[0]) / (s.xr[1] - s.xr[0]) * s.w
    def Y(s, v):
        v = math.log10(v) if s.ly else v
        return s.y0 + s.h - (v - s.yr[0]) / (s.yr[1] - s.yr[0]) * s.h
    def frame(s):
        return f'  <rect class="ln" x="{s.x0:.1f}" y="{s.y0:.1f}" width="{s.w:.1f}" height="{s.h:.1f}" />\n'

def bdl04_marker(x, y, kind, cls):
    r = 3.6
    if kind == 'circle':
        return f'  <circle class="{cls}" cx="{x:.1f}" cy="{y:.1f}" r="{r}" />\n'
    if kind == 'square':
        return f'  <rect class="{cls}" x="{x-r:.1f}" y="{y-r:.1f}" width="{2*r:.1f}" height="{2*r:.1f}" />\n'
    pts = {
        'up': [(0, -1.2), (1.1, 0.8), (-1.1, 0.8)],
        'down': [(0, 1.2), (1.1, -0.8), (-1.1, -0.8)],
        'left': [(-1.2, 0), (0.8, -1.1), (0.8, 1.1)],
        'right': [(1.2, 0), (-0.8, -1.1), (-0.8, 1.1)],
        'diamond': [(0, -1.3), (1.1, 0), (0, 1.3), (-1.1, 0)],
    }[kind]
    d = ' '.join(('M' if i == 0 else 'L') + f'{x+px*r:.1f},{y+py*r:.1f}' for i, (px, py) in enumerate(pts)) + ' Z'
    return f'  <path class="{cls}" d="{d}" />\n'

def bdl04_series(P, data, cls, dash, kind, mcls):
    pts = [(P.X(a), P.Y(c)) for a, c in data]
    o = line(pts, cls, f' stroke-dasharray="{dash}"' if dash else '')
    if kind:
        for x, y in pts:
            o += bdl04_marker(x, y, kind, mcls)
    return o

def bdl04_ylabel(x, y, t):
    return f'  <text class="small" x="{x:.1f}" y="{y:.1f}" text-anchor="middle" transform="rotate(-90 {x:.1f} {y:.1f})">{t}</text>\n'

# ---------- Figures 4.1 and 4.2: cost against MSE for SMC and MLSMC ----------
def bdl04_cost_panel(x0, xr, yr, smc, ml, inv, label):
    P = Bdl04Log(x0, 34, 236, 210, xr, yr)
    o = ''
    for e in range(int(math.ceil(xr[0])), int(math.floor(xr[1])) + 1):
        o += line([(P.X(10 ** e), P.y0), (P.X(10 ** e), P.y0 + P.h)], 'grid')
        o += text(P.X(10 ** e), P.y0 + P.h + 18, bdl04_pow(e), 'middle', 'small')
    for e in range(int(math.ceil(yr[0])), int(math.floor(yr[1])) + 1):
        o += line([(P.x0, P.Y(10 ** e)), (P.x0 + P.w, P.Y(10 ** e))], 'grid')
        o += text(P.x0 - 6, P.Y(10 ** e) + 4, bdl04_pow(e), 'end', 'small')
    o += P.frame()
    o += text(P.x0 + P.w / 2, P.y0 + P.h + 40, 'MSE', 'middle', 'small')
    o += bdl04_ylabel(P.x0 - 40, P.y0 + P.h / 2, 'Cost')
    o += text(P.x0, P.y0 - 12, label, 'start', 'small')
    # credible sets: thin curves above and below each estimate
    for data, f in ((smc, 1.55), (ml, 1.6)):
        o += line([(P.X(a), P.Y(c * f)) for a, c in data], 'grid')
        o += line([(P.X(a), P.Y(c / f)) for a, c in data], 'grid')
    if inv:
        o += line([(P.X(a), P.Y(1 / a)) for a in inv], 'ln', ' stroke-dasharray="2 3"')
    o += bdl04_series(P, smc, 'mut', '7 4', 'circle', 'box')
    o += bdl04_series(P, ml, 'acc', '', 'circle', 'dot')
    # legend
    lx, ly = P.x0 + P.w - 92, P.y0 + 10
    o += f'  <rect class="box" x="{lx-6:.1f}" y="{ly-8:.1f}" width="92" height="{52 if inv else 36}" />\n'
    o += line([(lx, ly), (lx + 26, ly)], 'mut', ' stroke-dasharray="7 4"') + bdl04_marker(lx + 13, ly, 'circle', 'box')
    o += text(lx + 32, ly + 4, 'SMC', 'start', 'small')
    o += line([(lx, ly + 16), (lx + 26, ly + 16)], 'acc') + bdl04_marker(lx + 13, ly + 16, 'circle', 'dot')
    o += text(lx + 32, ly + 20, 'MLSMC', 'start', 'small')
    if inv:
        o += line([(lx, ly + 32), (lx + 26, ly + 32)], 'ln', ' stroke-dasharray="2 3"')
        o += text(lx + 32, ly + 36, 'MSE<tspan class="sub" dy="-6">−1</tspan>', 'start', 'small')
    return o

b = bdl04_cost_panel(64, (-5, -2), (2, 6),
    [(4e-5, 5.7e5), (8e-5, 1.3e5), (5e-4, 2e4), (1.15e-3, 3.2e3), (8e-3, 2e2)],
    [(4e-5, 3.2e4), (9.5e-5, 1.25e4), (4.3e-4, 6.4e3), (1.1e-3, 2e3), (7.5e-3, 2.5e2)],
    [4.2e-5, 8e-3], 'Left: ' + var('s') + ' = 3')
b += bdl04_cost_panel(388, (math.log10(4.5e-5), -2), (2, 6),
    [(4.5e-5, 4.2e5), (7.2e-5, 1.12e5), (4e-4, 2.8e4), (1.75e-3, 2.7e3), (8e-3, 1.6e2)],
    [(5e-5, 1.15e5), (8e-5, 3.3e4), (3.8e-4, 1.5e4), (1.95e-3, 1.9e3), (7.5e-3, 1.5e2)],
    None, 'Right: ' + var('s') + ' = 1.1')
svg('Bdl04RegressionCost', 640, 300, 'Cost against mean square error for SMC and MLSMC on the TNN regression problem',
    'Two log-log panels, cost from 100 to 1 million against MSE from about 0.00001 to 0.01. '
    'Left, smoothness s equal to 3: the MLSMC curve runs close to the MSE to the power minus 1 reference line, '
    'from a cost of about 250 at an MSE of 0.0075 to about 32,000 at 0.00004, while SMC rises more steeply to about 570,000 at the same MSE, roughly a factor of 10 to 20 above MLSMC. '
    'Right, s equal to 1.1: both methods rise from about 150 at an MSE of 0.008 to between 100,000 and 400,000 at 0.00005, with MLSMC only moderately below SMC. '
    'Thin curves above and below each line mark the credible intervals.',
    b)

b = bdl04_cost_panel(64, (math.log10(3.8e-5), -2), (2, 6.9),
    [(4.5e-5, 1.3e6), (9e-5, 3.2e5), (4e-4, 5.5e4), (1.3e-3, 1.3e4), (9e-3, 8e2)],
    [(4e-5, 9e4), (8.2e-5, 4.1e4), (3.1e-4, 1.7e4), (1.1e-3, 4e3), (8.5e-3, 6e2)],
    [4e-5, 8.5e-3], 'Left: ' + var('s') + ' = 3')
b += bdl04_cost_panel(388, (math.log10(3.8e-5), math.log10(7.5e-3)), (2, 6.9),
    [(4.1e-5, 8e5), (5.8e-5, 2.6e5), (2e-4, 6.8e4), (2.3e-3, 6e3), (6.6e-3, 9.5e2)],
    [(5e-5, 1.8e5), (6.6e-5, 1.05e5), (1.9e-4, 2.4e4), (2.3e-3, 3.1e3), (6.3e-3, 1.05e3)],
    [5e-5, 6.3e-3], 'Right: ' + var('s') + ' = 1.1')
svg('Bdl04MnistCost', 640, 300, 'Cost against mean square error for SMC and MLSMC on binary MNIST classification',
    'Two log-log panels, cost from 100 to about 8 million against MSE from about 0.00004 to 0.01. '
    'Left, s equal to 3: MLSMC rises from about 600 at an MSE of 0.0085 to about 90,000 at 0.00004, roughly parallel to the MSE to the power minus 1 line and well below SMC, which reaches about 1.3 million. '
    'Right, s equal to 1.1: MLSMC rises from about 1,000 at an MSE of 0.006 to about 180,000 at 0.00005, and SMC from about 950 to about 800,000; the gap is smaller than on the left. '
    'Thin curves mark the credible sets.',
    b)

# ---------- Figure 4.3: variance against the number of processors ----------
R = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
MR = [511 * r for r in R]
P = Bdl04Log(78, 46, 380, 300, (math.log10(1500), 6), (-6, 0))
b = ''
for e in (4, 5, 6):
    b += text(P.X(10 ** e), P.y0 + P.h + 18, bdl04_pow(e), 'middle', 'small')
for m in MR:
    b += line([(P.X(m), P.y0), (P.X(m), P.y0 + P.h)], 'grid')
for e in range(-6, 1):
    b += line([(P.x0, P.Y(10 ** e)), (P.x0 + P.w, P.Y(10 ** e))], 'grid')
    b += text(P.x0 - 6, P.Y(10 ** e) + 4, bdl04_pow(e), 'end', 'small')
for r, m in zip(R, MR):
    b += text(P.X(m), P.y0 - 8, str(r), 'middle', 'small')
b += P.frame()
b += text(P.x0 + P.w / 2, P.y0 - 28, 'Number of processors (' + var('R') + ')', 'middle', 'small')
b += text(P.x0 + P.w / 2, P.y0 + P.h + 40, 'Total number of particles (' + var('MR') + ')', 'middle', 'small')
b += bdl04_ylabel(P.x0 - 48, P.y0 + P.h / 2, 'Variance')
series43 = [
    ('MH', [0.17, 0.055, 0.026, 0.0135, 0.0095, 0.005, 0.0018, 0.0011, 0.00052], 'ln', '', 'circle', 'arrowhead'),
    ('MH smMALA', [0.0042, 0.003, 0.0013, 0.00055, 0.00024, 0.00014, 6.8e-5, 4e-5, 1.6e-5], 'mut', '5 3', 'down', 'box'),
    ('RB-MP-MCMC', [0.00095, 0.00048, 0.00027, 0.00011, 6.3e-5, 2.2e-5, 1.6e-5, 6.2e-6, 2.9e-6], 'ln', '8 3 2 3', 'up', 'box'),
    ('ARB-MP-MCMC', [0.0008, 0.00031, 0.000155, 9e-5, 4e-5, 2e-5, 1.3e-5, 4.7e-6, 1.7e-6], 'ln', '1.5 3', 'square', 'arrowhead'),
    ('SMC<tspan class="sub" dy="3">∥</tspan><tspan dy="-3">-PCN</tspan>', [0.0009, 0.00049, 0.00031, 0.00012, 6.2e-5, 2.6e-5, 1.95e-5, 8.8e-6, 3.4e-6], 'acc', '5 3', 'left', 'box'),
    ('PCN<tspan class="sub" dy="3">∥</tspan>', [0.097, 0.072, 0.046, 0.025, 0.0105, 0.0048, 0.0023, 0.0013, 0.0007], 'mut', '8 3 2 3', 'right', 'arrowhead'),
    ('MH<tspan class="sub" dy="3">∥</tspan>', [0.17, 0.118, 0.058, 0.026, 0.013, 0.008, 0.0038, 0.0016, 0.0006], 'mut', '1.5 3', 'circle', 'arrowhead'),
    ('AIS', [0.0079, 0.0025, 0.0018, 0.00105, 0.00046, 0.000135, 7.5e-5, 2.45e-5, 2.2e-5], 'mut', '', 'diamond', 'box'),
]
b += line([(P.X(MR[0]), P.Y(0.031)), (P.X(MR[-1]), P.Y(0.031 * 4 / 1024))], 'ln', ' stroke-dasharray="6 4"')
for name, vals, cls, dash, kind, mcls in series43:
    b += bdl04_series(P, list(zip(MR, vals)), cls, dash, kind, mcls)
lx, ly = 482, 60
b += line([(lx, ly), (lx + 30, ly)], 'ln', ' stroke-dasharray="6 4"')
b += text(lx + 38, ly + 4, var('R') + '<tspan class="sub" dy="-6">−1</tspan>', 'start', 'small')
for i, (name, vals, cls, dash, kind, mcls) in enumerate(series43):
    y = ly + 22 * (i + 1)
    b += line([(lx, y), (lx + 30, y)], cls, f' stroke-dasharray="{dash}"' if dash else '')
    b += bdl04_marker(lx + 15, y, kind, mcls)
    b += text(lx + 38, y + 4, name, 'start', 'small')
svg('Bdl04AustralianCredit', 640, 400, 'Empirical variance of posterior mean estimates against the number of processors on Australian Credit',
    'Log-log plot of variance, from 0.000001 to 1, against the total number of particles MR from about 2,000 to 520,000, with the number of processors R from 4 to 1024 on the top axis and M equal to 511. '
    'All methods decrease roughly in proportion to the reference line R to the power minus 1. '
    'MH, PCN parallel and MH parallel are highest, falling from about 0.1 to 0.17 at R equal to 4 to about 0.0005 to 0.0007 at R equal to 1024. '
    'AIS and MH smMALA lie in the middle, from about 0.004 to 0.008 down to about 0.00002. '
    'SMC parallel pCN, RB-MP-MCMC and ARB-MP-MCMC are lowest and close together, from about 0.0008 to 0.0009 down to about 0.000002 to 0.000003.',
    b)

# ---------- Figure 4.4: IMDb, accuracy and NLL ----------
def bdl04_dual_panel(x0, xs, xticks, xlab, xlog, accr, nllr, acct, nllt, series, title, af, nf):
    P = Bdl04Log(x0, 40, 180, 200, (math.log10(xs[0]), math.log10(xs[1])) if xlog else xs, accr, lx=xlog, ly=False)
    Q = Bdl04Log(x0, 40, 180, 200, P.xr, nllr, lx=xlog, ly=False)
    o = ''
    for v, lab in xticks:
        o += line([(P.X(v), P.y0), (P.X(v), P.y0 + P.h)], 'grid', ' stroke-dasharray="3 3"')
        o += text(P.X(v), P.y0 + P.h + 18, lab, 'middle', 'small')
    for v in acct:
        o += line([(P.x0, P.Y(v)), (P.x0 + P.w, P.Y(v))], 'grid', ' stroke-dasharray="3 3"')
        o += text(P.x0 - 6, P.Y(v) + 4, format(v, af), 'end', 'small')
    for v in nllt:
        o += text(P.x0 + P.w + 6, Q.Y(v) + 4, format(v, nf), 'start', 'small')
    o += P.frame()
    o += text(P.x0 + P.w / 2, P.y0 + P.h + 38, xlab, 'middle', 'small')
    o += text(P.x0 + P.w / 2, P.y0 - 14, title, 'middle', 'small')
    o += bdl04_ylabel(P.x0 - 50, P.y0 + P.h / 2, 'Accuracy (%)')
    o += bdl04_ylabel(P.x0 + P.w + 64, P.y0 + P.h / 2, 'NLL')
    for xsv, acc, nll, cls, kind, mcls in series:
        if acc:
            o += bdl04_series(P, list(zip(xsv, acc)), cls, '', kind, mcls)
        if nll:
            o += bdl04_series(Q, list(zip(xsv, nll)), cls, '6 4', kind, mcls)
    return o

Rs = [1, 2, 4, 8]
b = bdl04_dual_panel(62, (0, 3), [(0, '2<tspan class="sub" dy="-6">0</tspan>'), (1, '2<tspan class="sub" dy="-6">1</tspan>'), (2, '2<tspan class="sub" dy="-6">2</tspan>'), (3, '2<tspan class="sub" dy="-6">3</tspan>')],
    var('R') + ' (processors)', False, (88.594, 88.728), (0.28455, 0.28566), [88.60, 88.62, 88.64, 88.66, 88.68, 88.70, 88.72], [0.2846, 0.2850, 0.2854],
    [([0, 1, 2, 3], [88.60, 88.67, 88.71, 88.72], [0.2856, 0.2852, 0.2849, 0.2846], 'acc', 'circle', 'dot'),
     ([0, 1, 2], [88.68, 88.69, 88.69], [0.2854, 0.2854, 0.2854], 'mut', 'square', 'box'),
     ([0, 1, 2], [88.70, 88.71, 88.70], [0.2854, 0.2853, 0.2854], 'ln', 'up', 'arrowhead')],
    'Accuracy and NLL against ' + var('R') + ' (budget ≈ τ<tspan class="sub" dy="3">irr</tspan><tspan dy="-3">)</tspan>', '.2f', '.4f')
ep = [40, 700, 1e4]
b += bdl04_dual_panel(392, (25, 1.4e4), [(100, bdl04_pow(2)), (1000, bdl04_pow(3)), (1e4, bdl04_pow(4))],
    'Wall-clock time (epochs)', True, (82.52, 89.08), (0.264, 0.655), [83, 84, 85, 86, 87, 88, 89], [0.3, 0.4, 0.5, 0.6],
    [(ep, [82.95, 87.25, 88.72], [0.607, 0.318, 0.284], 'acc', 'circle', 'dot'),
     (ep, [82.78, 87.12, 88.70], [0.633, 0.322, 0.283], 'mut', 'square', 'box'),
     (ep, [88.30, 88.68, 88.72], [0.293, 0.286, 0.284], 'ln', 'up', 'arrowhead')],
    'Accuracy and NLL against budget, ' + var('R') + ' = 8', '.0f', '.1f')
# shared legend under the panels
ly = 316
items = [('acc', 'circle', 'dot', 'SMC<tspan class="sub" dy="3">∥</tspan><tspan dy="-3"> (</tspan>' + var('R') + ' = 8 on the right)'),
         ('mut', 'square', 'box', 'HMC<tspan class="sub" dy="3">∥</tspan><tspan dy="-3"> (</tspan>' + var('R') + ' = 8 on the right)'),
         ('ln', 'up', 'arrowhead', 'HMC (' + var('R') + ' = 4 on the right)')]
for i, (cls, kind, mcls, lab) in enumerate(items):
    x = 40 + 200 * i
    b += line([(x, ly), (x + 28, ly)], cls) + bdl04_marker(x + 14, ly, kind, mcls)
    b += text(x + 34, ly + 4, lab, 'start', 'small')
b += line([(150, ly + 24), (178, ly + 24)], 'ln')
b += text(184, ly + 28, 'accuracy (left axis)', 'start', 'small')
b += line([(350, ly + 24), (378, ly + 24)], 'ln', ' stroke-dasharray="6 4"')
b += text(384, ly + 28, 'NLL (right axis)', 'start', 'small')
svg('Bdl04ImdbParallel', 640, 356, 'Test accuracy and negative log-likelihood of parallel SMC and HMC on IMDb',
    'Left panel, at a budget of about 10,000 epochs, against R from 1 to 8 on a log scale: SMC parallel accuracy rises from 88.60 to 88.72 percent and its NLL falls from 0.2856 to 0.2846, '
    'while HMC parallel and serial HMC stay near 88.68 to 88.71 percent accuracy and an NLL of about 0.2854. '
    'Right panel, R equal to 8, against a wall-clock budget of 40, 700 and 10,000 epochs on a log scale: SMC parallel and HMC parallel collapse to about 83 percent accuracy with an NLL above 0.6 at 40 epochs, '
    'reach about 87 percent and an NLL of 0.32 at 700 epochs, and converge to 88.7 percent and 0.28 at 10,000 epochs, where serial HMC, which stays near 88.3 to 88.7 percent throughout, also ends.',
    b)

# ---------- 05-low-precision-sampling ----------
# ---------- Bdl05: Figure 5.1, low-precision SGLD histograms ----------
# Histogram densities (bin width 0.25) from a simulation of the setup described in the text:
# standard Gaussian target, 8-bit fixed point with 3 fractional bits, stochastic rounding,
# 4000 chains of 12/alpha steps, samples from the second half of each run.
BDL05_HIST = {'naive-0.001': (-6.5625, [0.0001, 0.0, 0.0002, 0.0002, 0.0005, 0.0006, 0.001, 0.0016, 0.0034, 0.0053, 0.0071, 0.0143, 0.0196, 0.0285, 0.0394, 0.052, 0.0727, 0.0919, 0.1119, 0.1413, 0.1728, 0.1935, 0.2245, 0.2389, 0.2478, 0.268, 0.2635, 0.2635, 0.2518, 0.2265, 0.1983, 0.1779, 0.1495, 0.1303, 0.1018, 0.0824, 0.0646, 0.0434, 0.0338, 0.0265, 0.0174, 0.0106, 0.0085, 0.0048, 0.0037, 0.0018, 0.0006, 0.0007, 0.0002, 0.0004, 0.0001, 0.0001, 0.0001]), 'vc-0.001': (-4.8125, [0.0001, 0.0, 0.0001, 0.0002, 0.0003, 0.0014, 0.0016, 0.005, 0.0096, 0.0169, 0.0393, 0.0613, 0.095, 0.142, 0.1961, 0.2508, 0.3111, 0.3632, 0.3875, 0.4015, 0.3783, 0.3391, 0.2887, 0.2313, 0.1701, 0.1213, 0.0789, 0.0512, 0.0296, 0.0155, 0.0074, 0.0033, 0.0024, 0.0002]), 'f-0.001': (-4.5625, [0.0001, 0.0001, 0.0002, 0.0004, 0.0008, 0.0023, 0.0059, 0.0106, 0.0215, 0.0366, 0.0602, 0.0971, 0.141, 0.1936, 0.2643, 0.3195, 0.3645, 0.4011, 0.3964, 0.3685, 0.3322, 0.2785, 0.2279, 0.1731, 0.1185, 0.0768, 0.0451, 0.0311, 0.0165, 0.009, 0.0038, 0.0015, 0.0008, 0.0005, 0.0001]), 'naive-0.0001': (-8.0625, [0.0022, 0.0021, 0.0029, 0.0049, 0.0055, 0.0065, 0.008, 0.0099, 0.0121, 0.0155, 0.0173, 0.0212, 0.0258, 0.0314, 0.0366, 0.0415, 0.0462, 0.0565, 0.063, 0.0728, 0.0767, 0.0875, 0.0991, 0.1113, 0.1167, 0.1201, 0.1268, 0.1336, 0.144, 0.1456, 0.1529, 0.1525, 0.1508, 0.1525, 0.1439, 0.15, 0.1314, 0.1394, 0.1229, 0.1208, 0.1105, 0.1034, 0.0907, 0.0869, 0.0788, 0.07, 0.0581, 0.053, 0.0528, 0.0407, 0.0348, 0.0271, 0.0246, 0.0205, 0.0163, 0.0145, 0.0114, 0.0075, 0.0066, 0.0064, 0.0048, 0.0041, 0.0022, 0.0023, 0.0016]), 'vc-0.0001': (-4.0625, [0.0002, 0.0002, 0.0012, 0.0033, 0.0048, 0.0111, 0.0214, 0.0361, 0.062, 0.0975, 0.1455, 0.2005, 0.2511, 0.3136, 0.3631, 0.3932, 0.3979, 0.3664, 0.3338, 0.2918, 0.2269, 0.1718, 0.1189, 0.0779, 0.0514, 0.0279, 0.0155, 0.0097, 0.0029, 0.0019, 0.0004, 0.0002]), 'f-0.0001': (-4.0625, [0.0002, 0.001, 0.0014, 0.0033, 0.0073, 0.0103, 0.021, 0.0382, 0.0576, 0.0963, 0.1378, 0.2008, 0.2567, 0.3237, 0.3659, 0.3921, 0.3998, 0.3819, 0.3357, 0.2834, 0.2227, 0.1645, 0.1194, 0.0755, 0.0476, 0.0281, 0.0135, 0.0071, 0.0039, 0.0019, 0.0006, 0.0006, 0.0001, 0.0001])}
def bdl05_panel(ox, oy, key, label, xr, xticks):
    P = Plot(ox, oy, 150, 118, xr, (0, 0.42))
    o = P.axes(xticks, [0, 0.1, 0.2, 0.3, 0.4], '', '')
    o += f'  <text class="small" x="{ox-34}" y="{oy+59}" text-anchor="middle" transform="rotate(-90 {ox-34} {oy+59})">Density</text>\n'
    x0, dens = BDL05_HIST[key]
    w = 0.25
    d = ''
    for i, v in enumerate(dens):
        a, b = x0 + i*w, x0 + (i+1)*w
        if b <= xr[0] or a >= xr[1] or v <= 0:
            continue
        a, b = max(a, xr[0]), min(b, xr[1])
        d += f'M{P.X(a):.1f},{P.Y(0):.1f} V{P.Y(min(v, 0.42)):.1f} H{P.X(b):.1f} V{P.Y(0):.1f} Z '
    o += f'  <path class="band" d="{d.strip()}" />\n'
    o += f'  <path class="mut" d="{d.strip()}" stroke-width="0.6" />\n'
    o += P.curve(lambda t: math.exp(-t*t/2)/math.sqrt(2*math.pi), n=160)
    lx = ox + 8
    o += line([(lx, oy-30), (lx+14, oy-30)], 'acc')
    o += text(lx+20, oy-26, 'True', 'start', 'small')
    o += f'  <rect class="band" x="{lx}" y="{oy-17}" width="14" height="9" />\n'
    o += f'  <rect class="mut" x="{lx}" y="{oy-17}" width="14" height="9" />\n'
    o += text(lx+20, oy-9, label, 'start', 'small')
    return o

b = ''
for row, (alpha, akey, cap) in enumerate(((0.001, '0.001', '(a) Low-precision SGLD with ' + var('α') + ' = 0.001'),
                                          (0.0001, '0.0001', '(b) Low-precision SGLD with ' + var('α') + ' = 0.0001'))):
    oy = 44 + row*218
    for col, (kind, lab) in enumerate((('naive', 'Naive SGLDLP-L'), ('vc', 'VC SGLDLP-L'), ('f', 'SGLDLP-F'))):
        ox = 62 + col*205
        if kind == 'naive' and row == 1:
            xr, xt = (-7.5, 7.5), [-6, -4, -2, 0, 2, 4, 6]
        else:
            xr, xt = (-5.5, 5.5), [-4, -2, 0, 2, 4]
        b += bdl05_panel(ox, oy, f'{kind}-{akey}', lab, xr, xt)
    b += text(330, oy + 118 + 40, cap, 'middle')
svg('Bdl05LowPrecisionSgld', 660, 440, 'Histograms of low-precision SGLD samples on a standard Gaussian for two stepsizes',
    'Six panels in two rows. Each panel shows a histogram of samples against the standard Gaussian density, drawn as a line. Top row, stepsize 0.001: naive SGLD with low-precision gradient accumulators gives a histogram that is too wide, with a peak of about 0.27 instead of 0.40, while the variance-corrected version and SGLD with full-precision gradient accumulators match the Gaussian. Bottom row, stepsize 0.0001: the naive histogram is wider still, spreading from about minus 7 to 7 with a peak of about 0.15, while the other two still match the Gaussian.',
    b)

# ---------- 06-discrete-sampling ----------

# ===================== Chapter 6: Discrete sampling =====================

def bdl06_contours(f, x0, y0, x1, y1, levels, step=4.0):
    # Marching squares on f(px, py) over the pixel rectangle; returns one path string per level.
    nx = int((x1 - x0) / step); ny = int((y1 - y0) / step)
    xs = [x0 + i * (x1 - x0) / nx for i in range(nx + 1)]
    ys = [y0 + j * (y1 - y0) / ny for j in range(ny + 1)]
    grid = [[f(x, y) for x in xs] for y in ys]
    out = []
    for lev in levels:
        segs = []
        for j in range(ny):
            for i in range(nx):
                c = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
                vals = [grid[b][a] for a, b in c]
                pts = []
                for k in range(4):
                    (a1, b1), (a2, b2) = c[k], c[(k + 1) % 4]
                    v1, v2 = vals[k], vals[(k + 1) % 4]
                    if (v1 < lev) != (v2 < lev):
                        t = (lev - v1) / (v2 - v1)
                        pts.append((xs[a1] + t * (xs[a2] - xs[a1]), ys[b1] + t * (ys[b2] - ys[b1])))
                if len(pts) == 2:
                    segs.append(pts)
                elif len(pts) == 4:
                    segs.append(pts[:2]); segs.append(pts[2:])
        out.append(' '.join(f'M{p[0][0]:.1f},{p[0][1]:.1f} L{p[1][0]:.1f},{p[1][1]:.1f}' for p in segs))
    return out

def bdl06_sub(t, cls='sub'):
    return f'<tspan class="{cls}" dy="4">{t}</tspan><tspan dy="-4"> </tspan>'

def bdl06_hatch(x, y, s, gap=6):
    o = ''
    for c in range(gap, 2 * s, gap):
        p0 = (x + max(0, c - s), y + min(c, s))
        p1 = (x + min(c, s), y + max(0, c - s))
        o += line([p0, p1], 'mut')
    return o

def bdl06_bits(x, y, bits, hatched=(), s=26, h=32):
    o = ''
    for k, v in enumerate(bits):
        cx = x + k * s
        if k in hatched:
            o += f'  <rect class="region" x="{cx}" y="{y}" width="{s}" height="{h}" />\n'
            o += bdl06_hatch(cx, y + (h - s) / 2, s)
        o += f'  <rect class="ln" x="{cx}" y="{y}" width="{s}" height="{h}" />\n'
        o += text(cx + s / 2, y + h / 2 + 5, str(v), 'middle')
    return o

def bdl06_star(cx, cy, r=9):
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = r if k % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return '  <path class="dot" d="' + ' '.join(('M' if i == 0 else 'L') + f'{x:.1f},{y:.1f}' for i, (x, y) in enumerate(pts)) + ' Z" />\n'

# ---------- Figure 6.1: gradient-informed proposal on a discrete grid ----------
G0, GS = 60, 86   # grid origin (index 0) and spacing in pixels
gx = lambda i: G0 + i * GS
def bdl06_landscape(px, py):
    i = (px - G0) / GS; j = (py - G0) / GS
    du, dv = i - 3.4, j - 1.3
    a, bq = 0.94 * du + 0.34 * dv, -0.34 * du + 0.94 * dv
    main = math.exp(-(a * a / (2 * 1.05 ** 2) + bq * bq / (2 * 0.72 ** 2)))
    side = 0.62 * math.exp(-((i - 0.75) ** 2 / (2 * 0.5 ** 2) + (j - 2.95) ** 2 / (2 * 0.6 ** 2)))
    bridge = 0.35 * math.exp(-((i - 1.9) ** 2 / (2 * 0.9 ** 2) + (j - 2.6) ** 2 / (2 * 0.45 ** 2)))
    return main + side + bridge
X0, Y0, X1, Y1 = 14, 14, 466, 466
b = '  <defs><clipPath id="bdl06-gwg-clip"><rect x="%d" y="%d" width="%d" height="%d" /></clipPath></defs>\n' % (X0, Y0, X1 - X0, Y1 - Y0)
b += '  <g clip-path="url(#bdl06-gwg-clip)">\n'
solid = [0.3, 0.42, 0.54, 0.66, 0.78, 0.9]
dashed = [0.05, 0.11, 0.19]
for d in bdl06_contours(bdl06_landscape, X0, Y0, X1, Y1, solid):
    b += f'  <path class="mut" d="{d}" />\n'
for d in bdl06_contours(bdl06_landscape, X0, Y0, X1, Y1, dashed):
    b += f'  <path class="mut" d="{d}" stroke-dasharray="5 4" />\n'
b += '  </g>\n'
cur = (2, 2)
nbrs = [(1, 2), (3, 2), (2, 3), (2, 1)]
for i in range(5):
    for j in range(5):
        if (i, j) == cur or (i, j) in nbrs:
            continue
        b += f'  <circle class="box" cx="{gx(i)}" cy="{gx(j)}" r="4" />\n'
cx, cy = gx(2), gx(2)
# proposal arrows: thickness indicates proposal weight
b += arrow([(cx - 12, cy), (gx(1) + 14, cy)], 'mut')
b += arrow([(cx, cy + 12), (cx, gx(3) - 14)], 'mut')
b += line([(cx + 12, cy), (gx(3) - 16, cy)], 'thick', ' stroke-dasharray="8 5"')
b += arrow([(gx(3) - 18, cy), (gx(3) - 14, cy)], 'thick')
b += line([(cx, cy - 12), (cx, gx(1) + 18)], 'thick', ' stroke-dasharray="8 5"')
b += arrow([(cx, gx(1) + 20), (cx, gx(1) + 14)], 'thick')
for (i, j) in nbrs[:3]:
    b += f'  <circle class="box" cx="{gx(i)}" cy="{gx(j)}" r="8" />\n'
b += f'  <circle class="box" cx="{gx(2)}" cy="{gx(1)}" r="8" />\n'
b += bdl06_star(gx(2), gx(1))
b += arrow([(cx + 4, cy - 4), (cx + 70, cy - 76)], 'thick')
b += f'  <rect class="box" x="{cx - 10}" y="{cy - 10}" width="20" height="20" />\n'
b += text(cx - 16, cy + 36, var('x'), 'end')
b += text(gx(2) + 18, gx(1) - 18, var('x') + '′', 'start')
b += text(cx + 74, cy - 70, '∇' + var('U') + '(' + var('x') + ')', 'start')
b += text(gx(1) - 26, gx(0) + 52, var('H') + '(' + var('x') + ')', 'start')
svg('Bdl06GradientInformed', 480, 480, 'Gradient-informed proposal over the Hamming-one neighborhood of a discrete state',
    'A five by five grid of discrete states lies over the contour lines of a smooth function with a large mode at the upper right and a smaller mode at the lower left. The current state x, drawn as a square in the middle, has four neighbors that differ in one coordinate, forming H(x). The gradient of U at x points up and to the right, toward the large mode. Proposal arrows from x to its neighbors are thick toward the right and upper neighbors and thin toward the left and lower ones. The upper neighbor, marked with a star, is the proposed state x prime.',
    b)

# ---------- Figure 6.2: Gibbs-With-Gradient versus Discrete Langevin Proposal ----------
b = ''
def bdl06_row(y, title, xp_bits, hatched, mid, mid_label):
    o = text(14, y - 44, title, 'start')
    o += text(26, y - 10, var('x'), 'start')
    o += bdl06_bits(20, y, [0, 1, 0, 1, 0, 0])
    o += mid
    o += text(250, y - 22, mid_label, 'middle')
    o += text(346, y - 10, var('x') + '′', 'start')
    o += bdl06_bits(340, y, xp_bits, hatched)
    o += arrow([(498, y + 16), (522, y + 16)])
    o += f'  <rect class="box" x="524" y="{y - 6}" width="104" height="44" rx="6" />\n'
    o += text(576, y + 12, 'Metropolis–', 'middle', 'small')
    o += text(576, y + 28, 'Hastings', 'middle', 'small')
    return o
y1 = 70
sel = ''
for k in range(6):
    yy = y1 - 2 + k * 7.2
    if k == 3:
        sel += line([(196, yy), (226, yy)], 'thick')
        sel += f'  <circle class="dot" cx="229" cy="{yy:.1f}" r="3.5" />\n'
        sel += arrow([(240, yy), (334, yy)])
    else:
        sel += line([(196, yy), (214, yy)], 'ln')
        sel += f'  <circle class="box" cx="217" cy="{yy:.1f}" r="2.6" />\n'
b += bdl06_row(y1, 'Gibbs-With-Gradient', [0, 1, 1, 1, 0, 0], (2,), sel, var('q') + '(' + var('i') + ' | ' + var('x') + ')')
b += line([(14, 132), (626, 132)], 'grid')
y2 = 196
bars = arrow([(178, y2 + 16), (190, y2 + 16)])
probs = [0.3, 0.85, 0.35, 0.8, 0.45, 0.25]
for k, p in enumerate(probs):
    bx = 194 + k * 18
    hh = 40
    fill = hh * p
    bars += f'  <rect class="dot" x="{bx}" y="{y2 - 4 + hh - fill:.1f}" width="12" height="{fill:.1f}" />\n'
    bars += f'  <rect class="ln" x="{bx}" y="{y2 - 4}" width="12" height="{hh}" />\n'
bars += arrow([(306, y2 + 16), (334, y2 + 16)])
b += bdl06_row(y2, 'Discrete Langevin Proposal', [1, 1, 0, 0, 1, 0], (0, 3, 4), bars,
               '&#123;' + var('q') + bdl06_sub(var('i')) + '&#125;' + '<tspan class="sub" dy="-10">' + var('d') + '</tspan><tspan class="sub" dy="14">' + var('i') + '=1</tspan>')
b += arrow([(178, y1 + 16), (190, y1 + 16)])
svg('Bdl06GwgVsDlp', 640, 250, 'Gibbs-With-Gradient compared with the Discrete Langevin Proposal',
    'Top row: Gibbs-With-Gradient takes the binary state x equal to 0 1 0 1 0 0, selects one coordinate with the distribution q of i given x, and proposes x prime equal to 0 1 1 1 0 0, in which only the third bit, shaded, has changed; x prime then goes to a Metropolis-Hastings step. Bottom row: the Discrete Langevin Proposal builds one distribution q i per coordinate, drawn as six bars, and proposes x prime equal to 1 1 0 0 1 0, in which the first, fourth and fifth bits, shaded, have changed in parallel; x prime then goes to a Metropolis-Hastings step.',
    b)

# ---------- Figure 6.3: proposal scale, balancing and cyclical scheduling ----------
b = ''
def bdl06_marker(kind, x, y, filled=False):
    cls = 'dot' if filled else 'box'
    r = 5.5 if filled else 3.6
    if kind == 'o':
        return f'  <circle class="{cls}" cx="{x:.1f}" cy="{y:.1f}" r="{r}" />\n'
    if kind == 's':
        return f'  <rect class="{cls}" x="{x - r:.1f}" y="{y - r:.1f}" width="{2 * r:.1f}" height="{2 * r:.1f}" />\n'
    return f'  <path class="{cls}" d="M{x:.1f},{y - r * 1.15:.1f} L{x + r:.1f},{y + r * 0.75:.1f} L{x - r:.1f},{y + r * 0.75:.1f} Z" />\n'
def bdl06_frame(P, xt, yt, xl=None, yl=None):
    o = ''
    for v, lab in yt:
        o += line([(P.x0 - 4, P.Y(v)), (P.x0, P.Y(v))])
        o += text(P.x0 - 7, P.Y(v) + 4, lab, 'end', 'small')
    for v, lab in xt:
        o += line([(P.X(v), P.y0 + P.h), (P.X(v), P.y0 + P.h + 4)])
        if lab:
            o += text(P.X(v), P.y0 + P.h + 17, lab, 'middle', 'small')
    o += line([(P.x0, P.y0), (P.x0, P.y0 + P.h), (P.x0 + P.w, P.y0 + P.h)])
    return o
# panel (a)
PA = Plot(56, 48, 236, 222, (0.5, 1.0), (0, 1.08))
b += text(10, 24, '(a)', 'start')
b += bdl06_frame(PA, [(0.5, '0.5'), (0.6, '0.6'), (0.7, '0.7'), (0.8, '0.8'), (0.9, '0.9'), (1.0, '1.0')], [(0, '0'), (1, '1')])
b += text(PA.x0 + PA.w / 2, PA.y0 + PA.h + 38, var('β'), 'middle')
b += f'  <text class="small" x="18" y="{PA.y0 + PA.h / 2:.1f}" text-anchor="middle" transform="rotate(-90 18 {PA.y0 + PA.h / 2:.1f})">Normalized illustrative efficiency</text>\n'
curves = [(0.52, 0.11, '', 'o', 'σ = 0.1'), (0.70, 0.12, ' stroke-dasharray="9 5"', 's', 'σ = 1'), (0.94, 0.125, ' stroke-dasharray="2 4"', 't', 'σ = 2')]
for mu, sd, dash, mk, lab in curves:
    f = lambda x, mu=mu, sd=sd: math.exp(-(x - mu) ** 2 / (2 * sd * sd))
    b += PA.curve(f, n=200, cls='ln', extra=dash)
    for k in range(8):
        xv = 0.5 + k * 0.5 / 7
        b += bdl06_marker(mk, PA.X(xv), PA.Y(f(xv)))
    b += bdl06_marker(mk, PA.X(mu), PA.Y(1), True)
lx = 100
for mu, sd, dash, mk, lab in curves:
    b += line([(lx, 22), (lx + 30, 22)], 'ln', dash)
    b += bdl06_marker(mk, lx + 15, 22)
    b += text(lx + 36, 26, var('σ') + lab[1:], 'start', 'small')
    lx += 80
# panel (b)
b += text(340, 24, '(b)', 'start')
PS = Plot(404, 40, 220, 100, (0, 39), (0.1, 2.0))
PB = Plot(404, 168, 220, 100, (0, 39), (0.5, 1.0))
sig = lambda k: 0.1 + 0.95 * (math.cos(math.pi * (k % 20) / 20) + 1)
bet = lambda k: 0.5 + 0.25 * (math.cos(math.pi * (k % 20) / 20) + 1)
xt = [(0, '0'), (10, '10'), (20, '20'), (30, '30'), (39, '39')]
b += bdl06_frame(PS, [(v, None) for v, _ in xt], [(0.1, '0.1'), (1.0, '1.0'), (2.0, '2.0')])
b += bdl06_frame(PB, xt, [(0.5, '0.50'), (0.75, '0.75'), (1.0, '1.00')])
for Pp, fn, dash, mk in ((PS, sig, '', 'o'), (PB, bet, ' stroke-dasharray="7 4"', 's')):
    for c0 in (0, 20):
        pts = [(Pp.X(c0 + i * 19 / 120), Pp.Y(fn(c0 + i * 19 / 120))) for i in range(121)]
        b += line(pts, 'ln', dash)
    b += line([(Pp.X(19), Pp.Y(fn(19))), (Pp.X(20), Pp.Y(fn(20)))], 'ln', dash)
    for k in range(0, 40, 4):
        b += bdl06_marker(mk, Pp.X(k), Pp.Y(fn(k)))
    b += line([(Pp.X(19.5), Pp.y0), (Pp.X(19.5), Pp.y0 + Pp.h)], 'mut', ' stroke-dasharray="2 3"')
b += f'  <text x="356" y="{PS.y0 + PS.h / 2 + 4:.1f}" text-anchor="middle">{var("σ")}{bdl06_sub(var("k"))}</text>\n'
b += f'  <text x="356" y="{PB.y0 + PB.h / 2 + 4:.1f}" text-anchor="middle">{var("β")}{bdl06_sub(var("k"))}</text>\n'
b += text(PB.x0 + PB.w / 2, PB.y0 + PB.h + 38, 'Sampling iteration ' + var('k'), 'middle', 'small')
svg('Bdl06ScaleSchedules', 640, 320, 'Balancing exponent against proposal scale, and coupled cyclical schedules',
    'Panel a: three bell-shaped curves of normalized illustrative efficiency against the balancing exponent beta from 0.5 to 1. The curve for sigma equal to 0.1 peaks near beta equal to 0.52, the curve for sigma equal to 1 near 0.7, and the curve for sigma equal to 2 near 0.94. Panel b: over 40 sampling iterations in two cycles of 20, the step size sigma k falls along a cosine from 2.0 to about 0.1 and jumps back to 2.0 at iteration 20, while the balancing exponent beta k falls in the same way from 1.00 to about 0.50.',
    b)


# ---------- Bdl07: Figure 7.1, Laplace approximation on a two-parameter perceptron ----------
def bdl07_energy(t1, t2):
    # Energy of a two-parameter model f(x, theta) = theta2 * tanh(theta1 * x + 1),
    # inputs X = (1, -1), targets (1, -1), square loss, regularizer 0.2 * ||theta||^2.
    f1 = t2 * math.tanh(t1 + 1)
    f2 = t2 * math.tanh(-t1 + 1)
    return (f1 - 1) ** 2 + (f2 + 1) ** 2 + 0.2 * (t1 * t1 + t2 * t2)

def bdl07_contours(F, xr, yr, n, levels):
    xs = [xr[0] + i * (xr[1] - xr[0]) / n for i in range(n + 1)]
    ys = [yr[0] + j * (yr[1] - yr[0]) / n for j in range(n + 1)]
    Z = [[F(x, y) for x in xs] for y in ys]
    out = {}
    for lev in levels:
        segs = []
        for j in range(n):
            for i in range(n):
                c = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
                v = [Z[b][a] - lev for a, b in c]
                pts = []
                for k in range(4):
                    a, b = k, (k + 1) % 4
                    if (v[a] < 0) != (v[b] < 0):
                        tt = v[a] / (v[a] - v[b])
                        (ia, ja), (ib, jb) = c[a], c[b]
                        key = tuple(sorted([(ia, ja), (ib, jb)]))
                        x = xs[ia] + tt * (xs[ib] - xs[ia])
                        y = ys[ja] + tt * (ys[jb] - ys[ja])
                        pts.append((key, (x, y)))
                if len(pts) == 2:
                    segs.append((pts[0], pts[1]))
                elif len(pts) == 4:
                    segs.append((pts[0], pts[1]))
                    segs.append((pts[2], pts[3]))
        # chain segments into polylines
        adj = {}
        for s_ in segs:
            for p_ in s_:
                adj.setdefault(p_[0], []).append(s_)
        used = set()
        lines = []
        for s_ in segs:
            if id(s_) in used:
                continue
            used.add(id(s_))
            chain = [s_[0], s_[1]]
            for direction in (0, 1):
                while True:
                    end = chain[-1] if direction == 0 else chain[0]
                    nxt = None
                    for cand in adj.get(end[0], []):
                        if id(cand) not in used:
                            nxt = cand
                            break
                    if nxt is None:
                        break
                    used.add(id(nxt))
                    other = nxt[1] if nxt[0][0] == end[0] else nxt[0]
                    if direction == 0:
                        chain.append(other)
                    else:
                        chain.insert(0, other)
            lines.append([p_[1] for p_ in chain])
        out[lev] = lines
    return out

P = Plot(60, 20, 480, 300, (-3, 3), (-3, 3))
b = '  <defs><clipPath id="bdl07-lap-clip"><rect x="60" y="20" width="480" height="300" /></clipPath></defs>\n'
b += '  <g clip-path="url(#bdl07-lap-clip)">\n'
levels = [0.9, 1.1, 1.2, 1.5, 2, 3, 5, 7, 10, 20]
cont = bdl07_contours(bdl07_energy, (-3, 3), (-3, 3), 150, levels)
for lev in levels:
    for pl in cont[lev]:
        pts = [(P.X(x), P.Y(y)) for x, y in pl]
        keep = [pts[0]]
        for q in pts[1:-1]:
            if abs(q[0] - keep[-1][0]) + abs(q[1] - keep[-1][1]) > 2.5:
                keep.append(q)
        keep.append(pts[-1])
        if len(keep) >= 2:
            b += line(keep, 'mut')
# Laplace approximation: minimum and covariance from the GGN plus prior precision
best = min((bdl07_energy(1.4 + i * 0.002, 0.8 + j * 0.002), 1.4 + i * 0.002, 0.8 + j * 0.002)
           for i in range(201) for j in range(251))
_, m1, m2 = best
def bdl07_f(t1, t2):
    return (t2 * math.tanh(t1 + 1), t2 * math.tanh(-t1 + 1))
e = 1e-5
J = [[(bdl07_f(m1 + e, m2)[r] - bdl07_f(m1 - e, m2)[r]) / (2 * e),
      (bdl07_f(m1, m2 + e)[r] - bdl07_f(m1, m2 - e)[r]) / (2 * e)] for r in range(2)]
G = [[2 * sum(J[r][a] * J[r][c] for r in range(2)) + (0.4 if a == c else 0) for c in range(2)] for a in range(2)]
det = G[0][0] * G[1][1] - G[0][1] * G[1][0]
S = [[G[1][1] / det, -G[0][1] / det], [-G[1][0] / det, G[0][0] / det]]
tr = S[0][0] + S[1][1]
disc = math.sqrt(((S[0][0] - S[1][1]) / 2) ** 2 + S[0][1] ** 2)
l1, l2 = tr / 2 + disc, tr / 2 - disc
ang = 0.5 * math.atan2(2 * S[0][1], S[0][0] - S[1][1])
for k, cls, dash in ((1, 'thick', ''), (2, 'thick', ' stroke-dasharray="8 6"')):
    pts = []
    for i in range(181):
        a = 2 * math.pi * i / 180
        u, w = k * math.sqrt(l1) * math.cos(a), k * math.sqrt(l2) * math.sin(a)
        x = m1 + u * math.cos(ang) - w * math.sin(ang)
        y = m2 + u * math.sin(ang) + w * math.cos(ang)
        pts.append((P.X(x), P.Y(y)))
    b += line(pts, cls, dash)
b += '  </g>\n'
b += f'  <circle class="dot" cx="{P.X(m1):.1f}" cy="{P.Y(m2):.1f}" r="4" />\n'
b += text(P.X(m1) + 8, P.Y(m2) - 8, var('θ') + '<tspan class="sub" dy="3">*</tspan>', 'start', 'small')
b += text(P.X(-1.55), P.Y(-1.05) + 4, '0.9', 'middle', 'small')
b += text(P.X(-2.3), P.Y(0.05) + 4, '1.5', 'middle', 'small')
for v in (-3, -2, -1, 0, 1, 2, 3):
    b += text(P.x0 - 6, P.Y(v) + 4, f'{v:g}'.replace('-', '−'), 'end', 'small')
    b += text(P.X(v), P.y0 + P.h + 16, f'{v:g}'.replace('-', '−'), 'middle', 'small')
b += f'  <rect class="ln" x="{P.x0}" y="{P.y0}" width="{P.w}" height="{P.h}" />\n'
b += text(P.X(0), P.y0 + P.h + 36, var('θ') + '<tspan class="sub" dy="3">1</tspan>', 'middle')
b += text(P.x0 - 34, P.Y(0) + 4, var('θ') + '<tspan class="sub" dy="3">2</tspan>', 'middle')
svg('Bdl07LaplaceContours', 560, 365, 'Laplace approximation on a two-parameter network',
    'Grey contour lines of the energy over the two parameters theta 1 and theta 2, each from minus 3 to 3. The landscape has two symmetric minima, one near theta 1 equal to 1.6 and theta 2 equal to 1, the other near minus 1.6 and minus 1, separated by a ridge through the origin. A dot marks the right-hand minimum theta star; a thick solid ellipse around it shows one standard deviation and a thick dashed ellipse two standard deviations of the Laplace approximation. The ellipses follow the local curvature at the minimum but extend over regions where the true energy rises steeply and miss the second minimum entirely.',
    b)


# ===================== Chapter 8: Linearized Laplace approximations =====================
import numpy as _bdl08_np

def bdl08_sub(t):
    return f'<tspan class="sub" dy="4">{t}</tspan><tspan dy="-4"> </tspan>'

def bdl08_sup(t):
    return f'<tspan class="sub" dy="-6">{t}</tspan><tspan dy="6"> </tspan>'

def bdl08_path(P, xs, ys, cls, extra=''):
    return line([(P.X(a), P.Y(b)) for a, b in zip(xs, ys)], cls, extra)

def bdl08_clip(cid, P):
    return (f'  <clipPath id="{cid}"><rect x="{P.x0}" y="{P.y0}" width="{P.w}" height="{P.h}" /></clipPath>\n')

def bdl08_axes(P, xticks, yticks, xlabel, ylabel):
    o = ''
    for v in yticks:
        o += line([(P.x0, P.Y(v)), (P.x0 + P.w, P.Y(v))], 'grid')
        o += text(P.x0 - 6, P.Y(v) + 4, f'{v:g}'.replace('-', '−'), 'end', 'small')
    for v in xticks:
        o += text(P.X(v), P.y0 + P.h + 16, f'{v:g}'.replace('-', '−'), 'middle', 'small')
    o += line([(P.x0, P.y0), (P.x0, P.y0 + P.h), (P.x0 + P.w, P.y0 + P.h)])
    o += text(P.x0 + P.w / 2, P.y0 + P.h + 32, xlabel, 'middle', 'small')
    o += text(P.x0 - 30, P.y0 + P.h / 2 + 4, ylabel, 'middle', 'small')
    return o

# ---------- Figure 8.1: the linearized Laplace pipeline ----------
def bdl08_box(x, y, w, h, lines):
    s = f'  <rect class="box" x="{x}" y="{y}" width="{w}" height="{h}" rx="3" />\n'
    n = len(lines)
    for i, (t, cls) in enumerate(lines):
        yy = y + h / 2 + 5 + (i - (n - 1) / 2) * 17
        s += text(x + w / 2, yy, t, 'middle', cls)
    return s

b = ''
bw, bh = 140, 62
r1, r2 = 16, 128
xs8 = [6, 170, 334, 498]
b += bdl08_box(xs8[0], r1, 136, bh, [('MAP', None), (var('θ') + bdl08_sub('*'), None)])
b += bdl08_box(xs8[1], r1, 136, bh, [('linearized network', 'small'), (var('f') + bdl08_sup('θ*'), None)])
b += bdl08_box(xs8[2], r1, 136, bh, [('logit GP', 'small'), ('𝒢𝒫(' + var('f') + '(·, ' + var('θ') + bdl08_sub('*') + '), ' + var('k') + '(Σ))', None)])
b += bdl08_box(xs8[3], r1, 136, bh, [('predictive', 'small'), (var('p') + '(' + var('y') + bdl08_sub('*') + ' | ' + var('x') + bdl08_sub('*') + ', 𝒟)', None)])
b += bdl08_box(xs8[1], r2, 136, bh, [('curvature', 'small'), ('Ψ(' + var('θ') + bdl08_sub('*') + ')', None)])
b += bdl08_box(xs8[2], r2, 136, bh, [('parameter covariance', 'small'), ('Σ = Ψ(' + var('θ') + bdl08_sub('*') + ')' + bdl08_sup('−1'), None)])
ym = r1 + bh / 2
b += arrow([(142, ym), (168, ym)])
b += arrow([(306, ym), (332, ym)])
b += arrow([(470, ym), (496, ym)])
b += arrow([(238, r1 + bh), (238, r2 - 2)])
b += arrow([(306, r2 + bh / 2), (332, r2 + bh / 2)])
b += arrow([(402, r2), (402, r1 + bh + 2)])
svg('Bdl08Pipeline', 640, 206, 'The linearized Laplace pipeline',
    'Four boxes in a row are joined by arrows: the MAP estimate theta star, the linearized network f superscript theta star, the logit Gaussian process GP of f of dot and theta star with kernel k of Sigma, and the predictive distribution p of y star given x star and the data. Below, an arrow runs from the linearized network down to the curvature Psi of theta star, which feeds the parameter covariance Sigma equal to the inverse of Psi of theta star, and an arrow runs from the parameter covariance up into the logit GP.',
    b)

# ---------- Figure 8.2: linearized versus nonlinear predictive of the same Laplace posterior ----------
_np = _bdl08_np
_rng = _np.random.default_rng(3)
_N2 = 90
_x2 = _np.concatenate([_rng.uniform(0, 1.5, 40), _rng.uniform(2.5, 5.8, 50)])
_y2 = -1.2 * _np.sin(1.25 * _x2) + 0.5 * _np.sin(2.6 * _x2) + 0.3 * _rng.standard_normal(_N2)
_H2 = 50
_P2 = 3 * _H2 + 1

def bdl08_mlp(t, x):
    W1, b1, W2, b2 = t[:_H2], t[_H2:2*_H2], t[2*_H2:3*_H2], t[3*_H2]
    return _np.tanh(_np.outer(x, W1) + b1) @ W2 + b2

def bdl08_mlp_jac(t, x):
    W1, b1, W2 = t[:_H2], t[_H2:2*_H2], t[2*_H2:3*_H2]
    h = _np.tanh(_np.outer(x, W1) + b1)
    d = (1 - h**2) * W2
    return _np.hstack([d * x[:, None], d, h, _np.ones((len(x), 1))])

_t2 = _np.concatenate([_rng.normal(0, 1.5, _H2), _rng.normal(0, 1.5, _H2), _rng.normal(0, 1 / _np.sqrt(_H2), _H2), [0.0]])
_sig2, _delta2 = 0.3, 1.0
_m = _np.zeros(_P2); _v = _np.zeros(_P2)
for _it in range(20000):
    _r = bdl08_mlp(_t2, _x2) - _y2
    _g = bdl08_mlp_jac(_t2, _x2).T @ _r / _sig2**2 + _delta2 * _t2
    _m = 0.9 * _m + 0.1 * _g; _v = 0.999 * _v + 0.001 * _g**2
    _t2 -= 0.01 * (_m / (1 - 0.9**(_it + 1))) / (_np.sqrt(_v / (1 - 0.999**(_it + 1))) + 1e-8)
_J2 = bdl08_mlp_jac(_t2, _x2)
_S2 = _np.linalg.inv(_J2.T @ _J2 / _sig2**2 + _delta2 * _np.eye(_P2))
_L2 = _np.linalg.cholesky(_S2)
_xs2 = _np.linspace(-1.2, 7.5, 200)
_Js2 = bdl08_mlp_jac(_t2, _xs2)
_mu2 = bdl08_mlp(_t2, _xs2)
_sd_lin = _np.sqrt(_np.einsum('ij,jk,ik->i', _Js2, _S2, _Js2))
_draws = _L2 @ _rng.standard_normal((_P2, 10))
_paths_lin = [_mu2 + _Js2 @ _draws[:, i] for i in range(10)]
_paths_nl = [bdl08_mlp(_t2 + _draws[:, i], _xs2) for i in range(10)]
_mc = _np.zeros_like(_xs2); _mc2 = _np.zeros_like(_xs2); _nmc = 0
for _blk in range(20):
    _th = _t2[:, None] + _L2 @ _rng.standard_normal((_P2, 1000))
    for _i in range(1000):
        _fv = bdl08_mlp(_th[:, _i], _xs2); _mc += _fv; _mc2 += _fv**2; _nmc += 1
_mu_nl = _mc / _nmc
_sd_nl = _np.sqrt(_np.maximum(_mc2 / _nmc - _mu_nl**2, 0))

def bdl08_panel82(P, cid, mean, sd, paths, label, show_y):
    o = ''
    o += bdl08_axes(P, [0, 2, 4, 6], [-3, -2, -1, 0, 1], var('x'), var('y') if show_y else '')
    o += f'  <g clip-path="url(#{cid})">\n'
    for pth in paths:
        o += bdl08_path(P, _xs2, pth, 'mut', ' stroke-width="0.9" stroke-opacity="0.7"')
    o += bdl08_path(P, _xs2, mean + 1.96 * sd, 'ln', ' stroke-dasharray="4 3"')
    o += bdl08_path(P, _xs2, mean - 1.96 * sd, 'ln', ' stroke-dasharray="4 3"')
    o += bdl08_path(P, _xs2, mean, 'thick')
    for a, c in zip(_x2, _y2):
        o += f'  <circle class="dot" cx="{P.X(a):.1f}" cy="{P.Y(c):.1f}" r="2.6" />\n'
    o += '  </g>\n'
    o += text(P.x0 + P.w / 2, P.y0 + P.h + 50, label, 'middle')
    return o

PA = Plot(52, 14, 250, 200, (-1.2, 7.5), (-3.2, 1.6))
PB = Plot(372, 14, 250, 200, (-1.2, 7.5), (-3.2, 1.6))
b = '  <defs>\n' + bdl08_clip('bdl08lin-clip-a', PA) + bdl08_clip('bdl08lin-clip-b', PB) + '  </defs>\n'
b += bdl08_panel82(PA, 'bdl08lin-clip-a', _mu2, _sd_lin, _paths_lin, '(a)', True)
b += bdl08_panel82(PB, 'bdl08lin-clip-b', _mu_nl, _sd_nl, _paths_nl, '(b)', True)
svg('Bdl08LinVsNonlin', 640, 284, 'One Laplace posterior under the linearized and the nonlinear predictive',
    'Two panels share a one-dimensional regression data set with inputs between 0 and 1.5 and between 2.5 and 5.8, and the same ten parameter draws from a full Laplace posterior of a small tanh network. Panel a, linearized network: the thin sample paths, the solid predictive mean and the dashed 95 percent bounds follow the data closely and widen only away from it. Panel b, nonlinear network: the sample paths swing far outside the plotted range, the dashed bounds lie outside the plot over the whole input range and the solid Monte Carlo mean misses the data.',
    b)

# ---------- Figure 8.3: one-dimensional regression with a Bayesian last layer ----------
_rng3 = _np.random.default_rng(8)
_x3 = _np.sort(_np.concatenate([_rng3.uniform(-3.1, -0.2, 11), _rng3.uniform(1.15, 3.0, 9)]))
_g3 = lambda x: 0.55 - 0.32 * x + 0.62 * _np.sin(2.1 * x + 0.1) - 0.08 * x**2
_s3 = lambda x: 0.06 + 0.32 / (1 + _np.exp(-3.0 * (x - 0.6)))
_y3 = _g3(_x3) + _s3(_x3) * _rng3.standard_normal(len(_x3))
_c3 = _np.linspace(-3.6, 3.6, 13)

def bdl08_feat(x):
    x = _np.atleast_1d(x)
    return _np.hstack([_np.exp(-0.5 * ((x[:, None] - _c3[None, :]) / 0.7)**2), _np.ones((len(x), 1)), x[:, None]])

_Phi3 = bdl08_feat(_x3)
_W3 = 1 / _s3(_x3)**2
_A3 = _Phi3.T @ (_W3[:, None] * _Phi3) + 1.0 * _np.eye(_Phi3.shape[1])
_S3 = _np.linalg.inv(_A3)
_w3 = _S3 @ (_Phi3.T @ (_W3 * _y3))
_xs3 = _np.linspace(-3.2, 3.2, 260)
_F3 = bdl08_feat(_xs3)
_mu3 = _F3 @ _w3
_sd3 = _np.sqrt(_np.einsum('ij,jk,ik->i', _F3, _S3, _F3))
_so3 = _np.sqrt(_sd3**2 + _s3(_xs3)**2)

P3 = Plot(60, 60, 560, 200, (-3.2, 3.2), (-2.7, 2.3))
b = '  <defs>\n' + bdl08_clip('bdl08llr-clip', P3) + '  </defs>\n'
b += bdl08_axes(P3, [-3, -2, -1, 0, 1, 2, 3], [-2, -1, 0, 1, 2], var('x'), var('y'))
b += '  <g clip-path="url(#bdl08llr-clip)">\n'
band = [(P3.X(a), P3.Y(c)) for a, c in zip(_xs3, _mu3 + 1.96 * _sd3)] + [(P3.X(a), P3.Y(c)) for a, c in zip(_xs3[::-1], (_mu3 - 1.96 * _sd3)[::-1])]
b += '  <path class="band" d="' + ' '.join(('M' if i == 0 else 'L') + f'{p[0]:.1f},{p[1]:.1f}' for i, p in enumerate(band)) + ' Z" />\n'
b += bdl08_path(P3, _xs3, _g3(_xs3), 'mut', ' stroke-dasharray="1.5 3"')
b += bdl08_path(P3, _xs3, _mu3 + 1.96 * _so3, 'ln', ' stroke-dasharray="4 3" stroke-width="1"')
b += bdl08_path(P3, _xs3, _mu3 - 1.96 * _so3, 'ln', ' stroke-dasharray="4 3" stroke-width="1"')
b += bdl08_path(P3, _xs3, _mu3, 'thick')
for a, c in zip(_x3, _y3):
    e = 1.0 * _s3(a)
    b += line([(P3.X(a), P3.Y(c - e)), (P3.X(a), P3.Y(c + e))], 'mut')
    b += f'  <circle class="dot" cx="{P3.X(a):.1f}" cy="{P3.Y(c):.1f}" r="3" />\n'
b += '  </g>\n'
lx, ly = 100, 14
b += f'  <rect class="band" x="{lx}" y="{ly}" width="28" height="11" />\n' + text(lx + 36, ly + 10, 'GP latent 95%', 'start', 'small')
b += line([(lx, ly + 30), (lx + 28, ly + 30)], 'mut', ' stroke-dasharray="1.5 3"') + text(lx + 36, ly + 34, 'signal', 'start', 'small')
b += line([(lx + 170, ly + 6), (lx + 198, ly + 6)], 'thick') + text(lx + 206, ly + 10, 'MAP / GP mean', 'start', 'small')
b += line([(lx + 170, ly + 30), (lx + 198, ly + 30)], 'ln', ' stroke-dasharray="4 3" stroke-width="1"') + text(lx + 206, ly + 34, 'observation 95%', 'start', 'small')
b += line([(lx + 350, ly - 1), (lx + 350, ly + 13)], 'mut') + f'  <circle class="dot" cx="{lx + 350}" cy="{ly + 6}" r="3" />\n' + text(lx + 362, ly + 10, 'training data', 'start', 'small')
svg('Bdl08LastLayerRegression', 640, 300, 'Linearized Laplace regression with a Bayesian last layer and input-dependent noise',
    'Twenty training points with one-standard-deviation error bars: eleven between x equal to minus 3.1 and minus 0.2 with small noise, nine between 1.15 and 3 with much larger noise, and a gap in between. The solid MAP and GP mean follows the dotted signal, the shaded latent 95 percent band is narrow on the left, widens slightly in the gap and widens more on the noisy right, and the dashed observation 95 percent curves sit close to the band on the left and far outside it on the right.',
    b)

# ---------- Figure 8.4: Iris last-layer Laplace classification ----------
_iris_v = '3.2,1.4 3.2,1.5 3.1,1.5 2.3,1.3 2.8,1.5 2.8,1.3 3.3,1.6 2.4,1.0 2.9,1.3 2.7,1.4 2.0,1.0 3.0,1.5 2.2,1.0 2.9,1.4 2.9,1.3 3.1,1.4 3.0,1.5 2.7,1.0 2.2,1.5 2.5,1.1 3.2,1.8 2.8,1.3 2.5,1.5 2.8,1.2 2.9,1.3 3.0,1.4 2.8,1.4 3.0,1.7 2.9,1.5 2.6,1.0 2.4,1.1 2.4,1.0 2.7,1.2 2.7,1.6 3.0,1.5 3.4,1.6 3.1,1.5 2.3,1.3 3.0,1.3 2.5,1.3 2.6,1.2 3.0,1.4 2.6,1.2 2.3,1.0 2.7,1.3 3.0,1.2 2.9,1.3 2.9,1.3 2.5,1.1 2.8,1.3'
_iris_g = '3.3,2.5 2.7,1.9 3.0,2.1 2.9,1.8 3.0,2.2 3.0,2.1 2.5,1.7 2.9,1.8 2.5,1.8 3.6,2.5 3.2,2.0 2.7,1.9 3.0,2.1 2.5,2.0 2.8,2.4 3.2,2.3 3.0,1.8 3.8,2.2 2.6,2.3 2.2,1.5 3.2,2.3 2.8,2.0 2.8,2.0 2.7,1.8 3.3,2.1 3.2,1.8 2.8,1.8 3.0,1.8 2.8,2.1 3.0,1.6 2.8,1.9 3.8,2.0 2.8,2.2 2.8,1.5 2.6,1.4 3.0,2.3 3.4,2.4 3.1,1.8 3.0,1.8 3.1,2.1 3.1,2.4 3.1,2.3 2.7,1.9 3.2,2.3 3.3,2.5 3.0,2.3 2.5,1.9 3.0,2.0 3.4,2.3 3.0,1.8'
_X4 = _np.array([[float(u) for u in p.split(',')] for p in (_iris_v + ' ' + _iris_g).split()])
_Y4 = _np.array([0] * 50 + [1] * 50)
_rng4 = _np.random.default_rng(4)
_split = _np.empty(100, dtype=int)
for _cls in (0, 1):
    _idx = _rng4.permutation(_np.where(_Y4 == _cls)[0])
    _split[_idx[:30]] = 0; _split[_idx[30:40]] = 1; _split[_idx[40:]] = 2
_mu4 = _X4.mean(0); _sdv4 = _X4.std(0)
_Wf = _rng4.normal(0, 1.5, (2, 60)); _bf = _rng4.uniform(-2, 2, 60)

def bdl08_iris_feat(X):
    Z = (X - _mu4) / _sdv4
    return _np.hstack([_np.tanh(Z @ _Wf + _bf), _np.ones((len(X), 1))])

def bdl08_sigmoid(a):
    return 1 / (1 + _np.exp(-a))

def bdl08_fit(Phi, y, alpha):
    w = _np.zeros(Phi.shape[1])
    for _ in range(100):
        p = bdl08_sigmoid(Phi @ w)
        Hm = Phi.T @ (Phi * (p * (1 - p))[:, None]) + alpha * _np.eye(len(w))
        w -= _np.linalg.solve(Hm, Phi.T @ (p - y) + alpha * w)
    p = bdl08_sigmoid(Phi @ w)
    Hm = Phi.T @ (Phi * (p * (1 - p))[:, None]) + alpha * _np.eye(len(w))
    return w, _np.linalg.inv(Hm)

_eps4 = _np.random.default_rng(5).standard_normal(2000)
def bdl08_mc(m, v):
    return bdl08_sigmoid(m[:, None] + _np.sqrt(v)[:, None] * _eps4[None, :]).mean(1)

_Phi4 = bdl08_iris_feat(_X4)
_tr, _va = _split == 0, _split == 1
_best = None
for _alpha in [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10]:
    _w, _S = bdl08_fit(_Phi4[_tr], _Y4[_tr], _alpha)
    _m = _Phi4[_va] @ _w; _vv = _np.einsum('ij,jk,ik->i', _Phi4[_va], _S, _Phi4[_va])
    _p = _np.clip(bdl08_mc(_m, _vv), 1e-9, 1 - 1e-9)
    _ls = -_np.mean(_Y4[_va] * _np.log(_p) + (1 - _Y4[_va]) * _np.log(1 - _p))
    if _best is None or _ls < _best[0]:
        _best = (_ls, _alpha, _w, _S)
_, _alpha4, _w4, _S4 = _best

_xr4, _yr4 = (1.9, 3.95), (0.9, 2.6)
_nx4, _ny4 = 60, 43
_gx = _np.linspace(_xr4[0], _xr4[1], _nx4); _gy = _np.linspace(_yr4[1], _yr4[0], _ny4)
_GX, _GY = _np.meshgrid(_gx, _gy)
_G4 = _np.column_stack([_GX.ravel(), _GY.ravel()])
_F4 = bdl08_iris_feat(_G4)
_m4 = _F4 @ _w4
_v4 = _np.einsum('ij,jk,ik->i', _F4, _S4, _F4)
_p_map = bdl08_sigmoid(_m4)
_p_mc = bdl08_mc(_m4, _v4)
_p_pr = bdl08_sigmoid(_m4 / _np.sqrt(1 + _np.pi * _v4 / 8))
_pc = _np.clip(_p_mc, 1e-12, 1 - 1e-12)
_ent = -(_pc * _np.log(_pc) + (1 - _pc) * _np.log(1 - _pc)) / _np.log(2)

def bdl08_heat(P, vals, levels=20):
    q = _np.round(vals.reshape(_ny4, _nx4) * levels) / levels
    cw, ch = P.w / _nx4, P.h / _ny4
    o = '  <g class="dot">\n'
    for j in range(_ny4):
        i = 0
        while i < _nx4:
            k = i
            while k + 1 < _nx4 and q[j, k + 1] == q[j, i]:
                k += 1
            if q[j, i] > 0:
                o += (f'  <rect x="{P.x0 + i * cw:.1f}" y="{P.y0 + j * ch:.1f}" width="{(k - i + 1) * cw + 0.3:.1f}" '
                      f'height="{ch + 0.3:.1f}" fill-opacity="{0.85 * q[j, i]:.2f}" />\n')
            i = k + 1
    return o + '  </g>\n'

def bdl08_marker(P, xv, yv, kind, black):
    cls = 'arrowhead' if black else 'box'
    X, Y = P.X(xv), P.Y(yv)
    if kind == 0:
        return f'  <circle class="{cls}" cx="{X:.1f}" cy="{Y:.1f}" r="3.4" stroke-width="1" />\n'
    if kind == 1:
        return f'  <path class="{cls}" d="M{X:.1f},{Y - 4:.1f} L{X + 3.8:.1f},{Y + 2.8:.1f} L{X - 3.8:.1f},{Y + 2.8:.1f} Z" stroke-width="1" />\n'
    return f'  <rect class="{cls}" x="{X - 3.2:.1f}" y="{Y - 3.2:.1f}" width="6.4" height="6.4" stroke-width="1" />\n'

def bdl08_panel84(P, vals, label):
    o = bdl08_heat(P, vals)
    o += f'  <rect class="ln" x="{P.x0}" y="{P.y0}" width="{P.w}" height="{P.h}" stroke-width="1" />\n'
    for (xv, yv), cl, sp in zip(_X4, _Y4, _split):
        o += bdl08_marker(P, xv, yv, sp, cl == 1)
    for v in (2.0, 2.5, 3.0, 3.5):
        o += text(P.X(v), P.y0 + P.h + 14, f'{v:g}', 'middle', 'small')
    for v in (1.0, 1.5, 2.0, 2.5):
        o += text(P.x0 - 5, P.Y(v) + 4, f'{v:g}', 'end', 'small')
    o += text(P.x0 + P.w / 2, P.y0 + P.h + 46, label, 'middle')
    return o

_pw, _ph = 262, 186
_Q = [Plot(52, 34, _pw, _ph, _xr4, _yr4), Plot(368, 34, _pw, _ph, _xr4, _yr4),
      Plot(52, 316, _pw, _ph, _xr4, _yr4), Plot(368, 316, _pw, _ph, _xr4, _yr4)]
b = ''
for Pq, vals, lab in zip(_Q, [_p_map, _p_mc, _p_pr, _ent], ['(a) MAP', '(b) Monte Carlo softmax', '(c) probit approximation', '(d) predictive entropy']):
    b += bdl08_panel84(Pq, vals, lab)
    b += text(Pq.x0 + Pq.w / 2, Pq.y0 + Pq.h + 30, 'sepal width (cm)', 'middle', 'small')
    b += text(Pq.x0 - 34, Pq.y0 - 10, 'petal width (cm)', 'start', 'small')
svg('Bdl08IrisLaplace', 640, 590, 'Last-layer Laplace classification of two Iris species',
    'Four heat maps over sepal width from 1.9 to 3.95 centimeters and petal width from 0.9 to 2.6 centimeters, each overlaid with the 100 versicolor (open markers) and virginica (filled markers) flowers, with circles for training, triangles for validation and squares for test points. In panels a to c the accent shading gives the probability of virginica: the MAP panel switches sharply from light at small petal width to dark at large petal width, while the Monte Carlo and probit panels show the same boundary with a broader, softer transition that fades toward intermediate shading away from the data, and the two are nearly identical. Panel d shades the predictive entropy, which is highest along the class boundary and away from the data and lowest in the two class clusters.',
    b)


# ---------- Bdl09: Figure 9.1, fibers of the restricted network and the tangent space ----------
def bdl09_proj(cx, cy, s, x, y, z):
    # oblique projection: x to the right, y into the page (foreshortened), z up
    return (cx + s * (x + 0.30 * y), cy - s * (0.9 * z - 0.30 * y))

def bdl09_bowl(cx, cy, s, rim_cls='ln'):
    o = ''
    # parallels (circles of radius r at height r^2)
    for r in (0.25, 0.5, 0.75):
        pts = [bdl09_proj(cx, cy, s, r * math.cos(2 * math.pi * i / 72), r * math.sin(2 * math.pi * i / 72), r * r) for i in range(73)]
        o += line(pts, 'mut')
    # meridians
    for k in range(12):
        a = 2 * math.pi * k / 12
        pts = [bdl09_proj(cx, cy, s, r * math.cos(a), r * math.sin(a), r * r) for r in [i / 20 for i in range(21)]]
        o += line(pts, 'mut')
    # rim
    pts = [bdl09_proj(cx, cy, s, math.cos(2 * math.pi * i / 90), math.sin(2 * math.pi * i / 90), 1.0) for i in range(91)]
    o += line(pts, rim_cls)
    # outline of the visible sides
    for sgn in (-1, 1):
        pts = [bdl09_proj(cx, cy, s, sgn * r, 0, r * r) for r in [i / 20 for i in range(21)]]
        o += line(pts, rim_cls)
    return o

b = ''
# left panel: one fiber and its tangent plane at theta0
cx, cy, s = 175, 190, 90
corners = [(-1.3, -1.1), (1.3, -1.1), (1.3, 1.1), (-1.3, 1.1)]
pts = [bdl09_proj(cx, cy, s, x, y, 0) for x, y in corners]
b += f'  <polygon class="region" points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" />\n'
b += line(pts + [pts[0]], 'mut')
b += bdl09_bowl(cx, cy, s)
b += f'  <circle class="dot" cx="{cx}" cy="{cy}" r="4" />\n'
b += text(cx + 8, cy + 20, var('θ') + '<tspan class="sub" dy="3">0</tspan>', 'start', 'small')
b += text(18, 64, var('ℳ') + '(' + var('θ') + '<tspan class="sub" dy="3">0</tspan><tspan dy="-3">)</tspan>', 'start')
b += text(18, 200, var('T') + '<tspan class="sub" dy="3">θ0</tspan><tspan dy="-3"> </tspan>' + var('ℳ') + '(' + var('θ') + '<tspan class="sub" dy="3">0</tspan><tspan dy="-3">)</tspan>', 'start')
# right panel: three fibers stacked in parameter space
cx2, s2 = 480, 80
for k, (yy, lab) in enumerate(((140, '0'), (195, '1'), (250, '2'))):
    b += bdl09_bowl(cx2, yy, s2, 'ln' if k == 0 else 'ln')
for yy, lab, ly in ((140, '0', 64), (195, '1', 120), (250, '2', 176)):
    b += text(330, ly, var('ℳ') + '(' + var('θ') + f'<tspan class="sub" dy="3">{lab}</tspan><tspan dy="-3">)</tspan>', 'start')
svg('Bdl09Fibers', 640, 262, 'Fibers of the restricted network and the tangent space of one fiber',
    'Left: a curved bowl-shaped surface labelled M of theta 0, the fiber through the parameter theta 0, with a flat shaded plane touching it at its lowest point theta 0, labelled T theta 0 M of theta 0, the tangent space of the fiber. Right: three such bowl-shaped surfaces stacked above one another, labelled M of theta 0, M of theta 1 and M of theta 2, three disjoint fibers into which the parameter space is partitioned.',
    b)


# ---------- Bdl10: Figure 10.1, MAP vs Laplace vs RGPR confidence on two moons ----------
# Schematic reproduction computed here: a small ReLU network (2-32-32-1) trained by
# full-batch Adam on a two-moons data set, a last-layer Laplace approximation with the
# probit (MacKay) approximation, and an RGPR term with variance growing cubically in |x|.
import numpy as _np10

def bdl10_moons(n, noise, rng):
    m = n // 2
    t1 = _np10.linspace(0, _np10.pi, m); t2 = _np10.linspace(0, _np10.pi, n - m)
    a = _np10.stack([_np10.cos(t1), _np10.sin(t1)], 1)
    b = _np10.stack([1 - _np10.cos(t2), 1 - _np10.sin(t2) - 0.5], 1)
    X = _np10.concatenate([a, b]) + noise * rng.standard_normal((n, 2))
    y = _np10.concatenate([_np10.zeros(m), _np10.ones(n - m)])
    X = (X - _np10.array([0.5, 0.25])) * 2.0
    return X, y

def bdl10_train():
    rng = _np10.random.default_rng(10)
    X, y = bdl10_moons(160, 0.12, rng)
    sizes = [2, 32, 32, 1]
    W = [rng.standard_normal((sizes[i], sizes[i+1])) * _np10.sqrt(2.0 / sizes[i]) for i in range(3)]
    B = [_np10.zeros(sizes[i+1]) for i in range(3)]
    params = W + B
    m = [_np10.zeros_like(p) for p in params]; v = [_np10.zeros_like(p) for p in params]
    lr, wd = 0.01, 5e-4
    for it in range(1, 4001):
        h1p = X @ W[0] + B[0]; h1 = _np10.maximum(h1p, 0)
        h2p = h1 @ W[1] + B[1]; h2 = _np10.maximum(h2p, 0)
        f = (h2 @ W[2] + B[2])[:, 0]
        p = 1 / (1 + _np10.exp(-f))
        g = (p - y)[:, None] / len(y)
        gW2 = h2.T @ g; gB2 = g.sum(0)
        d2 = (g @ W[2].T) * (h2p > 0)
        gW1 = h1.T @ d2; gB1 = d2.sum(0)
        d1 = (d2 @ W[1].T) * (h1p > 0)
        gW0 = X.T @ d1; gB0 = d1.sum(0)
        grads = [gW0 + wd*W[0], gW1 + wd*W[1], gW2 + wd*W[2], gB0, gB1, gB2]
        for k in range(6):
            m[k] = 0.9*m[k] + 0.1*grads[k]; v[k] = 0.999*v[k] + 0.001*grads[k]**2
            mh = m[k] / (1 - 0.9**it); vh = v[k] / (1 - 0.999**it)
            params[k] -= lr * mh / (_np10.sqrt(vh) + 1e-8)
    return X, y, W, B

def bdl10_feat(Xq, W, B):
    h1 = _np10.maximum(Xq @ W[0] + B[0], 0)
    h2 = _np10.maximum(h1 @ W[1] + B[1], 0)
    return _np10.concatenate([h2, _np10.ones((len(Xq), 1))], 1)

bdl10_X, bdl10_y, bdl10_W, bdl10_B = bdl10_train()
bdl10_w = _np10.concatenate([bdl10_W[2][:, 0], bdl10_B[2]])
_phi = bdl10_feat(bdl10_X, bdl10_W, bdl10_B)
_pp = 1 / (1 + _np10.exp(-_phi @ bdl10_w))
bdl10_prior_var = 100.0
_H = (_phi * (_pp*(1-_pp))[:, None]).T @ _phi + _np10.eye(len(bdl10_w)) / bdl10_prior_var
bdl10_Sigma = _np10.linalg.inv(_H)

def bdl10_conf(Xq, kind):
    ph = bdl10_feat(Xq, bdl10_W, bdl10_B)
    mu = ph @ bdl10_w
    if kind == 'map':
        s2 = _np10.zeros_like(mu)
    else:
        s2 = _np10.einsum('ij,jk,ik->i', ph, bdl10_Sigma, ph)
        if kind == 'rgpr':
            s2 = s2 + 1000.0 * (_np10.maximum(_np10.abs(Xq) - 3.0, 0)**3).sum(1) / 3
    p = 1 / (1 + _np10.exp(-mu / _np10.sqrt(1 + _np10.pi * s2 / 8)))
    return _np10.maximum(p, 1 - p), mu

def bdl10_contour(F, xs, ys, P):
    # marching squares for the zero level of F (F[j, i] at x = xs[i], y = ys[j])
    segs = ''
    for j in range(len(ys) - 1):
        for i in range(len(xs) - 1):
            c = [(xs[i], ys[j], F[j, i]), (xs[i+1], ys[j], F[j, i+1]),
                 (xs[i+1], ys[j+1], F[j+1, i+1]), (xs[i], ys[j+1], F[j+1, i])]
            pts = []
            for k in range(4):
                (xa, ya, fa), (xb, yb, fb) = c[k], c[(k+1) % 4]
                if (fa > 0) != (fb > 0):
                    t = fa / (fa - fb)
                    pts.append((xa + t*(xb-xa), ya + t*(yb-ya)))
            for a in range(0, len(pts) - 1, 2):
                (x1, y1), (x2, y2) = pts[a], pts[a+1]
                segs += f'M{P.X(x1):.1f},{P.Y(y1):.1f} L{P.X(x2):.1f},{P.Y(y2):.1f} '
    return f'  <path class="thick" d="{segs.strip()}" />\n'

def bdl10_panel(x0, y0, size, kind, title, show_y):
    P = Plot(x0, y0, size, size, (-5, 5), (-5, 5))
    o = ''
    # heatmap: 32 x 32 cells, opacity quantized to steps of 0.1, equal cells merged along rows
    n = 32; cell = 10 / n
    cs = _np10.array([[-5 + (i + 0.5)*cell, -5 + (j + 0.5)*cell] for j in range(n) for i in range(n)])
    conf, _ = bdl10_conf(cs, kind)
    lev = _np10.round((conf - 0.5) / 0.5 * 10).astype(int).reshape(n, n)
    o += '  <g class="dot" shape-rendering="crispEdges">\n'
    for j in range(n):
        i = 0
        while i < n:
            k = i
            while k + 1 < n and lev[j, k + 1] == lev[j, i]:
                k += 1
            if lev[j, i] > 0:
                x1 = P.X(-5 + i*cell); x2 = P.X(-5 + (k + 1)*cell)
                y1 = P.Y(-5 + (j + 1)*cell); y2 = P.Y(-5 + j*cell)
                o += (f'    <rect x="{x1:.1f}" y="{y1:.1f}" width="{x2 - x1:.1f}" height="{y2 - y1:.1f}" '
                      f'fill-opacity="{lev[j, i]/10:.1f}" />\n')
            i = k + 1
    o += '  </g>\n'
    g = 60; xs = _np10.linspace(-5, 5, g); ys = _np10.linspace(-5, 5, g)
    XX, YY = _np10.meshgrid(xs, ys)
    _, mu = bdl10_conf(_np10.stack([XX.ravel(), YY.ravel()], 1), 'map')
    o += bdl10_contour(mu.reshape(g, g), xs, ys, P)
    o += '  <g style="stroke-width:0.8">\n'
    for (px, py), lab in zip(bdl10_X, bdl10_y):
        cls = 'arrowhead' if lab == 0 else 'box'
        o += f'    <circle class="{cls}" cx="{P.X(px):.1f}" cy="{P.Y(py):.1f}" r="1.8" />\n'
    o += '  </g>\n'
    o += f'  <rect class="ln" x="{x0}" y="{y0}" width="{size}" height="{size}" />\n'
    for v in (-4, -2, 0, 2, 4):
        o += text(P.X(v), y0 + size + 13, f'{v:g}'.replace('-', '−'), 'middle', 'small')
        if show_y:
            o += text(x0 - 4, P.Y(v) + 4, f'{v:g}'.replace('-', '−'), 'end', 'small')
    o += text(x0 + size/2, y0 + size + 29, var('x') + '<tspan class="sub" dy="3">1</tspan>', 'middle')
    o += text(x0 + size/2, y0 - 8, title, 'middle')
    return o

b = ''
S = 128
b += text(14, 28 + S/2, var('x') + '<tspan class="sub" dy="3">2</tspan>', 'middle')
b += bdl10_panel(42, 28, S, 'map', 'MAP', True)
b += bdl10_panel(42 + S + 12, 28, S, 'laplace', 'Laplace', False)
b += bdl10_panel(42 + 2*(S + 12), 28, S, 'rgpr', 'RGPR', False)
# far-right panel: confidence along a ray alpha * x0, log-scaled distance
_dir = _np10.array([0.6, -0.8])
lx0 = 42 + 3*(S + 12) + 34
Q = Plot(lx0, 28, 150, S, (0, 2), (0.45, 1.02))
b += line([(Q.x0, Q.Y(0.5)), (Q.x0 + Q.w, Q.Y(0.5))], 'grid')
for v in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
    b += text(Q.x0 - 4, Q.Y(v) + 4, f'{v:.1f}', 'end', 'small')
    b += line([(Q.x0, Q.Y(v)), (Q.x0 + Q.w, Q.Y(v))], 'grid')
b += f'  <rect class="ln" x="{Q.x0}" y="{Q.y0}" width="{Q.w}" height="{Q.h}" />\n'
b += text(Q.X(0), Q.y0 + Q.h + 14, '10<tspan dy="-5" class="sub">0</tspan>', 'middle', 'small')
b += text(Q.X(1), Q.y0 + Q.h + 14, '10<tspan dy="-5" class="sub">1</tspan>', 'middle', 'small')
b += text(Q.X(2), Q.y0 + Q.h + 14, '10<tspan dy="-5" class="sub">2</tspan>', 'middle', 'small')
b += text(Q.x0 + Q.w/2, Q.y0 + Q.h + 29, 'Distance from origin', 'middle', 'small')
b += text(Q.x0 + Q.w/2, 20, 'Confidence', 'middle')
_ls = _np10.linspace(0, 2, 160)
_ray = (10**_ls)[:, None] * _dir[None, :]
_styles = {'map': ('thick', ''), 'laplace': ('ln', ' stroke-dasharray="5 3"'), 'rgpr': ('acc', ' stroke-dasharray="7 3 2 3"')}
bdl10_rayconf = {}
for kind, (cls, extra) in _styles.items():
    c, _ = bdl10_conf(_ray, kind)
    bdl10_rayconf[kind] = c
    b += line([(Q.X(l), Q.Y(cv)) for l, cv in zip(_ls, c)], cls, extra)
ly = Q.y0 + Q.h + 52
for k, (kind, lab) in enumerate([('map', 'MAP'), ('laplace', 'Laplace'), ('rgpr', 'RGPR')]):
    cls, extra = _styles[kind]
    xx = 120 + k * 150
    b += line([(xx, ly - 4), (xx + 28, ly - 4)], cls, extra)
    b += text(xx + 34, ly, lab, 'start', 'small')
# colour bar for the heatmap shading (confidence 0.5 to 1.0), as in the original figure
cbx = Q.x0 + Q.w + 10
b += '  <g class="dot" shape-rendering="crispEdges">\n'
for k in range(1, 11):
    yb = Q.Y(0.5 + 0.05 * (k - 1)); yt = Q.Y(0.5 + 0.05 * k)
    b += f'    <rect x="{cbx}" y="{yt:.1f}" width="8" height="{yb - yt + 0.6:.1f}" fill-opacity="{k/10:.1f}" />\n'
b += '  </g>\n'
b += f'  <rect class="ln" x="{cbx}" y="{Q.Y(1.0):.1f}" width="8" height="{Q.Y(0.5) - Q.Y(1.0):.1f}" style="stroke-width:1" />\n'
for v, lab in ((0.5, '0.5'), (0.75, '0.75'), (1.0, '1.0')):
    b += text(cbx + 11, Q.Y(v) + 4, lab, 'start', 'small')
b += text(42, ly + 22, 'Shading: stronger = higher confidence (0.5 to 1). Line: decision boundary, p = 0.5.', 'start', 'small')
svg('Bdl10OverconfidenceRgpr', 700, 28 + S + 105, 'Predictive confidence of MAP, Laplace and RGPR on two moons',
    'Three square panels over the input square from minus 5 to 5 show the confidence of a ReLU network on a two-moons data set, with the decision boundary drawn as a line. In the MAP panel nearly the whole plane is shaded dark, meaning confidence close to 1 everywhere except along the boundary. In the Laplace panel the shading fades with distance from the data. In the RGPR panel the shading is light everywhere away from the data. A fourth panel plots the maximum confidence along a ray against the distance from the origin on a logarithmic axis from 1 to 100: the MAP curve rises to 1, the Laplace curve levels off below 1, and the RGPR curve falls back toward 0.5. A colour bar beside it maps the shading to confidence values from 0.5 to 1.0.',
    b)
print('ray confidence at distance 100:', {k: round(float(v[-1]), 3) for k, v in bdl10_rayconf.items()})


# ---------- Chapter 11: model selection with the marginal likelihood ----------
import random as bdl11_random

def bdl11_gauss(mu, s, a):
    return lambda x: a * math.exp(-0.5 * ((x - mu) / s) ** 2)

# Figure 11.1: Occam's razor
def bdl11_occam():
    P = Plot(60, 30, 540, 200, (-1.0, 1.0), (0, 1.05))
    b = ''
    b += f'  <rect class="ln" x="{P.x0}" y="{P.y0}" width="{P.w}" height="{P.h}" />\n'
    simple = bdl11_gauss(0.0, 0.17, 1.0)
    inter = bdl11_gauss(0.0, 0.40, 0.49)
    comp = bdl11_gauss(0.0, 1.4, 0.19)
    b += P.curve(simple, cls='thick')
    b += P.curve(inter, cls='thick', extra=' stroke-dasharray="9 6"')
    b += P.curve(comp, cls='thick', extra=' stroke-dasharray="2 5"')
    xd = 0.33
    b += line([(P.X(xd), P.Y(0) + 12), (P.X(xd), P.Y(inter(xd)))], 'ln', ' stroke-dasharray="4 3"')
    for f in (simple, inter, comp):
        b += f'  <circle class="dot" cx="{P.X(xd):.1f}" cy="{P.Y(f(xd)):.1f}" r="4" />\n'
    b += text(P.X(xd), P.Y(0) + 28, var('𝒟'), 'middle')
    b += f'  <text class="small" x="0" y="0" text-anchor="middle" transform="translate(30 {P.y0 + P.h / 2:.1f}) rotate(-90)">' + var('p') + '(' + var('𝒟') + ' | ' + var('ℳ') + ')</text>\n'
    lx, ly = 420, 46
    for i, (lab, dash) in enumerate((('simple model', ''), ('intermediate model', ' stroke-dasharray="9 6"'), ('complex model', ' stroke-dasharray="2 5"'))):
        y = ly + 18 * i
        b += line([(lx, y), (lx + 34, y)], 'thick', dash)
        b += text(lx + 42, y + 4, lab, 'start', 'small')
    svg('Bdl11OccamRazor', 620, 290, 'Occam’s razor effect of the marginal likelihood',
        'Three bell-shaped curves of the marginal likelihood p of D given M over the space of all possible datasets. The simple model is tall and narrow, the intermediate model is lower and wider, and the complex model is low and almost flat across the whole axis. At a marked dataset D to the right of the peaks, the intermediate model has the highest value, the complex model the middle value and the simple model the lowest.',
        b)

# Figure 11.2: online selection of prior variances on a small BNN
def bdl11_online():
    b = ''
    # panel 1: log marginal likelihood vs steps
    A = Plot(36, 20, 120, 110, (0, 1), (0, 1))
    b += line([(A.x0, A.y0), (A.x0, A.y0 + A.h), (A.x0 + A.w, A.y0 + A.h)])
    def lml(t):
        # rises in two smooth steps and converges
        return 0.92 - 0.55 * math.exp(-6 * t) - 0.25 / (1 + math.exp((t - 0.38) / 0.04)) - 0.12 / (1 + math.exp((t - 0.62) / 0.03)) + 0.0 * t
    b += A.curve(lambda t: min(0.97, max(0.02, lml(t) - lml(0) + 0.05)), cls='thick')
    b += text(A.x0 + A.w / 2, A.y0 + A.h + 18, 'steps', 'middle', 'small')
    b += f'  <text class="small" x="0" y="0" text-anchor="middle" transform="translate(22 {A.y0 + A.h / 2:.1f}) rotate(-90)">log ' + var('q') + '(' + var('𝒟') + ' | ' + var('ℳ') + ')</text>\n'
    # panel 2: prior variances vs steps
    B = Plot(196, 20, 120, 110, (0, 1), (0, 1))
    b += line([(B.x0, B.y0), (B.x0, B.y0 + B.h), (B.x0 + B.w, B.y0 + B.h)])
    curves = [
        (lambda t: 0.35 + 0.55 * t - 0.15 * math.exp(-((t - 0.25) / 0.1) ** 2) + 0.12 * math.exp(-((t - 0.15) / 0.08) ** 2), ''),
        (lambda t: 0.35 + 0.25 * math.exp(-((t - 0.18) / 0.1) ** 2) - 0.12 * (1 - math.exp(-5 * t)), ' stroke-dasharray="8 3 2 3"'),
        (lambda t: 0.35 - 0.12 * (1 - math.exp(-8 * t)) + 0.05 * t, ' stroke-dasharray="2 3"'),
        (lambda t: 0.35 - 0.25 * (1 - math.exp(-10 * t)) + 0.08 * t, ' stroke-dasharray="6 4"'),
    ]
    for f, dash in curves:
        b += B.curve(f, n=120, cls='mut', extra=dash)
    b += line([(B.x0 + 8, B.y0 + 12), (B.x0 + 26, B.y0 + 12)], 'mut')
    b += text(B.x0 + 30, B.y0 + 16, var('σ') + '<tspan class="sub" dy="4">ℓ</tspan><tspan class="sub" dy="-9">2</tspan>', 'start', 'small')
    b += text(B.x0 + B.w / 2, B.y0 + B.h + 18, 'steps', 'middle', 'small')
    b += f'  <text class="small" x="0" y="0" text-anchor="middle" transform="translate(182 {B.y0 + B.h / 2:.1f}) rotate(-90)">prior variances</text>\n'
    # data: two interleaved classes
    rng = bdl11_random.Random(11)
    pts = []
    for i in range(40):
        a = rng.uniform(0, math.pi)
        pts.append((math.cos(a) * 0.55 - 0.2 + rng.gauss(0, 0.12), math.sin(a) * 0.55 - 0.1 + rng.gauss(0, 0.12), 0))
        a = rng.uniform(0, math.pi)
        pts.append((0.2 - math.cos(a) * 0.55 + rng.gauss(0, 0.12), 0.1 - math.sin(a) * 0.55 + 0.1 + rng.gauss(0, 0.12), 1))
    def smooth(x, y):
        g = y - 0.35 * math.sin(2.2 * x) - 0.05
        return 1 / (1 + math.exp(-g / 0.18))
    def jagged(x, y):
        g = y - 0.35 * math.sin(2.2 * x) - 0.05 + 0.22 * math.sin(9 * x + 1) * math.cos(7 * y) + 0.12 * math.sin(13 * y - 4 * x)
        return 1 / (1 + math.exp(-g / 0.03))
    n = 22
    for (px, f, lab) in ((372, smooth, 'optimized'), (500, jagged, 'naïve')):
        size = 110
        cell = size / n
        for i in range(n):
            for j in range(n):
                x = -1 + 2 * (i + 0.5) / n
                y = 1 - 2 * (j + 0.5) / n
                p = f(x, y)
                b += f'  <rect class="arrowhead" x="{px + i * cell:.1f}" y="{20 + j * cell:.1f}" width="{cell + 0.3:.1f}" height="{cell + 0.3:.1f}" style="fill-opacity:{0.04 + 0.42 * p:.2f}" />\n'
        b += f'  <rect class="ln" x="{px}" y="20" width="{size}" height="{size}" />\n'
        for (x, y, c) in pts:
            sx = px + (x + 1) / 2 * size
            sy = 20 + (1 - y) / 2 * size
            if not (px + 2 < sx < px + size - 2 and 22 < sy < 128):
                continue
            if c == 0:
                b += f'  <circle class="dot" cx="{sx:.1f}" cy="{sy:.1f}" r="2.2" />\n'
            else:
                b += line([(sx - 2.5, sy - 2.5), (sx + 2.5, sy + 2.5)], 'ln') + line([(sx - 2.5, sy + 2.5), (sx + 2.5, sy - 2.5)], 'ln')
        b += text(px + size / 2, 148, lab, 'middle', 'small')
    # colour bar
    cx = 628
    for k in range(10):
        p = 1 - (k + 0.5) / 10
        b += f'  <rect class="arrowhead" x="{cx}" y="{20 + k * 11:.1f}" width="12" height="11.3" style="fill-opacity:{0.04 + 0.42 * p:.2f}" />\n'
    b += f'  <rect class="ln" x="{cx}" y="20" width="12" height="110" />\n'
    for v, y in ((1, 24), (0.5, 79), (0, 134)):
        b += text(cx + 16, y, f'{v:g}', 'start', 'small')
    b += f'  <text class="small" x="0" y="0" text-anchor="middle" transform="translate(676 75) rotate(90)">' + var('p') + '(' + var('y') + '<tspan class="sub" dy="3">*</tspan><tspan dy="-3"> | </tspan>' + var('x') + '<tspan class="sub" dy="3">*</tspan><tspan dy="-3">, </tspan>' + var('𝒟') + ')</text>\n'
    svg('Bdl11OnlineSelection', 690, 160, 'Online selection of layerwise prior variances with the Laplace marginal likelihood',
        'Four panels. First, the log Laplace marginal likelihood log q of D given M increases monotonically over training steps in several stages and levels off. Second, the layerwise prior variances change during training: one rises steadily while the others drop and settle. Third and fourth, the predictive class probability over a two-dimensional input space with the training points of two classes shown as dots and crosses: the optimized model has a smooth, gradual decision boundary, while the naively trained model has a sharp, irregular boundary with isolated patches. A grey-scale bar maps shading to probabilities from 0 to 1.',
        b)

# Figure 11.3: flat and sharp minima
def bdl11_flat_sharp():
    P = Plot(60, 20, 540, 230, (0, 1), (0, 1.05))
    b = ''
    b += f'  <rect class="ln" x="{P.x0}" y="{P.y0}" width="{P.w}" height="{P.h}" />\n'
    def train(x):
        return 0.04 + 3.0 * (x - 0.38) ** 2 - 0.68 * math.exp(-((x - 0.87) / 0.03) ** 2)
    def test(x):
        return train(x - 0.06) + 0.02
    def upto(f):
        pts = []
        for i in range(401):
            x = i / 400
            if f(x) > 1.05:
                break
            pts.append((P.X(x), P.Y(f(x))))
        return pts
    b += line(upto(train), 'thick')
    b += line(upto(test), 'thick', ' stroke-dasharray="9 6"')
    for xm, lab in ((0.38, 'flat'), (0.87, 'sharp')):
        b += line([(P.X(xm), P.y0), (P.X(xm), P.y0 + P.h + 6)], 'ln', ' stroke-dasharray="2 3"')
        b += f'  <circle class="dot" cx="{P.X(xm):.1f}" cy="{P.Y(train(xm)):.1f}" r="4" />\n'
        b += f'  <circle class="dot" cx="{P.X(xm):.1f}" cy="{P.Y(test(xm)):.1f}" r="4" />\n'
        b += text(P.X(xm), P.y0 + P.h + 24, var('θ') + '<tspan class="sub" dy="4">*</tspan><tspan class="sub" dy="-12">' + lab + '</tspan>', 'middle')
    b += f'  <text class="small" x="0" y="0" text-anchor="middle" transform="translate(32 {P.y0 + P.h / 2:.1f}) rotate(-90)">− log ' + var('p') + '(' + var('θ') + ' | ' + var('𝒟') + ')</text>\n'
    lx, ly = P.x0 + 12, P.y0 + 18
    b += line([(lx, ly), (lx + 34, ly)], 'thick') + text(lx + 42, ly + 4, 'Training loss', 'start', 'small')
    b += line([(lx, ly + 18), (lx + 34, ly + 18)], 'thick', ' stroke-dasharray="9 6"') + text(lx + 42, ly + 22, 'Test loss', 'start', 'small')
    svg('Bdl11FlatSharpMinima', 620, 290, 'Training and test loss around a flat and a sharp minimum',
        'The training loss, a solid curve of the negative log posterior, has a broad flat minimum at theta star flat and a narrow sharp minimum at theta star sharp further right, separated by a hump. The test loss, dashed, is the same landscape shifted slightly to the right. At the flat minimum the test loss is only slightly higher than the training loss, while at the sharp minimum the test loss sits near the top of the hump.',
        b)

bdl11_occam()
bdl11_online()
bdl11_flat_sharp()
