import json
import math
import os
import xml.etree.ElementTree as ET

icons_path = r'd:\Desktop\Resume-Extension\profile-assets\icons_data.json'
with open(icons_path, 'r', encoding='utf-8') as f:
    icons = json.load(f)

FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"

# Tilt angle for 2.5D galactic perspective
TILT_DEG = -8
ALPHA = math.radians(TILT_DEG)
COS_A = math.cos(ALPHA)
SIN_A = math.sin(ALPHA)

def generate_orbit_keyframes(name, rx, ry, reverse=False):
    css = f"@keyframes {name} {{\n"
    steps = 40
    direction = -1 if reverse else 1
    for i in range(steps + 1):
        pct = (i / steps) * 100
        theta = direction * (i / steps) * 2 * math.pi
        x = rx * math.cos(theta) * COS_A - ry * math.sin(theta) * SIN_A
        y = rx * math.cos(theta) * SIN_A + ry * math.sin(theta) * COS_A
        css += f"  {pct:.1f}% {{ transform: translate({x:.1f}px, {y:.1f}px); }}\n"
    css += "}\n"
    return css

# 3 Orbits configuration:
# Orbit 1: Inner (4 techs, 22s)
orbit1_rx, orbit1_ry, orbit1_dur = 165, 55, 22
orbit1_techs = [
    {"name": "Next.js", "icon": "Next.js", "color": "#ffffff", "border": "#38bdf8"},
    {"name": "React", "icon": "React", "color": "#61dafb", "border": "#61dafb"},
    {"name": "TypeScript", "icon": "TypeScript", "color": "#3178c6", "border": "#60a5fa"},
    {"name": "Java", "icon": "Java", "color": "#f89820", "border": "#f59e0b"}
]

# Orbit 2: Middle (5 techs, 32s, reverse orbit for depth!)
orbit2_rx, orbit2_ry, orbit2_dur = 265, 82, 32
orbit2_techs = [
    {"name": "Spring Boot", "icon": "Spring", "color": "#6db33f", "border": "#4ade80"},
    {"name": "AWS Cloud", "icon": "AWS", "color": "#ff9900", "border": "#ff9900"},
    {"name": "Node.js", "icon": "Node.js", "color": "#5fa04e", "border": "#5fa04e"},
    {"name": "PostgreSQL", "icon": "PostgreSQL", "color": "#4169e1", "border": "#60a5fa"},
    {"name": "Supabase", "icon": "Supabase", "color": "#3ecf8e", "border": "#3ecf8e"}
]

# Orbit 3: Outer (6 techs, 44s)
orbit3_rx, orbit3_ry, orbit3_dur = 360, 110, 44
orbit3_techs = [
    {"name": "OpenAI", "icon": "OpenAI", "color": "#10a37f", "border": "#10a37f"},
    {"name": "Gemini AI", "icon": "Gemini", "color": "#8e75ff", "border": "#c084fc"},
    {"name": "Python", "icon": "Python", "color": "#3776ab", "border": "#38bdf8"},
    {"name": "Stripe", "icon": "Stripe", "color": "#635bff", "border": "#818cf8"},
    {"name": "Docker", "icon": "Docker", "color": "#2496ed", "border": "#38bdf8"},
    {"name": "Electron", "icon": "Electron", "color": "#47848f", "border": "#22d3ee"}
]

css_keyframes = ""
css_keyframes += generate_orbit_keyframes("orbitInner", orbit1_rx, orbit1_ry, reverse=False)
css_keyframes += generate_orbit_keyframes("orbitMid", orbit2_rx, orbit2_ry, reverse=True)
css_keyframes += generate_orbit_keyframes("orbitOuter", orbit3_rx, orbit3_ry, reverse=False)

