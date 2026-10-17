import json
import os

repo_dir = r"D:\Desktop\Projects\Abhishek6827"
local_assets_dir = r"D:\Desktop\Resume-Extension\profile-assets"

# Load icons
with open(os.path.join(local_assets_dir, "icons_data.json")) as f:
    icons = json.load(f)

FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"

# ==============================================================================
# 1. FIX STACK.SVG: ELIMINATE TOP LINE & PROGRESS BARS OVERLAP
# ==============================================================================
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

    /* 15s cycle: 5s per batch with clean visibility switching */
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
      28%, 99% {{ width: 65px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes stBarFill2 {{
      0%, 33% {{ width: 0px; }}
      61%, 99% {{ width: 65px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes stBarFill3 {{
      0%, 66% {{ width: 0px; }}
      94%, 99% {{ width: 65px; }}
      100% {{ width: 0px; }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="480" rx="20" fill="#070b16"/>
  <rect width="900" height="480" fill="url(#st-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="478.5" rx="19.25" fill="none" stroke="url(#st-border)" stroke-width="1.5"/>

  <!-- Top Header Title: Short clean titles + Right-aligned progress bars (NO OVERLAP) -->
  <g transform="translate(50, 34)">
    <rect width="170" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="85" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      02 // TECH ARSENAL
    </text>
    
    <!-- Short titles that end around x=420 (leaving a massive 200px gap before progress bars!) -->
    <g class="st-batch-1">
      <text x="185" y="16" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11">BATCH 01 // CORE ARCHITECTURE &amp; CLOUD</text>
    </g>
    <g class="st-batch-2">
      <text x="185" y="16" fill="#34d399" font-family="{FONT_MONO}" font-size="11">BATCH 02 // FRAMEWORKS &amp; DATABASES</text>
    </g>
    <g class="st-batch-3">
      <text x="185" y="16" fill="#f43f5e" font-family="{FONT_MONO}" font-size="11">BATCH 03 // AI, FINTECH &amp; ECOSYSTEM</text>
    </g>

    <!-- 3 Batch Segment Progress Bars (Anchored at x=590 to x=800, 170px away from text) -->
    <g transform="translate(580, 10)">
      <g transform="translate(0, 0)">
        <rect width="65" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#38bdf8" class="st-bar-1"/>
      </g>
      <g transform="translate(73, 0)">
        <rect width="65" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#34d399" class="st-bar-2"/>
      </g>
      <g transform="translate(146, 0)">
        <rect width="65" height="4" rx="2" fill="#1e293b"/>
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

for p in [os.path.join(repo_dir, "assets", "stack.svg"), os.path.join(local_assets_dir, "stack.svg")]:
    with open(p, "w", encoding="utf-8") as f:
        f.write(stack_svg)

print("Regenerated stack.svg with non-overlapping header!")

# ==============================================================================
# 2. ASSEMBLE ZERO-DUPLICATION UNIFIED README.MD
# ==============================================================================
# In this unified README:
# - Starts directly with the 5 animated SVGs
# - Quick action buttons with PROFILE VIEWS counter below connect.svg
# - NO duplicate About Me (already presented in Hero & About-life SVGs)
# - NO duplicate Tech Arsenal wall (already presented in Stack SVG)
# - NO duplicate Connect buttons (already presented below connect.svg)
# - Clean Battle Log (Work history)
# - 4 Shipped Flagship Projects (with Resume Tailor at #2) + More Projects table
# - Developer Stats & Activity (Streaks, Overall Stats, Trophies, Activity Graph, Contribution Snake)
# - Certifications Table
# - Signature Footer

unified_readme = '''<div align="center">

<!-- ANIMATED SVG 01: HERO -->
<img src="./assets/hero.svg?v=1" alt="Abhishek Tiwari — Hero Profile" width="100%" />

<br/><br/>

<!-- ANIMATED SVG 02: ABOUT & CAPABILITIES CAROUSEL -->
<img src="./assets/about-life.svg?v=2" alt="Abhishek Tiwari — Capabilities & Life Carousel" width="100%" />

<br/><br/>

<!-- ANIMATED SVG 03: TECH ARSENAL ORBITS -->
<img src="./assets/stack.svg?v=4" alt="Abhishek Tiwari — Tech Arsenal Orbit" width="100%" />

<br/><br/>

<!-- ANIMATED SVG 04: ID BADGE & VERIFIED METRICS -->
<img src="./assets/id-dashboard.svg?v=1" alt="Abhishek Tiwari — ID Badge & Credentials Dashboard" width="100%" />

<br/><br/>

<!-- ANIMATED SVG 05: CONNECT & SOCIAL CTA -->
<img src="./assets/connect.svg?v=1" alt="Connect with Abhishek Tiwari" width="100%" />

<br/>

<!-- REAL CLICKABLE SOCIAL BUTTONS + PROFILE VIEWS COUNTER -->
<a href="https://www.linkedin.com/in/abhishek-tiwariiii"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;
<a href="https://portfolio.getchintu.com"><img src="https://img.shields.io/badge/Portfolio-Visit_Live-6366f1?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>&nbsp;
<a href="https://getchintu.com"><img src="https://img.shields.io/badge/CHINTU_AI-Live_Platform-8B5CF6?style=for-the-badge&logo=rocket&logoColor=white" /></a>&nbsp;
<a href="https://github.com/Abhishek6827"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;
<a href="mailto:abhishektiwari@getchintu.com"><img src="https://img.shields.io/badge/Gmail-Hire_Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>&nbsp;
<img src="https://komarev.com/ghpvc/?username=Abhishek6827&style=for-the-badge&color=a855f7&label=👁️+PROFILE+VIEWS" alt="Profile Views" />

</div>

---

## 💼 Battle Log (Experience)

### ⚡ Full-Stack Developer
**CHINTU AI** · `📅 02/2026 – Present`

<img src="https://skillicons.dev/icons?i=nextjs,electron,supabase" width="42" />&nbsp;&nbsp;Building **CHINTU AI** — AI Career Platform for Interviews, Assessments &amp; Resume Tailoring | Real-Time AI Copilot. Electron desktop app (Windows/Mac DMG) + Android APK + Next.js web platform. Multi-model LLM orchestration (Alibaba, OpenAI, Groq). Razorpay billing with 3-tier subscriptions. AI-powered practice sessions, voice input, technical assessment tools, and 63+ language support. Auto-updater pipeline with GitHub Releases.

---

### <img src="https://skillicons.dev/icons?i=nextjs" width="18" /> Full Stack Developer
**Indian Capital &amp; Investment (Coimbatore) Ltd.** · `📅 11/2025 – 02/2026`

<img src="https://skillicons.dev/icons?i=nextjs,firebase" width="28" />&nbsp;&nbsp;Stripe &amp; Zoho payment gateways · Next.js + Firebase backend · Automated webhooks &amp; Resend notifications · Notion API workflow automation

---

### <img src="https://skillicons.dev/icons?i=react" width="18" /> Software Developer
**Vasnaani Education** · `📅 08/2024 – 10/2025`

<img src="https://skillicons.dev/icons?i=react,django" width="28" />&nbsp;&nbsp;Official website development · Django REST API + React integration · Performance optimization · Critical UI/UX bug resolution

---

### <img src="https://skillicons.dev/icons?i=django" width="18" /> Full-Stack Developer Intern
**Hoping Minds** · `📅 01/2024 – 06/2024`

<img src="https://skillicons.dev/icons?i=react,redux,django" width="42" />&nbsp;&nbsp;React + Redux + Django apps · Cross-functional team delivery · Responsive design · Clean code practices

---

### <img src="https://skillicons.dev/icons?i=js" width="18" /> Web Developer
**Quizario** · `📅 11/2023 – 12/2023`

<img src="https://skillicons.dev/icons?i=react,js,bootstrap" width="42" />&nbsp;&nbsp;Interactive quiz applications · User authentication · Data management features · UX optimization

---

## 🚀 Shipped &amp; Deployed Flagship Projects

### ⚡ 01. CHINTU AI — AI Career Platform &amp; Real-Time Copilot &nbsp; [**LIVE ↗**](https://getchintu.com)

<img src="https://skillicons.dev/icons?i=nextjs,ts,electron,supabase,tailwind,nodejs&perline=10" />

<br/>

<img src="https://getchintu.com/5.png" width="70%" alt="CHINTU AI Interface" />

> AI-powered career prep platform for **interviews**, **assessments**, and **resume tailoring**. Multi-model intelligence, voice input, technical assessment tools, and 63+ language support. Cross-platform — Desktop (Electron · Windows/Mac DMG), Android APK, and Web with Razorpay billing, auto-updater, and intelligent answer synthesis.

<details>
<summary><b>📋 Full Feature List &amp; Architecture (click to expand)</b></summary>

**🤖 Multi-Model AI Engine**
- **Standard Engine** — Balanced responses for general practice questions
- **Pro Engine** — Detailed, contextual answers with memory
- **Coding Engine** — Specialized for DSA, system design, and technical assessments
- **Turbo Engine (Elite)** — Ultra-low-latency answers (&lt;200ms) via Groq
- **Scout + Turbo** — Deep analysis with verified fixes for technical problems

**🎙️ Voice &amp; Input**
- Hold-Space voice input with instant AI synthesis
- Vision OCR — analyze any question image and get structured answers
- Minimizable assistant panel for focused practice sessions
- Universal keyboard shortcuts across all platforms

**💳 Billing &amp; Plans**
- **Starter** — Free tier with 10 credits/month
- **Professional** — 100 credits/month, all premium engines
- **Elite** — 500 credits/month, Turbo Engine, screen recording, dedicated support
- Razorpay integration with webhook-driven credit management

**🏗️ Architecture**
- **Frontend:** Next.js 14 + TypeScript + Tailwind CSS + Framer Motion
- **Desktop:** Electron with auto-updater, native protocols, system tray
- **Backend:** Next.js API Routes + Express microservices
- **Database:** Supabase + SQLite (local)
- **AI:** Alibaba + OpenAI + Groq + AssemblyAI
- **Payments:** Razorpay with webhook verification
- **Languages:** 63+ international locales
- **Deployment:** Vercel (web) + GitHub Releases (Electron auto-updater)

</details>

---

### 📄 02. AI Resume Tailor &amp; LaTeX Engine (AWS + Java Spring Boot) &nbsp; [**SOURCE REPO ↗**](https://github.com/Abhishek6827/Resume-Extension)

<img src="https://skillicons.dev/icons?i=java,spring,aws,nextjs,ts,tailwind&perline=10" />

> Cloud-native, AI-driven resume tailoring platform that customizes resumes for specific job descriptions. Features high-throughput **Java Spring Boot backend deployed on AWS Elastic Beanstalk**, multi-provider LLM fallback routing, document parsing, and LaTeX PDF compilation.

<details>
<summary><b>📋 Full Feature List &amp; Architecture (click to expand)</b></summary>

**☁️ AWS Cloud &amp; Java Spring Boot Backend**
- **Cloud Hosting:** Deployed on **AWS Elastic Beanstalk** (Single Instance Corretto 17 environment)
- **Backend Framework:** **Java 17/21 with Spring Boot**, structured with clean separation of services, controllers, and config
- **Spring WebClient:** High-throughput non-blocking asynchronous REST communication with LLM providers
- **Dynamic Port &amp; Environment Management:** Native integration with AWS environment variables (`SERVER_PORT=5000`)

**🧠 Multi-Provider AI Fallback Routing**
- Highly resilient fallback matrix across **Groq**, **Cerebras**, **NVIDIA**, and **OpenRouter**
- Bypasses rate limits and ensures sub-second response times for deep prompt engineering
- Context-aware bullet point rewrites strictly matching job descriptions while preserving truthfulness

**📄 Document Parsing &amp; LaTeX PDF Compilation**
- **Apache PDFBox** for robust PDF text extraction and metadata processing
- **Apache POI** for DOCX parsing and structural layout extraction
- **TexLive API Integration:** Automatic compilation into beautiful, ATS-compliant LaTeX templates
- Instant downloadable PDF output with pixel-perfect typography

**🧩 Chrome Extension &amp; Modern Frontend**
- Chrome Extension side-panel UI built with **Next.js**, **React**, and **TypeScript**
- Sleek glassmorphism aesthetic with responsive Tailwind CSS
- Real-time status sync between extension panel and AWS Spring Boot API

</details>

---

### 🟣 03. Social Connect — Full-Stack Real-Time Social Platform &nbsp; [**LIVE ↗**](https://socialconnect.getchintu.com/login)

<img src="https://skillicons.dev/icons?i=angular,ts,express,nodejs,mongodb&perline=10" />

> Full-stack social media application with **real-time chat**, **WebRTC video/audio calls**, and a rich messaging system.

<details>
<summary><b>📋 Full Feature List &amp; Architecture (click to expand)</b></summary>

**💬 Real-Time Chat (Socket.io)**
- Text, image, audio, voice &amp; file message types
- Emoji reactions on messages (add/remove per user)
- Message editing (10-min window) &amp; deletion with real-time sync
- Read receipts &amp; read timestamps
- Typing indicators (start/stop)
- Online/offline presence tracking with `lastSeen`
- Unread message count per chat

**📞 WebRTC Audio &amp; Video Calls**
- Peer-to-peer audio &amp; video calls with ICE candidate exchange
- Call initiation, accept, reject, and end signaling via Socket.io
- Caller avatar &amp; name display on incoming call UI

**🔐 Authentication**
- JWT-based auth with bcrypt password hashing
- Google OAuth 2.0 &amp; Facebook OAuth via Passport.js
- Email verification with token expiration (Brevo/Sendinblue)
- Remembered users &amp; session persistence
- Auth guards on client routes

**👤 User Profiles**
- Avatar &amp; cover image uploads (Multer)
- Bio, location, website, follower/following counts
- User search by username
- Profile pages with activity feed

**🏗️ Architecture**
- **Frontend:** Angular 17 with Material UI, RxJS, infinite scroll
- **Backend:** Express.js + TypeScript, Helmet security, compression, Morgan logging
- **Database:** MongoDB with Mongoose ODM
- **Real-time:** Socket.io with JWT-authenticated connections
- **Deployment:** Vercel (client) + Render (server)

**📱 Pages:** Feed, Explore, Friends, Groups, Events, Chat, Profile, Dashboard

</details>

---

### 🔴 04. YouTube Automation — AI-Powered Automated YouTube Upload Pipeline &nbsp; [**LIVE ↗**](https://yt-automation-beta.vercel.app/)

<img src="https://skillicons.dev/icons?i=nextjs,ts,prisma,postgres,tailwind&perline=10" />

> Automated end-to-end YouTube content workflow: **Google Drive → AI Metadata → Scheduled YouTube Upload** with copyright protection.

<details>
<summary><b>📋 Full Feature List &amp; Architecture (click to expand)</b></summary>

**🤖 AI-Powered Metadata Generation (3-tier system)**
- **Tier 1 — Audio Transcription:** AssemblyAI extracts transcript → Gemini 2.0 Flash generates title/description/tags from spoken content
- **Tier 2 — Visual Analysis:** FFmpeg extracts video frames → Gemini Vision analyzes scenes → generates metadata from visuals
- **Tier 3 — Filename Fallback:** Gemini generates viral metadata from filename with randomized styles (suspense, comedy, motivational, etc.)
- Enforces YouTube limits (title ≤100 chars, tags ≤500 chars total)

**📁 Google Drive Integration**
- Folder scan &amp; single-file link support via Google Drive API
- Auto-detect folders vs individual video files
- Skip already-processed videos (deduplication)
- Download video streams for upload &amp; frame extraction

**📤 YouTube Upload &amp; Scheduling**
- Automated upload via YouTube Data API v3
- Configurable schedule: upload hour + videos per day per job
- Privacy control: public, unlisted, or private
- Scheduled publishing with `publishAt` timestamp
- Quota error detection &amp; handling

**🛡️ Copyright Safety System**
- Post-upload copyright claim detection (polling up to 2 min)
- Auto-revert to private if restrictions found
- Copyright logs with claim type, status &amp; details
- Region restriction detection

**⚙️ Automation Jobs**
- Multi-job support: multiple Drive folders → one YouTube channel
- Per-job scheduling (independent upload hours &amp; daily limits)
- Enable/disable individual jobs
- Cron-based daily automation (`node-cron`)
- Draft/preview workflow before committing to upload

**🔐 Authentication**
- NextAuth v5 (Auth.js) with Google OAuth
- Prisma Adapter for session persistence
- Multi-user support: isolated videos, folders, settings &amp; jobs

**🏗️ Architecture**
- **Frontend:** Next.js 16 (App Router) + TypeScript + Tailwind CSS + Radix UI
- **Backend:** Next.js API Routes (17 endpoints: ai, auth, automation, channel, cron, drive, proxy, settings, videos)
- **Database:** PostgreSQL with Prisma ORM (7 models)
- **AI:** Google Generative AI (Gemini 2.0 Flash) + AssemblyAI
- **Video Processing:** FFmpeg (frame extraction) via fluent-ffmpeg
- **Deployment:** Vercel with Speed Insights

</details>

---

### 📦 More Projects

<div align="center">

| # | Project | What it does | Stack | Link |
|:-:|---------|-------------|-------|:----:|
| 🟠 | **Tempusmail** | Disposable email service, real-time | <img src="https://skillicons.dev/icons?i=nextjs,firebase,tailwind" width="48" /> | [**LIVE ↗**](https://tempomail.getchintu.com) |
| 🩷 | **Myntra Clone** | Fashion e-commerce platform | <img src="https://skillicons.dev/icons?i=react,redux,css" width="48" /> | [**LIVE ↗**](https://Abhishek6827.github.io/Myntra/) |
| 🔵 | **Kanban WorkBoard** | Project management + Django backend | <img src="https://skillicons.dev/icons?i=django,react,redux,tailwind" width="64" /> | [**LIVE ↗**](https://Abhishek6827.github.io/Kanban_WorkBoard/) |
| 🟡 | **Market Explorer** | Seasonal market trend calendar | <img src="https://skillicons.dev/icons?i=react,tailwind" width="32" /> | [**LIVE ↗**](https://abhishek6827.github.io/Market-Seasonality-Explorer/) |
| 🟢 | **Skill Up** | Online learning platform | <img src="https://skillicons.dev/icons?i=react,firebase" width="32" /> | [**LIVE ↗**](https://Abhishek6827.github.io/Skill_Up/) |
| 🟣 | **Elante Mall** | Shopping mall directory | <img src="https://skillicons.dev/icons?i=react,css,js" width="48" /> | [**LIVE ↗**](https://Abhishek6827.github.io/Elante_Mall/) |

<br/>

<a href="https://abhishek6827.github.io/Portfolio/"><img src="https://img.shields.io/badge/Explore_All_Projects_%E2%86%92-6366F1?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>

</div>

---

## 📊 Stats That Speak

<div align="center">

<img width="49%" src="https://github-readme-stats-7ihy.vercel.app/api?username=Abhishek6827&show_icons=true&theme=radical&hide_border=true&bg_color=0d1117&title_color=a855f7&icon_color=a855f7&text_color=c9d1d9&count_private=true&rank_icon=github" />
<img width="49%" src="https://github-readme-streak-stats-eight.vercel.app?user=Abhishek6827&theme=radical&hide_border=true&background=0d1117&ring=a855f7&fire=a855f7&currStreakLabel=a855f7" />

<br/>
<!-- GitHub Trophies — Bottom 4 hidden to show only top performers -->
<img src="https://github-profile-trophy-orpin-alpha.vercel.app/?username=Abhishek6827&theme=radical&no-frame=true&no-bg=true&column=4&row=1&margin-w=10&margin-h=10&hidden=Reviews,Followers,Issues,PullRequest" width="100%" />

<br/>

<!-- Activity Graph -->
<img src="https://github-readme-activity-graph.vercel.app/graph?username=Abhishek6827&custom_title=Abhishek's+Contribution+Graph&bg_color=0d1117&color=a855f7&line=6366f1&point=a855f7&area_color=6366f1&area=true&hide_border=true" width="98%" />

<br/>

<!-- Contribution Snake Animation -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake.svg" />
  <img alt="github-snake" src="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake.svg" />
</picture>

</div>

---

## 🏆 Certifications

<div align="center">

| 🥇 | Certification | Issuer | Year |
|:--:|---------------|--------|:----:|
| <img src="https://img.shields.io/badge/Meta-0668E1?style=flat-square&logo=meta&logoColor=white" /> | **React Developer Certification** | Meta | `2025` |
| <img src="https://img.shields.io/badge/FCC-0A0A23?style=flat-square&logo=freecodecamp&logoColor=white" /> | **Full Stack Web Development** | FreeCodeCamp | `2024` |
| <img src="https://img.shields.io/badge/FCC-0A0A23?style=flat-square&logo=freecodecamp&logoColor=white" /> | **JS Algorithms &amp; Data Structures** | FreeCodeCamp | `2023` |

</div>

---

<div align="center">

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" width="70%" />

<br/><br/>

> ⚡ *"Crafting digital experiences with modern web technologies. Passionate about creating scalable solutions that make a difference."*

</div>
'''

for p in [os.path.join(repo_dir, "Readme.md"), os.path.join(local_assets_dir, "README.md")]:
    with open(p, "w", encoding="utf-8") as f:
        f.write(unified_readme)

print("Unified Readme.md successfully assembled without any duplicate sections!")
