import json
import os
import io
import base64
from PIL import Image

def get_optimized_b64(path):
    img = Image.open(path)
    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('ascii')

# Load icons
with open(r'd:\Desktop\Resume-Extension\profile-assets\icons_data.json') as f:
    icons = json.load(f)

FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"

repo_assets = r"D:\Desktop\Projects\Abhishek6827\assets"
local_assets = r"D:\Desktop\Resume-Extension\profile-assets"

# ==============================================================================
# 1. FIX ABOUT-LIFE.SVG: PIXEL-PERFECT ALIGNMENT & ZERO GHOST TEXT
# ==============================================================================
about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 395" width="900" height="395" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="ab-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="ab-bar-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <linearGradient id="ab-bar-crimson" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff354f"/>
      <stop offset="100%" stop-color="#fb7185"/>
    </linearGradient>
    <linearGradient id="ab-bar-amber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#fbbf24"/>
    </linearGradient>
    <radialGradient id="ab-glow" cx="80%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="ab-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <style>
    @media (prefers-reduced-motion: reduce) {{
      .ab-anim {{ animation: none !important; }}
    }}

    /* 12s total cycle with visibility toggle to eliminate ghosting completely */
    .ab-slide-1 {{ animation: slideFade1 12s infinite ease-in-out; }}
    .ab-slide-2 {{ animation: slideFade2 12s infinite ease-in-out; }}
    .ab-slide-3 {{ animation: slideFade3 12s infinite ease-in-out; }}

    @keyframes slideFade1 {{
      0%, 28% {{ opacity: 1; visibility: visible; transform: translateY(0); }}
      31%, 97% {{ opacity: 0; visibility: hidden; transform: translateY(6px); }}
      100% {{ opacity: 1; visibility: visible; transform: translateY(0); }}
    }}
    @keyframes slideFade2 {{
      0%, 30% {{ opacity: 0; visibility: hidden; transform: translateY(6px); }}
      33%, 61% {{ opacity: 1; visibility: visible; transform: translateY(0); }}
      64%, 100% {{ opacity: 0; visibility: hidden; transform: translateY(6px); }}
    }}
    @keyframes slideFade3 {{
      0%, 63% {{ opacity: 0; visibility: hidden; transform: translateY(6px); }}
      66%, 94% {{ opacity: 1; visibility: visible; transform: translateY(0); }}
      97%, 100% {{ opacity: 0; visibility: hidden; transform: translateY(6px); }}
    }}

    /* Segment progress bar animations */
    .ab-prog-1 {{ animation: progFill1 12s infinite linear; }}
    .ab-prog-2 {{ animation: progFill2 12s infinite linear; }}
    .ab-prog-3 {{ animation: progFill3 12s infinite linear; }}

    @keyframes progFill1 {{
      0% {{ width: 0px; }}
      28%, 99% {{ width: 106px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes progFill2 {{
      0%, 33% {{ width: 0px; }}
      61%, 99% {{ width: 106px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes progFill3 {{
      0%, 66% {{ width: 0px; }}
      94%, 99% {{ width: 106px; }}
      100% {{ width: 0px; }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="395" rx="20" fill="#070b16"/>
  <rect width="900" height="395" fill="url(#ab-glow)"/>
  <rect width="900" height="395" fill="url(#ab-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="393.5" rx="19.25" fill="none" stroke="url(#ab-border)" stroke-width="1.5"/>

  <!-- Top Header Title -->
  <g transform="translate(50, 36)">
    <rect width="195" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="97" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      01 // CAPABILITIES &amp; LIFE
    </text>
    <text x="215" y="17" fill="#64748b" font-family="{FONT_MONO}" font-size="11">ENGINEERING CORE + LIFE PHILOSOPHY</text>
  </g>

  <!-- LEFT COLUMN: Engineering Capabilities (width: 380, height: 295) -->
  <g transform="translate(50, 75)">
    <rect width="380" height="295" rx="16" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
    
    <!-- Title -->
    <text x="24" y="32" fill="#f8fafc" font-size="15" font-weight="700">Production Capabilities</text>
    <text x="24" y="48" fill="#64748b" font-family="{FONT_MONO}" font-size="10">VERIFIED DOMAINS &amp; ARCHITECTURAL STRENGTH</text>

    <!-- Cap 1: Full-Stack & Next.js -->
    <g transform="translate(24, 75)">
      <text x="0" y="0" fill="#e2e8f0" font-size="12.5" font-weight="600">Full-Stack SaaS Architecture</text>
      <text x="332" y="0" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="600" text-anchor="end">96%</text>
      <rect y="8" width="332" height="6" rx="3" fill="#1e293b"/>
      <rect y="8" width="318" height="6" rx="3" fill="url(#ab-bar-grad)"/>
      <text y="26" fill="#64748b" font-size="10">Next.js 14 · React · Node.js · Express · Supabase · MongoDB</text>
    </g>

    <!-- Cap 2: Java Spring Boot & AWS -->
    <g transform="translate(24, 125)">
      <text x="0" y="0" fill="#e2e8f0" font-size="12.5" font-weight="600">Java Spring Boot &amp; AWS Cloud</text>
      <text x="332" y="0" fill="#f59e0b" font-family="{FONT_MONO}" font-size="11" font-weight="600" text-anchor="end">95%</text>
      <rect y="8" width="332" height="6" rx="3" fill="#1e293b"/>
      <rect y="8" width="315" height="6" rx="3" fill="url(#ab-bar-amber)"/>
      <text y="26" fill="#64748b" font-size="10">AWS Elastic Beanstalk · Spring Boot · Apache PDFBox/POI · LaTeX</text>
    </g>

    <!-- Cap 3: Multi-Model AI Orchestration -->
    <g transform="translate(24, 175)">
      <text x="0" y="0" fill="#e2e8f0" font-size="12.5" font-weight="600">Multi-Model AI Orchestration</text>
      <text x="332" y="0" fill="#ff758f" font-family="{FONT_MONO}" font-size="11" font-weight="600" text-anchor="end">94%</text>
      <rect y="8" width="332" height="6" rx="3" fill="#1e293b"/>
      <rect y="8" width="312" height="6" rx="3" fill="url(#ab-bar-crimson)"/>
      <text y="26" fill="#64748b" font-size="10">Groq (&lt;200ms) · OpenAI · NVIDIA · Cerebras · AssemblyAI</text>
    </g>

    <!-- Cap 4: Cross-Platform & Fintech -->
    <g transform="translate(24, 225)">
      <text x="0" y="0" fill="#e2e8f0" font-size="12.5" font-weight="600">Cross-Platform &amp; Fintech Payments</text>
      <text x="332" y="0" fill="#a78bfa" font-family="{FONT_MONO}" font-size="11" font-weight="600" text-anchor="end">92%</text>
      <rect y="8" width="332" height="6" rx="3" fill="#1e293b"/>
      <rect y="8" width="305" height="6" rx="3" fill="url(#ab-bar-grad)"/>
      <text y="26" fill="#64748b" font-size="10">Electron (Mac DMG / Win EXE) · Stripe · Razorpay · Zoho</text>
    </g>
  </g>

  <!-- RIGHT COLUMN: 3-Slide Interests Carousel (width: 400, height: 295) -->
  <g transform="translate(450, 75)">
    <rect width="400" height="295" rx="16" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>

    <!-- 3 Segment Progress Bars (Positioned cleanly at y=20) -->
    <g transform="translate(24, 20)">
      <g transform="translate(0, 0)">
        <rect width="106" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#247bff" class="ab-prog-1"/>
      </g>
      <g transform="translate(122, 0)">
        <rect width="106" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#f59e0b" class="ab-prog-2"/>
      </g>
      <g transform="translate(244, 0)">
        <rect width="106" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#ff354f" class="ab-prog-3"/>
      </g>
    </g>

    <!-- Slide 1: SaaS Factory (0s-4s) -->
    <g transform="translate(24, 46)" class="ab-slide-1">
      <rect width="180" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="0.9"/>
      <text x="12" y="16" fill="#60a5fa" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">INTEREST 01 // SAAS</text>
      
      <text x="0" y="52" fill="#ffffff" font-size="16.5" font-weight="700">Mass-Producing Production SaaS</text>
      <text x="0" y="74" fill="#38bdf8" font-size="12.5" font-style="italic">"I mass produce web apps like a factory 🏭"</text>

      <text x="0" y="104" fill="#cbd5e1" font-size="12">• Zero-to-one product builder with 20+ shipped apps</text>
      <text x="0" y="126" fill="#cbd5e1" font-size="12">• High-scale architectures on AWS, Vercel &amp; Render</text>
      <text x="0" y="148" fill="#cbd5e1" font-size="12">• Multi-tier recurring billing &amp; secure payment webhooks</text>
      <text x="0" y="170" fill="#cbd5e1" font-size="12">• Battle-tested engineering shipped with relentless speed</text>
    </g>

    <!-- Slide 2: Java & Enterprise Cloud (4s-8s) -->
    <g transform="translate(24, 46)" class="ab-slide-2">
      <rect width="210" height="24" rx="6" fill="#0e172a" stroke="#f59e0b" stroke-width="0.9"/>
      <text x="12" y="16" fill="#fbbf24" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">INTEREST 02 // JAVA &amp; AWS</text>
      
      <text x="0" y="52" fill="#ffffff" font-size="16.5" font-weight="700">Enterprise Java &amp; AWS Cloud</text>
      <text x="0" y="74" fill="#fbbf24" font-size="12.5" font-style="italic">"Scalable cloud microservices with Java Spring Boot ☁️"</text>

      <text x="0" y="104" fill="#cbd5e1" font-size="12">• Built AI Resume Tailor on AWS Elastic Beanstalk</text>
      <text x="0" y="126" fill="#cbd5e1" font-size="12">• High-throughput Spring WebClient &amp; document parsing</text>
      <text x="0" y="148" fill="#cbd5e1" font-size="12">• Dynamic fallback routing across Groq, NVIDIA &amp; Cerebras</text>
      <text x="0" y="170" fill="#cbd5e1" font-size="12">• Automated LaTeX to ATS PDF compilation pipelines</text>
    </g>

    <!-- Slide 3: AI Copilots & Cross-Platform (8s-12s) -->
    <g transform="translate(24, 46)" class="ab-slide-3">
      <rect width="195" height="24" rx="6" fill="#0e172a" stroke="#ff354f" stroke-width="0.9"/>
      <text x="12" y="16" fill="#ff758f" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">INTEREST 03 // COPILOTS</text>
      
      <text x="0" y="52" fill="#ffffff" font-size="16.5" font-weight="700">AI Copilots &amp; Cross-Platform</text>
      <text x="0" y="74" fill="#ff758f" font-size="12.5" font-style="italic">"Real-time AI that feels like a native superpower ⚡"</text>

      <text x="0" y="104" fill="#cbd5e1" font-size="12">• Founder of CHINTU AI — real-time career intelligence</text>
      <text x="0" y="126" fill="#cbd5e1" font-size="12">• Native Electron desktop apps (Mac DMG &amp; Windows EXE)</text>
      <text x="0" y="148" fill="#cbd5e1" font-size="12">• Real-time voice inference &amp; computer vision OCR</text>
      <text x="0" y="170" fill="#cbd5e1" font-size="12">• WebRTC real-time audio/video on Social Connect</text>
    </g>

    <!-- Bottom Carousel Indicator Status -->
    <g transform="translate(24, 260)">
      <text x="0" y="14" fill="#475569" font-family="{FONT_MONO}" font-size="9.5">4s INTERVAL CAROUSEL // AUTO-CYCLING</text>
    </g>
  </g>
</svg>'''

for p in [os.path.join(repo_assets, "about-life.svg"), os.path.join(local_assets, "about-life.svg")]:
    with open(p, "w", encoding="utf-8") as f:
        f.write(about_svg)

print("Updated about-life.svg with pixel-perfect alignment and zero ghosting!")

# ==============================================================================
# 2. FIX STACK.SVG: DYNAMIC BUBBLE WIDTHS WITH GUARANTEED PADDING
# ==============================================================================

# 8 slot coordinates carefully balanced on the 3 elliptical orbits
slots = [
    {"x": -140, "y": -28}, # Inner Left
    {"x": 135, "y": 28},   # Inner Right
    {"x": 0, "y": -58},     # Inner Top
    {"x": -240, "y": -42}, # Mid Left
    {"x": 95, "y": -80},   # Mid Top-Right
    {"x": -90, "y": 76},   # Mid Bottom-Left
    {"x": -335, "y": 20},  # Outer Left
    {"x": 255, "y": 44}    # Outer Right
]

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
    x, y = slot["x"], slot["y"]
    name = cfg["name"]
    color = cfg["color"]
    border = cfg["border"]
    icon_info = icons.get(cfg["icon"], {})
    
    # Calculate pill width dynamically with 16px right margin guarantee
    # 10px left-padding + 16px icon + 8px gap + text width (approx 7.8px/char) + 16px right-padding
    w = max(100, int(10 + 16 + 8 + len(name) * 7.8 + 16))
    h = 28
    half_w = w / 2
    half_h = h / 2
    
    if icon_info.get("is_multi_path"):
        icon_svg = f'''<svg x="{-half_w + 10}" y="{-8}" width="16" height="16" viewBox="0 0 256 256">'''
        for p in icon_info["paths"]:
            icon_svg += f'''<path fill="{p['fill']}" d="{p['d']}"/>'''
        icon_svg += '</svg>'
    else:
        d_path = icon_info.get("d", "")
        icon_svg = f'''<svg x="{-half_w + 10}" y="{-8}" width="16" height="16" viewBox="0 0 24 24" fill="{color}">
          <path d="{d_path}"/>
        </svg>'''
        
    return f'''
      <g transform="translate({x}, {y})">
        <rect x="{-half_w}" y="{-half_h}" width="{w}" height="{h}" rx="14" fill="#0b1224" stroke="{border}" stroke-width="1.3" stroke-opacity="0.95"/>
        {icon_svg}
        <text x="{-half_w + 34}" y="4" fill="#ffffff" font-size="11.5" font-weight="700" letter-spacing="0.2">{name}</text>
      </g>'''

def render_batch(batch_list, class_name):
    nodes_svg = ""
    for idx, item in enumerate(batch_list):
        nodes_svg += render_node(item, idx)
    return f'''<g class="{class_name}">{nodes_svg}</g>'''

b1_svg = render_batch(batch_1, "st-batch-1")
b2_svg = render_batch(batch_2, "st-batch-2")
b3_svg = render_batch(batch_3, "st-batch-3")

stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="900" height="480" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
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

    /* 15s total cycle (5s each batch with visibility toggle for clean transitions) */
    .st-batch-1 {{ animation: cycleBatch1 15s infinite ease-in-out; }}
    .st-batch-2 {{ animation: cycleBatch2 15s infinite ease-in-out; }}
    .st-batch-3 {{ animation: cycleBatch3 15s infinite ease-in-out; }}

    @keyframes cycleBatch1 {{
      0%, 28% {{ opacity: 1; visibility: visible; transform: scale(1); }}
      31%, 97% {{ opacity: 0; visibility: hidden; transform: scale(0.92); }}
      100% {{ opacity: 1; visibility: visible; transform: scale(1); }}
    }}
    @keyframes cycleBatch2 {{
      0%, 30% {{ opacity: 0; visibility: hidden; transform: scale(0.92); }}
      33%, 61% {{ opacity: 1; visibility: visible; transform: scale(1); }}
      64%, 100% {{ opacity: 0; visibility: hidden; transform: scale(0.92); }}
    }}
    @keyframes cycleBatch3 {{
      0%, 63% {{ opacity: 0; visibility: hidden; transform: scale(0.92); }}
      66%, 94% {{ opacity: 1; visibility: visible; transform: scale(1); }}
      97%, 100% {{ opacity: 0; visibility: hidden; transform: scale(0.92); }}
    }}

    /* Progress Segment Bars */
    .st-bar-1 {{ animation: stBarFill1 15s infinite linear; }}
    .st-bar-2 {{ animation: stBarFill2 15s infinite linear; }}
    .st-bar-3 {{ animation: stBarFill3 15s infinite linear; }}

    @keyframes stBarFill1 {{
      0% {{ width: 0px; }}
      28%, 99% {{ width: 85px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes stBarFill2 {{
      0%, 33% {{ width: 0px; }}
      61%, 99% {{ width: 85px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes stBarFill3 {{
      0%, 66% {{ width: 0px; }}
      94%, 99% {{ width: 85px; }}
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
    
    <!-- Rotating Header Indicator with visibility safety -->
    <g class="st-batch-1">
      <text x="185" y="16" fill="#94a3b8" font-family="{FONT_MONO}" font-size="10.5">BATCH 01 // CORE ARCHITECTURE (NEXT.JS · REACT · JAVA · AWS · NODE)</text>
    </g>
    <g class="st-batch-2">
      <text x="185" y="16" fill="#34d399" font-family="{FONT_MONO}" font-size="10.5">BATCH 02 // FRAMEWORKS &amp; DATABASES (TAILWIND · ANGULAR · POSTGRES · MONGO)</text>
    </g>
    <g class="st-batch-3">
      <text x="185" y="16" fill="#f43f5e" font-family="{FONT_MONO}" font-size="10.5">BATCH 03 // AI, FINTECH &amp; ECOSYSTEM (OPENAI · GEMINI · STRIPE · DOCKER)</text>
    </g>

    <!-- 3 Batch Segment Progress Bars -->
    <g transform="translate(605, 8)">
      <g transform="translate(0, 0)">
        <rect width="70" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#38bdf8" class="st-bar-1"/>
      </g>
      <g transform="translate(78, 0)">
        <rect width="70" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#34d399" class="st-bar-2"/>
      </g>
      <g transform="translate(156, 0)">
        <rect width="70" height="4" rx="2" fill="#1e293b"/>
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

    <!-- 3 ROTATING BATCHES WITH DYNAMIC PILL WIDTHS & AUTHENTIC LOGOS -->
    {b1_svg}
    {b2_svg}
    {b3_svg}
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

for p in [os.path.join(repo_assets, "stack.svg"), os.path.join(local_assets, "stack.svg")]:
    with open(p, "w", encoding="utf-8") as f:
        f.write(stack_svg)

print("Updated stack.svg with dynamic bubble widths and generous margins!")