def render_revolving_pill(tech, anim_name, dur, delay):
    icon_info = icons.get(tech["icon"], {})
    name = tech["name"]
    color = tech["color"]
    border = tech["border"]
    
    text_w = len(name) * 7.5
    w = max(88, int(text_w + 38))
    h = 26
    half_w = w / 2
    half_h = h / 2
    
    if icon_info.get("is_multi_path"):
        icon_svg = f'<svg x="{-half_w + 7}" y="{-7.5}" width="15" height="15" viewBox="0 0 256 256">'
        for p in icon_info["paths"]:
            icon_svg += f'<path fill="{p["fill"]}" d="{p["d"]}"/>'
        icon_svg += '</svg>'
    else:
        d = icon_info.get("d", "")
        icon_svg = f'<svg x="{-half_w + 7}" y="{-7.5}" width="15" height="15" viewBox="0 0 24 24" fill="{color}"><path d="{d}"/></svg>'
        
    return f'''
    <!-- Revolving Planet: {name} -->
    <g style="animation: {anim_name} {dur}s linear infinite; animation-delay: {delay:.2f}s; will-change: transform;">
      <rect x="{-half_w}" y="{-half_h}" width="{w}" height="{h}" rx="13" fill="#0b1224" stroke="{border}" stroke-width="1.2" stroke-opacity="0.95"/>
      {icon_svg}
      <text x="{-half_w + 26}" y="4" fill="#ffffff" font-size="11" font-weight="700">{name}</text>
    </g>'''

# Generate all revolving planets
planets_svg = ""

# Orbit 1 (4 items)
for idx, item in enumerate(orbit1_techs):
    delay = - (idx / len(orbit1_techs)) * orbit1_dur
    planets_svg += render_revolving_pill(item, "orbitInner", orbit1_dur, delay)

# Orbit 2 (5 items)
for idx, item in enumerate(orbit2_techs):
    delay = - (idx / len(orbit2_techs)) * orbit2_dur
    planets_svg += render_revolving_pill(item, "orbitMid", orbit2_dur, delay)

