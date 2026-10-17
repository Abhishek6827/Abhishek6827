import json
import os

with open(r'd:\Desktop\Resume-Extension\profile-assets\icons_data.json') as f:
    icons = json.load(f)

FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"

# Coordinates for 8 slots:
# Slot 0: Inner Left (-135, -28)
# Slot 1: Inner Right (130, 26)
# Slot 2: Inner Top (0, -56)
# Slot 3: Mid Left (-235, -42)
# Slot 4: Mid Top-Right (90, -78)
# Slot 5: Mid Bottom-Left (-85, 74)
# Slot 6: Outer Left (-325, 18)
# Slot 7: Outer Right (245, 42)

slots = [
    {"x": -135, "y": -28, "w": 105},
    {"x": 130, "y": 26, "w": 100},
    {"x": 0, "y": -56, "w": 118},
    {"x": -235, "y": -42, "w": 105},
    {"x": 90, "y": -78, "w": 112},
    {"x": -85, "y": 74, "w": 108},
    {"x": -325, "y": 18, "w": 110},
    {"x": 245, "y": 42, "w": 115}
]

# Batch 1: Core Architecture & Cloud
batch_1 = [
    {"name": "Next.js", "icon": "Next.js", "color": "#ffffff", "border": "#38bdf8"},
    {"name": "React", "icon": "React", "color": "#61dafb", "border": "#61dafb"},
    {"name": "TypeScript", "icon": "TypeScript", "color": "#3178c6", "border": "#60a5fa"},
    {"name": "Java", "icon": "Java", "color": "#f89820", "border": "#f59e0b"},
    {"name": "Spring Boot", "icon": "Spring", "color": "#6db33f", "border": "#4ade80"},
    {"name": "AWS Cloud", "icon": "AWS", "color": "#ff9900", "border": "#ff9900"},
    {"name": "Node.js", "icon": "Node.js", "color": "#5fa04e", "border": "#5fa04e"},
    {"name": "Supabase", "icon": "Supabase", "color": "#3ecf8e", "border": "#3ecf8e"}
]

# Batch 2: Frameworks & Databases
batch_2 = [
    {"name": "Tailwind", "icon": "Tailwind", "color": "#06b6d4", "border": "#06b6d4"},
    {"name": "Redux", "icon": "Redux", "color": "#764abc", "border": "#a855f7"},
    {"name": "JavaScript", "icon": "JavaScript", "color": "#f7df1e", "border": "#eab308"},
    {"name": "Angular", "icon": "Angular", "color": "#dd0031", "border": "#f43f5e"},
    {"name": "Express.js", "icon": "Express", "color": "#ffffff", "border": "#94a3b8"},
    {"name": "Django", "icon": "Django", "color": "#44b78b", "border": "#10b981"},
    {"name": "PostgreSQL", "icon": "PostgreSQL", "color": "#4169e1", "border": "#60a5fa"},
    {"name": "MongoDB", "icon": "MongoDB", "color": "#47a248", "border": "#22c55e"}
]

# Batch 3: AI Copilots, Fintech & Ecosystem
batch_3 = [
    {"name": "OpenAI", "icon": "OpenAI", "color": "#10a37f", "border": "#10a37f"},
    {"name": "Gemini AI", "icon": "Gemini", "color": "#8e75ff", "border": "#c084fc"},
    {"name": "Python", "icon": "Python", "color": "#3776ab", "border": "#38bdf8"},
    {"name": "Stripe", "icon": "Stripe", "color": "#635bff", "border": "#818cf8"},
    {"name": "Razorpay", "icon": "Razorpay", "color": "#3395ff", "border": "#38bdf8"},
    {"name": "Firebase", "icon": "Firebase", "color": "#ffca28", "border": "#facc15"},
    {"name": "Electron", "icon": "Electron", "color": "#47848f", "border": "#22d3ee"},
    {"name": "Docker", "icon": "Docker", "color": "#2496ed", "border": "#38bdf8"}
]

def render_node(cfg, slot_idx):
    slot = slots[slot_idx]
    x, y, w = slot["x"], slot["y"], slot["w"]
    h = 28
    half_w = w / 2
    half_h = h / 2
    
    icon_info = icons.get(cfg["icon"], {})
    color = cfg["color"]
    border = cfg["border"]
    name = cfg["name"]
    
    # Render official SVG icon vector
    if icon_info.get("is_multi_path"):
        # AWS multi-path
        icon_svg = f'''<svg x="{-half_w + 6}" y="{-8}" width="16" height="16" viewBox="0 0 256 256">'''
        for p in icon_info["paths"]:
            icon_svg += f'''<path fill="{p['fill']}" d="{p['d']}"/>'''
        icon_svg += '</svg>'
    else:
        d_path = icon_info.get("d", "")
        icon_svg = f'''<svg x="{-half_w + 7}" y="{-8}" width="16" height="16" viewBox="0 0 24 24" fill="{color}">
          <path d="{d_path}"/>
        </svg>'''
        
    return f'''
      <g transform="translate({x}, {y})">
        <rect x="{-half_w}" y="{-half_h}" width="{w}" height="{h}" rx="14" fill="#0b1224" stroke="{border}" stroke-width="1.2" stroke-opacity="0.9"/>
        {icon_svg}
        <text x="{-half_w + 28}" y="4" fill="#ffffff" font-size="11" font-weight="700">{name}</text>
      </g>'''

