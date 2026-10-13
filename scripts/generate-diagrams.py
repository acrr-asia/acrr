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
    'In the complex h-lambda plane, explicit Euler is stable inside the disc of radius 1 centred at minus 1. The RK4 region is larger: it reaches about minus 2.79 on the real axis and about plus and minus 2.83 j on the imaginary axis. The point h-lambda equal to minus 2.5, from lambda equal to minus 50 and h equal to 0.05, lies outside the Euler disc but inside the RK4 region.',
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
    f'Three bell-shaped curves over position. The prediction is centred at {xp:g} metres with standard deviation {math.sqrt(Pp):.2f} metres; '
    f'the measurement is centred at {zm:g} metres with standard deviation {math.sqrt(Rm):.2f} metres. The fused estimate is centred at {xf:.2f} metres, '
    f'between the two and closer to the more precise measurement, and is narrower than either, with standard deviation {math.sqrt(Pf):.2f} metres.',
    b)