# Orbit 3 (6 items)
for idx, item in enumerate(orbit3_techs):
    delay = - (idx / len(orbit3_techs)) * orbit3_dur
    planets_svg += render_revolving_pill(item, "orbitOuter", orbit3_dur, delay)

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500" width="900" height="500" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="st-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <radialGradient id="st-core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="st-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <style>
    @media (prefers-reduced-motion: reduce) {{
      * {{ animation: none !important; }}
    }}
    .st-pulse {{
      animation: stPulse 3s ease-in-out infinite;
    }}
    @keyframes stPulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.95; }}
      50% {{ transform: scale(1.08); opacity: 1; }}
    }}

    {css_keyframes}
  </style>

  <!-- Background Base -->
  <rect width="900" height="500" rx="20" fill="#070b16"/>
  <rect width="900" height="500" fill="url(#st-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="498.5" rx="19.25" fill="none" stroke="url(#st-border)" stroke-width="1.5"/>

  <!-- Top Header Title: Matching Screenshot 1 (03 / MY ENGINE ROOM) -->
  <g transform="translate(50, 32)">
    <rect width="180" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="90" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      03 // MY ENGINE ROOM
    </text>
    <text x="195" y="16" fill="#ffffff" font-size="14.5" font-weight="800" letter-spacing="0.5">TOOLS CHANGE. CURIOSITY DOESN'T.</text>
    <text x="545" y="16" fill="#64748b" font-family="{FONT_MONO}" font-size="10.5" font-weight="600">LANGUAGES / SYSTEMS / INTELLIGENCE</text>

    <!-- Top Right Real-Time Orbiting Status Badge -->
    <g transform="translate(680, 0)">
      <rect width="120" height="24" rx="6" fill="#0b1224" stroke="#38bdf8" stroke-width="1" stroke-opacity="0.8"/>
      <circle cx="14" cy="12" r="3.5" fill="#38bdf8" class="st-pulse"/>
      <text x="24" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="700">LIVE ORBITS ⚡</text>
    </g>
  </g>

  <!-- REVOLVING GALAXY SECTION (Center: 450, 195) -->
  <g transform="translate(450, 195)">
    <!-- Central Core Glow Aura -->
    <circle cx="0" cy="0" r="140" fill="url(#st-core-glow)"/>

    <!-- Tilted Elliptical Orbit Paths -->
    <ellipse cx="0" cy="0" rx="{orbit3_rx}" ry="{orbit3_ry}" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.25" stroke-dasharray="6 6" transform="rotate({TILT_DEG})"/>
    <ellipse cx="0" cy="0" rx="{orbit2_rx}" ry="{orbit2_ry}" fill="none" stroke="#ff354f" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="4 4" transform="rotate({TILT_DEG})"/>
    <ellipse cx="0" cy="0" rx="{orbit1_rx}" ry="{orbit1_ry}" fill="none" stroke="#38bdf8" stroke-width="1.4" stroke-opacity="0.45" transform="rotate({TILT_DEG})"/>

    <!-- Center Sun / Core Engine -->
    <g class="st-pulse">
      <circle cx="0" cy="0" r="34" fill="#0b1224" stroke="#247bff" stroke-width="2"/>
      <circle cx="0" cy="0" r="39" fill="none" stroke="#ff354f" stroke-width="1" stroke-opacity="0.5"/>
      <text x="0" y="-3" fill="#ffffff" font-family="{FONT_MONO}" font-size="10.5" font-weight="800" text-anchor="middle">CHINTU</text>
      <text x="0" y="11" fill="#38bdf8" font-family="{FONT_MONO}" font-size="8.5" font-weight="700" text-anchor="middle">ENGINE</text>
    </g>

    <!-- CONTINUOUSLY REVOLVING PLANETS -->
    {planets_svg}
  </g>

  <!-- BOTTOM SECTION: Categorized Tech Stack Overview (3 Cards) -->
  <g transform="translate(50, 350)">
    <!-- Card 1: Frontend -->
    <g transform="translate(0, 0)">
      <rect width="255" height="120" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <text x="16" y="24" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="700">⚔️ FRONTEND ARSENAL</text>
      <text x="16" y="44" fill="#ffffff" font-size="13" font-weight="700">Next.js 14 · React 18 · TypeScript</text>
      <text x="16" y="64" fill="#94a3b8" font-size="11">Tailwind CSS · Redux Toolkit · Angular</text>
      <text x="16" y="82" fill="#94a3b8" font-size="11">JavaScript · HTML5 · CSS Modules</text>
      <text x="16" y="100" fill="#64748b" font-family="{FONT_MONO}" font-size="10">Framer Motion · Chrome Extensions</text>
    </g>

    <!-- Card 2: Java, AWS & Backend -->
    <g transform="translate(272, 0)">
      <rect width="255" height="120" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <text x="16" y="24" fill="#f59e0b" font-family="{FONT_MONO}" font-size="10" font-weight="700">☕ JAVA, AWS &amp; BACKEND</text>
      <text x="16" y="44" fill="#ffffff" font-size="13" font-weight="700">Java 17/21 (Spring Boot) · AWS Cloud</text>
      <text x="16" y="64" fill="#94a3b8" font-size="11">AWS Elastic Beanstalk · Node.js · Express</text>
      <text x="16" y="82" fill="#94a3b8" font-size="11">Django · Python · PostgreSQL · MySQL</text>
      <text x="16" y="100" fill="#64748b" font-family="{FONT_MONO}" font-size="10">Supabase · MongoDB · Firebase · REST</text>
    </g>

    <!-- Card 3: AI, Fintech & Ecosystem -->
    <g transform="translate(545, 0)">
      <rect width="255" height="120" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <text x="16" y="24" fill="#f43f5e" font-family="{FONT_MONO}" font-size="10" font-weight="700">🤖 AI, FINTECH &amp; ECOSYSTEM</text>
      <text x="16" y="44" fill="#ffffff" font-size="13" font-weight="700">OpenAI · Google Gemini · Groq</text>
      <text x="16" y="64" fill="#94a3b8" font-size="11">AssemblyAI · Alibaba · Stripe · Razorpay</text>
      <text x="16" y="82" fill="#94a3b8" font-size="11">Zoho Payments · LaTeX Engine · Webhooks</text>
      <text x="16" y="100" fill="#64748b" font-family="{FONT_MONO}" font-size="10">Electron · Docker · Vercel · Git/GitHub</text>
    </g>
  </g>
</svg>'''

out_path = r'd:\Desktop\Resume-Extension\profile-assets\stack.svg'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(svg_content)

ET.parse(out_path)
print("Successfully generated revolving galaxy stack.svg! Valid XML!")