def render_batch(batch_list, class_name):
    nodes_svg = ""
    for idx, item in enumerate(batch_list):
        nodes_svg += render_node(item, idx)
    return f'''<g class="{class_name}">{nodes_svg}</g>'''

batch_1_svg = render_batch(batch_1, "st-batch-1")
batch_2_svg = render_batch(batch_2, "st-batch-2")
batch_3_svg = render_batch(batch_3, "st-batch-3")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="900" height="480" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="st-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <radialGradient id="st-core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#ff354f" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="st-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <style>
    @media (prefers-reduced-motion: reduce) {{
      .st-anim {{ animation: none !important; }}
    }}
    .st-pulse {{
      animation: stPulse 3s ease-in-out infinite;
    }}
    @keyframes stPulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.95; }}
      50% {{ transform: scale(1.06); opacity: 1; }}
    }}

    /* 15s total cycle (5s per batch with smooth 0.5s cross-fade) */
    .st-batch-1 {{ animation: cycleBatch1 15s infinite ease-in-out; }}
    .st-batch-2 {{ animation: cycleBatch2 15s infinite ease-in-out; }}
    .st-batch-3 {{ animation: cycleBatch3 15s infinite ease-in-out; }}

    @keyframes cycleBatch1 {{
      0%, 30% {{ opacity: 1; transform: scale(1); pointer-events: auto; }}
      33%, 97% {{ opacity: 0; transform: scale(0.92); pointer-events: none; }}
      100% {{ opacity: 1; transform: scale(1); pointer-events: auto; }}
    }}
    @keyframes cycleBatch2 {{
      0%, 30% {{ opacity: 0; transform: scale(0.92); pointer-events: none; }}
      33%, 63% {{ opacity: 1; transform: scale(1); pointer-events: auto; }}
      66%, 100% {{ opacity: 0; transform: scale(0.92); pointer-events: none; }}
    }}
    @keyframes cycleBatch3 {{
      0%, 63% {{ opacity: 0; transform: scale(0.92); pointer-events: none; }}
      66%, 97% {{ opacity: 1; transform: scale(1); pointer-events: auto; }}
      100% {{ opacity: 0; transform: scale(0.92); pointer-events: none; }}
    }}

    /* Progress Segment Bars */
    .st-bar-1 {{ animation: stBarFill1 15s infinite linear; }}
    .st-bar-2 {{ animation: stBarFill2 15s infinite linear; }}
    .st-bar-3 {{ animation: stBarFill3 15s infinite linear; }}

    @keyframes stBarFill1 {{
      0% {{ width: 0px; }}
      30%, 99% {{ width: 85px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes stBarFill2 {{
      0%, 33% {{ width: 0px; }}
      63%, 99% {{ width: 85px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes stBarFill3 {{
      0%, 66% {{ width: 0px; }}
      97%, 99% {{ width: 85px; }}
      100% {{ width: 0px; }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="480" rx="20" fill="#070b16"/>
  <rect width="900" height="480" fill="url(#st-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="478.5" rx="19.25" fill="none" stroke="url(#st-border)" stroke-width="1.5"/>

  <!-- Top Header Title & Batch Cycle Progress Indicators -->
  <g transform="translate(50, 34)">
    <rect width="170" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="85" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      02 // TECH ARSENAL
    </text>
    
    <!-- Rotating Header Indicator -->
    <g class="st-batch-1">
      <text x="185" y="16" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11">BATCH 01 // CORE ARCHITECTURE &amp; CLOUD (NEXT.JS · REACT · JAVA · AWS · NODE)</text>
    </g>
    <g class="st-batch-2">
      <text x="185" y="16" fill="#34d399" font-family="{FONT_MONO}" font-size="11">BATCH 02 // MODERN FRAMEWORKS &amp; DATABASES (TAILWIND · ANGULAR · POSTGRES · MONGO)</text>
    </g>
    <g class="st-batch-3">
      <text x="185" y="16" fill="#f43f5e" font-family="{FONT_MONO}" font-size="11">BATCH 03 // AI COPILOTS, PAYMENTS &amp; ECOSYSTEM (OPENAI · GEMINI · STRIPE · DOCKER)</text>
    </g>

    <!-- 3 Batch Segment Progress Bars -->
    <g transform="translate(530, 8)">
      <g transform="translate(0, 0)">
        <rect width="85" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#38bdf8" class="st-bar-1"/>
      </g>
      <g transform="translate(95, 0)">
        <rect width="85" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#34d399" class="st-bar-2"/>
      </g>
      <g transform="translate(190, 0)">
        <rect width="85" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#f43f5e" class="st-bar-3"/>
      </g>
    </g>
  </g>

  <!-- ORBITAL VISUALIZATION (Center: 450, 185) -->
  <g transform="translate(450, 185)">
    <!-- Central Core Glow -->
    <circle cx="0" cy="0" r="120" fill="url(#st-core-glow)"/>

    <!-- Tilted Elliptical Orbit 3 (Outer Ecosystem) -->
    <ellipse cx="0" cy="0" rx="360" ry="110" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.25" stroke-dasharray="6 6" transform="rotate(-9)"/>
    
    <!-- Tilted Elliptical Orbit 2 (Middle Cloud & Backend) -->
    <ellipse cx="0" cy="0" rx="260" ry="80" fill="none" stroke="#ff354f" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="4 4" transform="rotate(-9)"/>

    <!-- Tilted Elliptical Orbit 1 (Inner Core Frontend & Language) -->
    <ellipse cx="0" cy="0" rx="160" ry="50" fill="none" stroke="#38bdf8" stroke-width="1.4" stroke-opacity="0.45" transform="rotate(-9)"/>

    <!-- Center Sun / Core Engine -->
    <g class="st-pulse" transform="translate(0, 0)">
      <circle cx="0" cy="0" r="32" fill="#0b1224" stroke="#247bff" stroke-width="2"/>
      <circle cx="0" cy="0" r="37" fill="none" stroke="#ff354f" stroke-width="1" stroke-opacity="0.5"/>
      <text x="0" y="-3" fill="#ffffff" font-family="{FONT_MONO}" font-size="10.5" font-weight="800" text-anchor="middle">CHINTU</text>
      <text x="0" y="11" fill="#38bdf8" font-family="{FONT_MONO}" font-size="8.5" font-weight="700" text-anchor="middle">ENGINE</text>
    </g>

    <!-- 3 ROTATING BATCHES WITH AUTHENTIC VECTOR LOGOS -->
    {batch_1_svg}
    {batch_2_svg}
    {batch_3_svg}
  </g>

  <!-- BOTTOM SECTION: Categorized Tech Stack Overview (3 Comprehensive Cards) -->
  <g transform="translate(50, 335)">
    <!-- Box 1: Frontend & UI -->
    <g transform="translate(0, 0)">
      <rect width="255" height="118" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <text x="16" y="24" fill="#60a5fa" font-family="{FONT_MONO}" font-size="11" font-weight="700">⚔️ FRONTEND ARSENAL</text>
      <text x="16" y="48" fill="#f1f5f9" font-size="12" font-weight="600">Next.js 14 · React 18 · TypeScript</text>
      <text x="16" y="68" fill="#94a3b8" font-size="11.5">Tailwind CSS · Redux Toolkit · Angular</text>
      <text x="16" y="88" fill="#94a3b8" font-size="11.5">JavaScript · HTML5 · CSS Modules</text>
      <text x="16" y="106" fill="#64748b" font-size="10.5">Framer Motion · Chrome Extensions</text>
    </g>

    <!-- Box 2: Backend, Java & AWS Cloud -->
    <g transform="translate(270, 0)">
      <rect width="255" height="118" rx="12" fill="#0b1224" stroke="#f59e0b" stroke-width="1" stroke-opacity="0.4"/>
      <text x="16" y="24" fill="#fbbf24" font-family="{FONT_MONO}" font-size="11" font-weight="700">☕ JAVA, AWS &amp; BACKEND</text>
      <text x="16" y="48" fill="#f1f5f9" font-size="12" font-weight="600">Java 17/21 (Spring Boot) · AWS Cloud</text>
      <text x="16" y="68" fill="#94a3b8" font-size="11.5">AWS Elastic Beanstalk · Node.js · Express</text>
      <text x="16" y="88" fill="#94a3b8" font-size="11.5">Django · Python · PostgreSQL · MySQL</text>
      <text x="16" y="106" fill="#64748b" font-size="10.5">Supabase · MongoDB · Firebase · REST</text>
    </g>

    <!-- Box 3: AI, Payments & Ecosystem -->
    <g transform="translate(540, 0)">
      <rect width="260" height="118" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <text x="16" y="24" fill="#f43f5e" font-family="{FONT_MONO}" font-size="11" font-weight="700">🤖 AI, FINTECH &amp; ECOSYSTEM</text>
      <text x="16" y="48" fill="#f1f5f9" font-size="12" font-weight="600">OpenAI · Google Gemini · Groq</text>
      <text x="16" y="68" fill="#94a3b8" font-size="11.5">AssemblyAI · Alibaba · Stripe · Razorpay</text>
      <text x="16" y="88" fill="#94a3b8" font-size="11.5">Zoho Payments · LaTeX Engine · Webhooks</text>
      <text x="16" y="106" fill="#64748b" font-size="10.5">Electron · Docker · Vercel · Git/GitHub</text>
    </g>
  </g>
</svg>'''

output_paths = [
    r"D:\Desktop\Projects\Abhishek6827\assets\stack.svg",
    r"D:\Desktop\Resume-Extension\profile-assets\stack.svg"
]

for p in output_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(svg_content)

print("Generated new stack.svg with 3 animated batches and authentic vector logos!")
