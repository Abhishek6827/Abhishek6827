import base64
import os
import io
import zipfile
from PIL import Image

def get_optimized_b64(path):
    img = Image.open(path)
    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('ascii')

# Source image paths
id_png_path = r"C:\Users\Abhishek\Downloads\id.png"
pointing_png_path = r"C:\Users\Abhishek\Downloads\right_pointing.png"

id_b64 = get_optimized_b64(id_png_path)
pointing_b64 = get_optimized_b64(pointing_png_path)

output_dir = r"D:\Desktop\Projects\Abhishek6827\assets"
repo_dir = r"D:\Desktop\Projects\Abhishek6827"
os.makedirs(output_dir, exist_ok=True)

# Also save to profile-assets locally in workspace
local_assets_dir = r"D:\Desktop\Resume-Extension\profile-assets"
os.makedirs(local_assets_dir, exist_ok=True)

FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"

# ==============================================================================
# 1. HERO.SVG
# ==============================================================================
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="900" height="420" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="hero-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="hero-name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#93c5fd"/>
      <stop offset="100%" stop-color="#247bff"/>
    </linearGradient>
    <linearGradient id="hero-card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e172a" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0.95"/>
    </linearGradient>
    <radialGradient id="hero-glow-blue" cx="15%" cy="20%" r="40%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-glow-crimson" cx="85%" cy="80%" r="40%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="hero-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
    <clipPath id="hero-name-clip">
      <rect x="50" y="115" width="500" height="60"/>
    </clipPath>
    <clipPath id="hero-portrait-clip">
      <rect x="590" y="45" width="260" height="330" rx="18"/>
    </clipPath>
  </defs>

  <style>
    @media (prefers-reduced-motion: reduce) {{
      .hero-anim {{ animation: none !important; }}
    }}
    .hero-pulse {{
      animation: heroPulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }}
    @keyframes heroPulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.9); }}
    }}
    .hero-role {{
      font-family: {FONT_MONO};
      font-size: 15px;
      font-weight: 600;
      fill: #38bdf8;
    }}
    .hero-role-1 {{ animation: cycleRole1 12s infinite; }}
    .hero-role-2 {{ animation: cycleRole2 12s infinite; }}
    .hero-role-3 {{ animation: cycleRole3 12s infinite; }}
    .hero-role-4 {{ animation: cycleRole4 12s infinite; }}

    @keyframes cycleRole1 {{
      0%, 22% {{ opacity: 1; transform: translateY(0); }}
      25%, 97% {{ opacity: 0; transform: translateY(-8px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes cycleRole2 {{
      0%, 22% {{ opacity: 0; transform: translateY(8px); }}
      25%, 47% {{ opacity: 1; transform: translateY(0); }}
      50%, 100% {{ opacity: 0; transform: translateY(-8px); }}
    }}
    @keyframes cycleRole3 {{
      0%, 47% {{ opacity: 0; transform: translateY(8px); }}
      50%, 72% {{ opacity: 1; transform: translateY(0); }}
      75%, 100% {{ opacity: 0; transform: translateY(-8px); }}
    }}
    @keyframes cycleRole4 {{
      0%, 72% {{ opacity: 0; transform: translateY(8px); }}
      75%, 97% {{ opacity: 1; transform: translateY(0); }}
      100% {{ opacity: 0; transform: translateY(-8px); }}
    }}

    .hero-float {{
      animation: heroFloat 5s ease-in-out infinite;
    }}
    @keyframes heroFloat {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-6px); }}
    }}
    .hero-rising-name {{
      animation: heroNameRise 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    @keyframes heroNameRise {{
      from {{ transform: translateY(50px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="420" rx="20" fill="#070b16"/>
  <rect width="900" height="420" fill="url(#hero-glow-blue)"/>
  <rect width="900" height="420" fill="url(#hero-glow-crimson)"/>
  <rect width="900" height="420" fill="url(#hero-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="418.5" rx="19.25" fill="none" stroke="url(#hero-border)" stroke-width="1.5"/>

  <!-- Left Column -->
  <g transform="translate(0, 0)">
    <!-- Status Pill -->
    <g transform="translate(50, 42)">
      <rect width="250" height="28" rx="14" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.6"/>
      <circle cx="16" cy="14" r="4.5" fill="#22c55e" class="hero-pulse"/>
      <circle cx="16" cy="14" r="8" fill="#22c55e" opacity="0.25"/>
      <text x="32" y="18" fill="#93c5fd" font-family="{FONT_MONO}" font-size="11" font-weight="600" letter-spacing="1">SYSTEM ONLINE // CHINTU AI</text>
    </g>

    <!-- Typed Greeting -->
    <text x="50" y="105" fill="#94a3b8" font-family="{FONT_MONO}" font-size="15" font-weight="500" letter-spacing="1.5">
      &gt; HELLO WORLD, I'M <tspan fill="#ff354f">_</tspan>
    </text>

    <!-- Rising Name Reveal -->
    <g clip-path="url(#hero-name-clip)">
      <text x="50" y="165" fill="url(#hero-name-grad)" font-size="44" font-weight="800" letter-spacing="-0.5" class="hero-rising-name">
        ABHISHEK TIWARI
      </text>
    </g>

    <!-- Cycling 4 Roles (with fallback static visibility) -->
    <g transform="translate(50, 208)">
      <rect x="0" y="-18" width="480" height="32" rx="8" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <g class="hero-role hero-role-1">
        <text x="14" y="3" fill="#60a5fa">⚡ Founder &amp; Full-Stack Dev @ CHINTU AI</text>
      </g>
      <g class="hero-role hero-role-2">
        <text x="14" y="3" fill="#38bdf8">☕ Java &amp; AWS Cloud Architect (Spring Boot)</text>
      </g>
      <g class="hero-role hero-role-3">
        <text x="14" y="3" fill="#ff758f">🤖 Multi-Model AI Orchestrator &amp; Systems Engineer</text>
      </g>
      <g class="hero-role hero-role-4">
        <text x="14" y="3" fill="#a78bfa">🖥️ Cross-Platform Builder (Electron · Next.js · APK)</text>
      </g>
    </g>

    <!-- Pitch Text -->
    <text x="50" y="260" fill="#cbd5e1" font-size="14.5" font-weight="400" line-height="1.6">
      Crafting scalable SaaS, Java/Spring cloud backends on AWS, and low-latency
    </text>
    <text x="50" y="282" fill="#94a3b8" font-size="14" font-weight="400">
      AI platforms. <tspan fill="#f1f5f9" font-weight="600">20+ production apps shipped &amp; deployed.</tspan>
    </text>

    <!-- Metadata Pill Row -->
    <g transform="translate(50, 325)">
      <!-- Location Pill -->
      <g transform="translate(0, 0)">
        <rect width="145" height="32" rx="8" fill="#0d1527" stroke="#1e293b" stroke-width="1"/>
        <text x="12" y="20" fill="#94a3b8" font-size="12">📍 Lucknow, India 🇮🇳</text>
      </g>
      <!-- Experience Pill -->
      <g transform="translate(155, 0)">
        <rect width="145" height="32" rx="8" fill="#0d1527" stroke="#1e293b" stroke-width="1"/>
        <text x="12" y="20" fill="#94a3b8" font-size="12">🚀 20+ Production Apps</text>
      </g>
      <!-- Education Pill -->
      <g transform="translate(310, 0)">
        <rect width="175" height="32" rx="8" fill="#0d1527" stroke="#1e293b" stroke-width="1"/>
        <text x="12" y="20" fill="#94a3b8" font-size="12">🎓 Postgrad in Comp App</text>
      </g>
    </g>
  </g>

  <!-- Right Column: Character Portrait Frame -->
  <g class="hero-float">
    <!-- Frame Glow Backing -->
    <rect x="588" y="43" width="264" height="334" rx="20" fill="none" stroke="url(#hero-border)" stroke-width="2"/>
    <rect x="590" y="45" width="260" height="330" rx="18" fill="url(#hero-card-grad)"/>

    <!-- Subtle Technical Grid Lines -->
    <line x1="590" y1="80" x2="850" y2="80" stroke="#1e293b" stroke-width="0.8" stroke-dasharray="4 4"/>
    <line x1="590" y1="335" x2="850" y2="335" stroke="#1e293b" stroke-width="0.8" stroke-dasharray="4 4"/>

    <!-- Corner Brackets -->
    <path d="M 598 57 L 598 50 L 605 50" fill="none" stroke="#247bff" stroke-width="1.8"/>
    <path d="M 842 57 L 842 50 L 835 50" fill="none" stroke="#247bff" stroke-width="1.8"/>
    <path d="M 598 363 L 598 370 L 605 370" fill="none" stroke="#ff354f" stroke-width="1.8"/>
    <path d="M 842 363 L 842 370 L 835 370" fill="none" stroke="#ff354f" stroke-width="1.8"/>

    <!-- Top Badge -->
    <text x="608" y="66" fill="#64748b" font-family="{FONT_MONO}" font-size="9.5" letter-spacing="1">ID // AT-6827</text>
    <circle cx="830" cy="62" r="3.5" fill="#247bff"/>

    <!-- Character Image (Inlined Base64 Alpha PNG) -->
    <g clip-path="url(#hero-portrait-clip)">
      <image href="data:image/png;base64,{id_b64}" x="575" y="45" width="290" height="290" preserveAspectRatio="xMidYMid meet"/>
    </g>

    <!-- Bottom Tag on Card -->
    <g transform="translate(615, 345)">
      <rect width="210" height="22" rx="6" fill="#070b16" stroke="#247bff" stroke-width="1" stroke-opacity="0.6"/>
      <text x="105" y="15" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="700" text-anchor="middle" letter-spacing="1.2">
        FULL-STACK SAAS BUILDER
      </text>
    </g>
  </g>
</svg>'''

with open(os.path.join(output_dir, "hero.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)
with open(os.path.join(local_assets_dir, "hero.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)

print("Updated hero.svg")

# ==============================================================================
# 2. ABOUT-LIFE.SVG
# ==============================================================================
about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 390" width="900" height="390" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="ab-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.6"/>
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
    .ab-slide-1 {{ animation: slideFade1 12s infinite; }}
    .ab-slide-2 {{ animation: slideFade2 12s infinite; }}
    .ab-slide-3 {{ animation: slideFade3 12s infinite; }}

    @keyframes slideFade1 {{
      0%, 30% {{ opacity: 1; transform: translateY(0); }}
      33%, 97% {{ opacity: 0; transform: translateY(8px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes slideFade2 {{
      0%, 30% {{ opacity: 0; transform: translateY(8px); }}
      33%, 63% {{ opacity: 1; transform: translateY(0); }}
      66%, 100% {{ opacity: 0; transform: translateY(8px); }}
    }}
    @keyframes slideFade3 {{
      0%, 63% {{ opacity: 0; transform: translateY(8px); }}
      66%, 97% {{ opacity: 1; transform: translateY(0); }}
      100% {{ opacity: 0; transform: translateY(8px); }}
    }}

    .ab-prog-1 {{ animation: progFill1 12s infinite linear; }}
    .ab-prog-2 {{ animation: progFill2 12s infinite linear; }}
    .ab-prog-3 {{ animation: progFill3 12s infinite linear; }}

    @keyframes progFill1 {{
      0% {{ width: 0px; }}
      30%, 99% {{ width: 112px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes progFill2 {{
      0%, 33% {{ width: 0px; }}
      63%, 99% {{ width: 112px; }}
      100% {{ width: 0px; }}
    }}
    @keyframes progFill3 {{
      0%, 66% {{ width: 0px; }}
      97%, 99% {{ width: 112px; }}
      100% {{ width: 0px; }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="390" rx="20" fill="#070b16"/>
  <rect width="900" height="390" fill="url(#ab-glow)"/>
  <rect width="900" height="390" fill="url(#ab-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="388.5" rx="19.25" fill="none" stroke="url(#ab-border)" stroke-width="1.5"/>

  <!-- Top Header Title -->
  <g transform="translate(50, 42)">
    <rect width="180" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="90" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      01 // CAPABILITIES &amp; LIFE
    </text>
    <text x="200" y="17" fill="#64748b" font-family="{FONT_MONO}" font-size="11">ENGINEERING CORE + LIFE PHILOSOPHY</text>
  </g>

  <!-- LEFT COLUMN: Engineering Capabilities (width: 380) -->
  <g transform="translate(50, 80)">
    <rect width="380" height="275" rx="16" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
    
    <!-- Title -->
    <text x="24" y="34" fill="#f8fafc" font-size="15" font-weight="700">Production Capabilities</text>
    <text x="24" y="52" fill="#64748b" font-family="{FONT_MONO}" font-size="10.5">VERIFIED DOMAINS &amp; ARCHITECTURAL STRENGTH</text>

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

  <!-- RIGHT COLUMN: 3-Slide Interests Carousel (width: 410) -->
  <g transform="translate(450, 80)">
    <rect width="400" height="275" rx="16" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>

    <!-- 3 Segment Progress Bars -->
    <g transform="translate(24, 24)">
      <g transform="translate(0, 0)">
        <rect width="112" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#247bff" class="ab-prog-1"/>
      </g>
      <g transform="translate(120, 0)">
        <rect width="112" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#f59e0b" class="ab-prog-2"/>
      </g>
      <g transform="translate(240, 0)">
        <rect width="112" height="4" rx="2" fill="#1e293b"/>
        <rect width="0" height="4" rx="2" fill="#ff354f" class="ab-prog-3"/>
      </g>
    </g>

    <!-- Slide 1: SaaS Factory (0s-4s) -->
    <g transform="translate(24, 52)" class="ab-slide-1">
      <rect width="150" height="22" rx="5" fill="#0e172a" stroke="#247bff" stroke-width="0.8"/>
      <text x="12" y="15" fill="#60a5fa" font-family="{FONT_MONO}" font-size="10" font-weight="700">INTEREST 01 // SAAS</text>
      
      <text x="0" y="48" fill="#ffffff" font-size="17" font-weight="700">Mass-Producing Production SaaS</text>
      <text x="0" y="70" fill="#38bdf8" font-size="12.5" font-style="italic">"I mass produce web apps like a factory 🏭"</text>

      <text x="0" y="102" fill="#cbd5e1" font-size="12.5">• Zero-to-one product builder with 20+ shipped apps</text>
      <text x="0" y="124" fill="#cbd5e1" font-size="12.5">• High-scale architectures on AWS, Vercel &amp; Render</text>
      <text x="0" y="146" fill="#cbd5e1" font-size="12.5">• Multi-tier recurring billing &amp; secure payment webhooks</text>
      <text x="0" y="168" fill="#cbd5e1" font-size="12.5">• Battle-tested engineering shipped with relentless speed</text>
    </g>

    <!-- Slide 2: Java & Enterprise Cloud (4s-8s) -->
    <g transform="translate(24, 52)" class="ab-slide-2">
      <rect width="180" height="22" rx="5" fill="#0e172a" stroke="#f59e0b" stroke-width="0.8"/>
      <text x="12" y="15" fill="#fbbf24" font-family="{FONT_MONO}" font-size="10" font-weight="700">INTEREST 02 // JAVA &amp; AWS</text>
      
      <text x="0" y="48" fill="#ffffff" font-size="17" font-weight="700">Enterprise Java &amp; AWS Cloud</text>
      <text x="0" y="70" fill="#fbbf24" font-size="12.5" font-style="italic">"Scalable cloud microservices with Java Spring Boot ☁️"</text>

      <text x="0" y="102" fill="#cbd5e1" font-size="12.5">• Built AI Resume Tailor on AWS Elastic Beanstalk</text>
      <text x="0" y="124" fill="#cbd5e1" font-size="12.5">• High-throughput Spring WebClient &amp; document parsing</text>
      <text x="0" y="146" fill="#cbd5e1" font-size="12.5">• Dynamic fallback routing across Groq, NVIDIA &amp; Cerebras</text>
      <text x="0" y="168" fill="#cbd5e1" font-size="12.5">• Automated LaTeX to PDF compilation pipelines</text>
    </g>

    <!-- Slide 3: AI Copilots & Cross-Platform (8s-12s) -->
    <g transform="translate(24, 52)" class="ab-slide-3">
      <rect width="180" height="22" rx="5" fill="#0e172a" stroke="#ff354f" stroke-width="0.8"/>
      <text x="12" y="15" fill="#ff758f" font-family="{FONT_MONO}" font-size="10" font-weight="700">INTEREST 03 // COPILOTS</text>
      
      <text x="0" y="48" fill="#ffffff" font-size="17" font-weight="700">AI Copilots &amp; Cross-Platform</text>
      <text x="0" y="70" fill="#ff758f" font-size="12.5" font-style="italic">"Real-time AI that feels like a native superpower ⚡"</text>

      <text x="0" y="102" fill="#cbd5e1" font-size="12.5">• Founder of CHINTU AI — real-time career intelligence</text>
      <text x="0" y="124" fill="#cbd5e1" font-size="12.5">• Native Electron desktop apps (Mac DMG &amp; Windows EXE)</text>
      <text x="0" y="146" fill="#cbd5e1" font-size="12.5">• Real-time voice inference &amp; computer vision OCR</text>
      <text x="0" y="168" fill="#cbd5e1" font-size="12.5">• WebRTC real-time audio/video on Social Connect</text>
    </g>

    <!-- Bottom Carousel Indicator Status -->
    <g transform="translate(24, 240)">
      <text x="0" y="14" fill="#475569" font-family="{FONT_MONO}" font-size="9.5">4s INTERVAL CAROUSEL // AUTO-CYCLING</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(output_dir, "about-life.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)
with open(os.path.join(local_assets_dir, "about-life.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)

print("Updated about-life.svg")

# ==============================================================================
# 3. STACK.SVG (FEATURING JAVA & AWS)
# ==============================================================================
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="900" height="460" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
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
      0%, 100% {{ transform: scale(1); opacity: 0.9; }}
      50% {{ transform: scale(1.05); opacity: 1; }}
    }}
    .st-orbit-1 {{
      animation: stFloat1 6s ease-in-out infinite;
    }}
    .st-orbit-2 {{
      animation: stFloat2 7s ease-in-out infinite;
    }}
    .st-orbit-3 {{
      animation: stFloat3 8s ease-in-out infinite;
    }}
    @keyframes stFloat1 {{
      0%, 100% {{ transform: translate(0, 0); }}
      50% {{ transform: translate(3px, -4px); }}
    }}
    @keyframes stFloat2 {{
      0%, 100% {{ transform: translate(0, 0); }}
      50% {{ transform: translate(-4px, 3px); }}
    }}
    @keyframes stFloat3 {{
      0%, 100% {{ transform: translate(0, 0); }}
      50% {{ transform: translate(2px, 4px); }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="460" rx="20" fill="#070b16"/>
  <rect width="900" height="460" fill="url(#st-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="458.5" rx="19.25" fill="none" stroke="url(#st-border)" stroke-width="1.5"/>

  <!-- Top Header Title -->
  <g transform="translate(50, 36)">
    <rect width="170" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="85" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      02 // TECH ARSENAL
    </text>
    <text x="190" y="17" fill="#64748b" font-family="{FONT_MONO}" font-size="11">MULTI-TIER ORBITAL ARCHITECTURE (JAVA · AWS · NEXT.JS)</text>
  </g>

  <!-- ORBITAL VISUALIZATION (Center: 450, 175) -->
  <g transform="translate(450, 175)">
    <!-- Central Core Glow -->
    <circle cx="0" cy="0" r="120" fill="url(#st-core-glow)"/>

    <!-- Tilted Elliptical Orbit 3 (Outer AI & Ecosystem) -->
    <ellipse cx="0" cy="0" rx="360" ry="110" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.25" stroke-dasharray="6 6" transform="rotate(-9)"/>
    
    <!-- Tilted Elliptical Orbit 2 (Middle Backend, Cloud & Java) -->
    <ellipse cx="0" cy="0" rx="260" ry="80" fill="none" stroke="#ff354f" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="4 4" transform="rotate(-9)"/>

    <!-- Tilted Elliptical Orbit 1 (Inner Core Frontend & Types) -->
    <ellipse cx="0" cy="0" rx="160" ry="50" fill="none" stroke="#38bdf8" stroke-width="1.4" stroke-opacity="0.45" transform="rotate(-9)"/>

    <!-- Center Sun / Core Hub -->
    <g class="st-pulse" transform="translate(0, 0)">
      <circle cx="0" cy="0" r="32" fill="#0b1224" stroke="#247bff" stroke-width="2"/>
      <circle cx="0" cy="0" r="37" fill="none" stroke="#ff354f" stroke-width="1" stroke-opacity="0.5"/>
      <text x="0" y="-3" fill="#ffffff" font-family="{FONT_MONO}" font-size="10.5" font-weight="800" text-anchor="middle">CHINTU</text>
      <text x="0" y="11" fill="#38bdf8" font-family="{FONT_MONO}" font-size="8.5" font-weight="700" text-anchor="middle">ENGINE</text>
    </g>

    <!-- ORBIT 1 NODES (Core Frontend & Language) -->
    <g class="st-orbit-1">
      <!-- Node: Next.js -->
      <g transform="translate(-135, -28)">
        <rect x="-38" y="-13" width="76" height="26" rx="13" fill="#000000" stroke="#38bdf8" stroke-width="1.2"/>
        <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">▲ Next.js</text>
      </g>
      <!-- Node: TypeScript -->
      <g transform="translate(0, -56)">
        <rect x="-42" y="-13" width="84" height="26" rx="13" fill="#3178c6" stroke="#ffffff" stroke-width="1"/>
        <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">TS TypeScript</text>
      </g>
      <!-- Node: React -->
      <g transform="translate(130, 26)">
        <rect x="-36" y="-13" width="72" height="26" rx="13" fill="#0b1224" stroke="#61dafb" stroke-width="1.2"/>
        <text x="0" y="4" fill="#61dafb" font-size="11" font-weight="700" text-anchor="middle">⚛ React</text>
      </g>
    </g>

    <!-- ORBIT 2 NODES (Backend, Java, AWS, Database) -->
    <g class="st-orbit-2">
      <!-- Node: Java Spring Boot (HIGHLIGHTED) -->
      <g transform="translate(-235, -42)">
        <rect x="-48" y="-13" width="96" height="26" rx="13" fill="#0e172a" stroke="#f59e0b" stroke-width="1.4"/>
        <text x="0" y="4" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">☕ Java Spring</text>
      </g>
      <!-- Node: AWS Cloud (HIGHLIGHTED) -->
      <g transform="translate(-85, 74)">
        <rect x="-40" y="-13" width="80" height="26" rx="13" fill="#0e172a" stroke="#ff9900" stroke-width="1.4"/>
        <text x="0" y="4" fill="#ff9900" font-size="11" font-weight="700" text-anchor="middle">☁️ AWS</text>
      </g>
      <!-- Node: Node.js -->
      <g transform="translate(85, -78)">
        <rect x="-38" y="-13" width="76" height="26" rx="13" fill="#0e172a" stroke="#5fa04e" stroke-width="1.2"/>
        <text x="0" y="4" fill="#5fa04e" font-size="11" font-weight="700" text-anchor="middle">⬢ Node.js</text>
      </g>
      <!-- Node: Supabase -->
      <g transform="translate(235, 42)">
        <rect x="-42" y="-13" width="84" height="26" rx="13" fill="#0e172a" stroke="#3ecf8e" stroke-width="1.2"/>
        <text x="0" y="4" fill="#3ecf8e" font-size="11" font-weight="700" text-anchor="middle">⚡ Supabase</text>
      </g>
    </g>

    <!-- ORBIT 3 NODES (AI, Payments & Cross-Platform) -->
    <g class="st-orbit-3">
      <!-- Node: OpenAI / Groq -->
      <g transform="translate(-330, 20)">
        <rect x="-44" y="-13" width="88" height="26" rx="13" fill="#0e172a" stroke="#10a37f" stroke-width="1.2"/>
        <text x="0" y="4" fill="#10a37f" font-size="11" font-weight="700" text-anchor="middle">🤖 OpenAI/Groq</text>
      </g>
      <!-- Node: Electron -->
      <g transform="translate(-200, 95)">
        <rect x="-38" y="-13" width="76" height="26" rx="13" fill="#0e172a" stroke="#47848f" stroke-width="1.2"/>
        <text x="0" y="4" fill="#47848f" font-size="11" font-weight="700" text-anchor="middle">⚛ Electron</text>
      </g>
      <!-- Node: Stripe -->
      <g transform="translate(-180, -96)">
        <rect x="-35" y="-13" width="70" height="26" rx="13" fill="#635bff" stroke="#ffffff" stroke-width="1"/>
        <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">💳 Stripe</text>
      </g>
      <!-- Node: Razorpay -->
      <g transform="translate(205, -96)">
        <rect x="-40" y="-13" width="80" height="26" rx="13" fill="#0c2451" stroke="#3395ff" stroke-width="1.2"/>
        <text x="0" y="4" fill="#3395ff" font-size="11" font-weight="700" text-anchor="middle">₹ Razorpay</text>
      </g>
      <!-- Node: PostgreSQL / MongoDB -->
      <g transform="translate(325, -25)">
        <rect x="-44" y="-13" width="88" height="26" rx="13" fill="#0e172a" stroke="#4169e1" stroke-width="1.2"/>
        <text x="0" y="4" fill="#60a5fa" font-size="11" font-weight="700" text-anchor="middle">🐘 Postgres/Mongo</text>
      </g>
      <!-- Node: Python/Django -->
      <g transform="translate(190, 95)">
        <rect x="-40" y="-13" width="80" height="26" rx="13" fill="#0e172a" stroke="#ffc331" stroke-width="1.2"/>
        <text x="0" y="4" fill="#ffc331" font-size="11" font-weight="700" text-anchor="middle">🐍 Python</text>
      </g>
    </g>
  </g>

  <!-- BOTTOM SECTION: Grouped Stack Chips (3 Boxes) -->
  <g transform="translate(50, 315)">
    <!-- Box 1: Frontend & UI -->
    <g transform="translate(0, 0)">
      <rect width="255" height="110" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <text x="16" y="24" fill="#60a5fa" font-family="{FONT_MONO}" font-size="11" font-weight="700">⚔️ FRONTEND ARSENAL</text>
      <text x="16" y="48" fill="#f1f5f9" font-size="12" font-weight="600">Next.js 14 · React 18 · TypeScript</text>
      <text x="16" y="68" fill="#94a3b8" font-size="11.5">Tailwind CSS · Redux Toolkit · Angular</text>
      <text x="16" y="88" fill="#64748b" font-size="11">Framer Motion · Chrome Extensions</text>
    </g>

    <!-- Box 2: Backend, Java & AWS Cloud -->
    <g transform="translate(270, 0)">
      <rect width="255" height="110" rx="12" fill="#0b1224" stroke="#f59e0b" stroke-width="1" stroke-opacity="0.4"/>
      <text x="16" y="24" fill="#fbbf24" font-family="{FONT_MONO}" font-size="11" font-weight="700">☕ JAVA, AWS &amp; BACKEND</text>
      <text x="16" y="48" fill="#f1f5f9" font-size="12" font-weight="600">Java 17/21 (Spring Boot) · AWS</text>
      <text x="16" y="68" fill="#94a3b8" font-size="11.5">Elastic Beanstalk · Node.js · Express</text>
      <text x="16" y="88" fill="#64748b" font-size="11">PostgreSQL · Supabase · MongoDB</text>
    </g>

    <!-- Box 3: AI, Payments & DevOps -->
    <g transform="translate(540, 0)">
      <rect width="260" height="110" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <text x="16" y="24" fill="#f43f5e" font-family="{FONT_MONO}" font-size="11" font-weight="700">🤖 AI, FINTECH &amp; ECOSYSTEM</text>
      <text x="16" y="48" fill="#f1f5f9" font-size="12" font-weight="600">Groq (&lt;200ms) · OpenAI · NVIDIA</text>
      <text x="16" y="68" fill="#94a3b8" font-size="11.5">Stripe · Razorpay · Zoho · LaTeX</text>
      <text x="16" y="88" fill="#64748b" font-size="11">Electron · Docker · Vercel · Git/GitHub</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(output_dir, "stack.svg"), "w", encoding="utf-8") as f:
    f.write(stack_svg)
with open(os.path.join(local_assets_dir, "stack.svg"), "w", encoding="utf-8") as f:
    f.write(stack_svg)

print("Updated stack.svg with Java & AWS")

# ==============================================================================
# 4. ID-DASHBOARD.SVG
# ==============================================================================
id_dash_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500" width="900" height="500" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="id-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="id-lanyard-strap" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="30%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#ff354f"/>
      <stop offset="70%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="id-metal-clasp" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="50%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="id-foil-sweep" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="transparent"/>
      <stop offset="45%" stop-color="transparent"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.28"/>
      <stop offset="55%" stop-color="transparent"/>
      <stop offset="100%" stop-color="transparent"/>
    </linearGradient>
    <clipPath id="id-avatar-circle">
      <circle cx="195" cy="190" r="50"/>
    </clipPath>
    <radialGradient id="id-dash-glow" cx="80%" cy="20%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="id-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <style>
    @media (prefers-reduced-motion: reduce) {{
      .id-anim {{ animation: none !important; }}
    }}
    .id-lanyard-assembly {{
      transform-origin: 195px 0px;
      animation: idPendulum 8s cubic-bezier(0.25, 1, 0.5, 1) infinite;
    }}
    @keyframes idPendulum {{
      0% {{ transform: rotate(-8deg); }}
      8% {{ transform: rotate(6.5deg); }}
      16% {{ transform: rotate(-4.2deg); }}
      24% {{ transform: rotate(2.8deg); }}
      32% {{ transform: rotate(-1.7deg); }}
      40% {{ transform: rotate(1.7deg); }}
      48% {{ transform: rotate(-1.7deg); }}
      56% {{ transform: rotate(1.7deg); }}
      64% {{ transform: rotate(-1.7deg); }}
      72% {{ transform: rotate(1.7deg); }}
      80% {{ transform: rotate(-1.7deg); }}
      88% {{ transform: rotate(1.7deg); }}
      96% {{ transform: rotate(-1.7deg); }}
      100% {{ transform: rotate(1.7deg); }}
    }}

    .id-foil-anim {{
      animation: idFoilSweep 4s ease-in-out infinite;
    }}
    @keyframes idFoilSweep {{
      0%, 20% {{ transform: translateX(-220px) translateY(-100px); }}
      60%, 100% {{ transform: translateX(220px) translateY(100px); }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="500" rx="20" fill="#070b16"/>
  <rect width="900" height="500" fill="url(#id-dash-glow)"/>
  <rect width="900" height="500" fill="url(#id-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="498.5" rx="19.25" fill="none" stroke="url(#id-border)" stroke-width="1.5"/>

  <!-- Top Title Header -->
  <g transform="translate(50, 36)">
    <rect width="190" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="95" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      03 // VERIFIED CREDENTIALS
    </text>
    <text x="210" y="17" fill="#64748b" font-family="{FONT_MONO}" font-size="11">OFFICIAL DEVELOPER IDENT &amp; DATED METRICS</text>
  </g>

  <!-- LEFT: HANGING LANYARD ID WITH METAL CLASP (Anchored at 195, 0) -->
  <g class="id-lanyard-assembly">
    <!-- Hanging Strap from Ceiling -->
    <rect x="183" y="0" width="24" height="68" fill="url(#id-lanyard-strap)" rx="2"/>
    <line x1="195" y1="0" x2="195" y2="68" stroke="#ff354f" stroke-width="2" stroke-opacity="0.8"/>

    <!-- Metallic Clasp and O-Ring -->
    <circle cx="195" cy="72" r="9" fill="none" stroke="url(#id-metal-clasp)" stroke-width="3"/>
    <rect x="187" y="78" width="16" height="12" rx="3" fill="url(#id-metal-clasp)"/>
    <line x1="187" y1="84" x2="203" y2="84" stroke="#1e293b" stroke-width="1"/>

    <!-- The ID Card Body (220 width, 340 height, centered at 195) -->
    <g transform="translate(85, 90)">
      <rect width="220" height="340" rx="16" fill="#0b1224" stroke="url(#id-border)" stroke-width="1.8"/>
      
      <!-- Top Lanyard Slot in Card -->
      <rect x="94" y="8" width="32" height="6" rx="3" fill="#070b16" stroke="#334155" stroke-width="1"/>

      <!-- Header of Card -->
      <g transform="translate(18, 28)">
        <text x="0" y="12" fill="#ffffff" font-family="{FONT_MONO}" font-size="11" font-weight="800" letter-spacing="1">CHINTU AI</text>
        <rect x="135" y="0" width="48" height="16" rx="4" fill="#1e293b"/>
        <text x="159" y="11" fill="#22c55e" font-family="{FONT_MONO}" font-size="8.5" font-weight="700" text-anchor="middle">LIVE PASS</text>
      </g>

      <!-- Holographic Avatar Frame with Inlined Base64 Image -->
      <g transform="translate(110, 100)">
        <circle cx="0" cy="0" r="54" fill="none" stroke="#247bff" stroke-width="2"/>
        <circle cx="0" cy="0" r="51" fill="#070b16"/>
        <g clip-path="url(#id-avatar-circle)" transform="translate(-195, -190)">
          <image href="data:image/png;base64,{id_b64}" x="135" y="130" width="120" height="120" preserveAspectRatio="xMidYMid meet"/>
        </g>
      </g>

      <!-- Dev Details -->
      <g transform="translate(110, 178)" text-anchor="middle">
        <text x="0" y="0" fill="#ffffff" font-size="15" font-weight="800">ABHISHEK TIWARI</text>
        <text x="0" y="18" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9.5" font-weight="600">FOUNDER &amp; FULL-STACK LEAD</text>
        <text x="0" y="32" fill="#64748b" font-family="{FONT_MONO}" font-size="8.5">ID: AT-6827 // HQ-LUCKNOW</text>
      </g>

      <!-- Foil Light Sweep Overlay -->
      <rect width="220" height="340" rx="16" fill="url(#id-foil-sweep)" class="id-foil-anim" pointer-events="none"/>

      <!-- Barcode Graphic & Tech Badges at Bottom -->
      <g transform="translate(20, 240)">
        <rect x="0" y="0" width="28" height="22" rx="4" fill="#ca8a04" stroke="#eab308" stroke-width="0.8"/>
        <line x1="8" y1="0" x2="8" y2="22" stroke="#a16207" stroke-width="0.8"/>
        <line x1="20" y1="0" x2="20" y2="22" stroke="#a16207" stroke-width="0.8"/>
        <text x="40" y="15" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">SECURITY CHIP // VERIFIED</text>
      </g>

      <!-- Barcode Lines -->
      <g transform="translate(20, 276)">
        <rect x="0" y="0" width="3" height="32" fill="#f8fafc"/>
        <rect x="5" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="9" y="0" width="4" height="32" fill="#f8fafc"/>
        <rect x="16" y="0" width="2" height="32" fill="#f8fafc"/>
        <rect x="21" y="0" width="1" height="32" fill="#f8fafc"/>
        <rect x="25" y="0" width="3" height="32" fill="#f8fafc"/>
        <rect x="31" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="35" y="0" width="4.5" height="32" fill="#f8fafc"/>
        <rect x="42" y="0" width="2" height="32" fill="#f8fafc"/>
        <rect x="47" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="51" y="0" width="3" height="32" fill="#f8fafc"/>
        <rect x="56" y="0" width="2" height="32" fill="#f8fafc"/>
        <rect x="61" y="0" width="4" height="32" fill="#f8fafc"/>
        <rect x="68" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="72" y="0" width="2" height="32" fill="#f8fafc"/>
        <rect x="76" y="0" width="3.5" height="32" fill="#f8fafc"/>
        <rect x="83" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="87" y="0" width="4" height="32" fill="#f8fafc"/>
        <rect x="94" y="0" width="2" height="32" fill="#f8fafc"/>
        <rect x="99" y="0" width="3" height="32" fill="#f8fafc"/>
        <rect x="105" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="109" y="0" width="4" height="32" fill="#f8fafc"/>
        <rect x="116" y="0" width="2" height="32" fill="#f8fafc"/>
        <rect x="121" y="0" width="3" height="32" fill="#f8fafc"/>
        <rect x="127" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="131" y="0" width="4" height="32" fill="#f8fafc"/>
        <rect x="138" y="0" width="2.5" height="32" fill="#f8fafc"/>
        <rect x="144" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="148" y="0" width="3" height="32" fill="#f8fafc"/>
        <rect x="154" y="0" width="2" height="32" fill="#f8fafc"/>
        <rect x="159" y="0" width="4" height="32" fill="#f8fafc"/>
        <rect x="166" y="0" width="1.5" height="32" fill="#f8fafc"/>
        <rect x="170" y="0" width="2.5" height="32" fill="#f8fafc"/>
        <rect x="175" y="0" width="4" height="32" fill="#f8fafc"/>
        <text x="90" y="44" fill="#64748b" font-family="{FONT_MONO}" font-size="8.5" text-anchor="middle">AUTHENTICATED DEVELOPER KEY</text>
      </g>
    </g>
  </g>

  <!-- RIGHT: VERIFIED METRICS & CREDENTIALS DASHBOARD (Width: 510) -->
  <g transform="translate(355, 85)">
    <!-- Metric Card 1: Production Apps -->
    <g transform="translate(0, 0)">
      <rect width="495" height="82" rx="14" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <circle cx="40" cy="41" r="22" fill="#0e172a" stroke="#247bff" stroke-width="1.2"/>
      <text x="40" y="47" fill="#38bdf8" font-size="20" text-anchor="middle">🚀</text>
      <text x="75" y="32" fill="#ffffff" font-size="16" font-weight="700">20+ Production Applications</text>
      <rect x="365" y="16" width="115" height="20" rx="5" fill="#070b16" stroke="#247bff" stroke-width="0.8"/>
      <text x="422" y="30" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9" font-weight="700" text-anchor="middle">LIVE PRODUCTION</text>
      <text x="75" y="52" fill="#94a3b8" font-size="12">Shipped full-lifecycle web, desktop (Electron) and mobile applications.</text>
      <text x="75" y="68" fill="#64748b" font-family="{FONT_MONO}" font-size="10">FEATURING: CHINTU AI · RESUME TAILOR (AWS+JAVA) · SOCIAL CONNECT</text>
    </g>

    <!-- Metric Card 2: Academic Degree -->
    <g transform="translate(0, 96)">
      <rect width="495" height="82" rx="14" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <circle cx="40" cy="41" r="22" fill="#0e172a" stroke="#a855f7" stroke-width="1.2"/>
      <text x="40" y="47" fill="#c084fc" font-size="20" text-anchor="middle">🎓</text>
      <text x="75" y="32" fill="#ffffff" font-size="16" font-weight="700">Postgraduate in Computer Applications</text>
      <rect x="375" y="16" width="105" height="20" rx="5" fill="#070b16" stroke="#a855f7" stroke-width="0.8"/>
      <text x="427" y="30" fill="#c084fc" font-family="{FONT_MONO}" font-size="9" font-weight="700" text-anchor="middle">ACADEMIC HONORS</text>
      <text x="75" y="52" fill="#94a3b8" font-size="12">Master's level computer science foundation in algorithms, networks &amp; DBs.</text>
      <text x="75" y="68" fill="#64748b" font-family="{FONT_MONO}" font-size="10">LOCATION: LUCKNOW, INDIA · POSTGRADUATE MCA</text>
    </g>

    <!-- Metric Card 3: Meta React Developer -->
    <g transform="translate(0, 192)">
      <rect width="495" height="82" rx="14" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <circle cx="40" cy="41" r="22" fill="#0e172a" stroke="#0668e1" stroke-width="1.2"/>
      <text x="40" y="47" fill="#60a5fa" font-size="18" text-anchor="middle">🥇</text>
      <text x="75" y="32" fill="#ffffff" font-size="16" font-weight="700">Meta Certified React Developer</text>
      <rect x="365" y="16" width="115" height="20" rx="5" fill="#070b16" stroke="#0668e1" stroke-width="0.8"/>
      <text x="422" y="30" fill="#60a5fa" font-family="{FONT_MONO}" font-size="9" font-weight="700" text-anchor="middle">META VERIFIED // 2025</text>
      <text x="75" y="52" fill="#94a3b8" font-size="12">Advanced React patterns, state orchestration, component lifecycle &amp; UX.</text>
      <text x="75" y="68" fill="#64748b" font-family="{FONT_MONO}" font-size="10">ISSUER: META · VALIDATED CREDENTIAL 2025</text>
    </g>

    <!-- Metric Card 4: FreeCodeCamp Full Stack -->
    <g transform="translate(0, 288)">
      <rect width="495" height="82" rx="14" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <circle cx="40" cy="41" r="22" fill="#0e172a" stroke="#22c55e" stroke-width="1.2"/>
      <text x="40" y="47" fill="#4ade80" font-size="18" text-anchor="middle">📜</text>
      <text x="75" y="32" fill="#ffffff" font-size="16" font-weight="700">FreeCodeCamp Full-Stack &amp; DSA</text>
      <rect x="365" y="16" width="115" height="20" rx="5" fill="#070b16" stroke="#22c55e" stroke-width="0.8"/>
      <text x="422" y="30" fill="#4ade80" font-family="{FONT_MONO}" font-size="9" font-weight="700" text-anchor="middle">FCC VERIFIED // 2024</text>
      <text x="75" y="52" fill="#94a3b8" font-size="12">Full Stack Web Development &amp; JavaScript Algorithms and Data Structures.</text>
      <text x="75" y="68" fill="#64748b" font-family="{FONT_MONO}" font-size="10">ISSUER: FREECODECAMP · VERIFIED 2023 - 2024</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(output_dir, "id-dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(id_dash_svg)
with open(os.path.join(local_assets_dir, "id-dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(id_dash_svg)

print("Updated id-dashboard.svg")

# ==============================================================================
# 5. CONNECT.SVG
# ==============================================================================
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="900" height="420" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="conn-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="conn-title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#93c5fd"/>
      <stop offset="100%" stop-color="#247bff"/>
    </linearGradient>
    <radialGradient id="conn-char-glow" cx="220" cy="220" r="180" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.25"/>
      <stop offset="60%" stop-color="#ff354f" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="conn-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <style>
    @media (prefers-reduced-motion: reduce) {{
      .conn-anim {{ animation: none !important; }}
    }}
    .conn-float {{
      animation: connFloat 4s ease-in-out infinite;
    }}
    @keyframes connFloat {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-7px); }}
    }}
    .conn-nudge {{
      animation: connNudge 1.4s ease-in-out infinite;
    }}
    @keyframes connNudge {{
      0%, 100% {{ transform: translateX(0); }}
      50% {{ transform: translateX(7px); }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="420" rx="20" fill="#070b16"/>
  <rect width="900" height="420" fill="url(#conn-dots)"/>
  <circle cx="220" cy="220" r="180" fill="url(#conn-char-glow)"/>
  <rect x="0.75" y="0.75" width="898.5" height="418.5" rx="19.25" fill="none" stroke="url(#conn-border)" stroke-width="1.5"/>

  <!-- LEFT: CHARACTER ASSET (right_pointing.png) -->
  <g class="conn-float" transform="translate(10, 20)">
    <ellipse cx="200" cy="220" rx="150" ry="150" fill="none" stroke="#247bff" stroke-width="1" stroke-opacity="0.2" stroke-dasharray="4 4"/>
    <ellipse cx="200" cy="220" rx="175" ry="175" fill="none" stroke="#ff354f" stroke-width="1" stroke-opacity="0.15" stroke-dasharray="6 6"/>

    <image href="data:image/png;base64,{pointing_b64}" x="10" y="25" width="370" height="370" preserveAspectRatio="xMidYMid meet"/>

    <g transform="translate(90, 365)">
      <rect width="210" height="24" rx="6" fill="#0b1224" stroke="#247bff" stroke-width="1"/>
      <text x="105" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="700" text-anchor="middle" letter-spacing="1">
        LET'S CONNECT &amp; BUILD ⚡
      </text>
    </g>
  </g>

  <!-- RIGHT: CALL TO ACTION & SOCIAL CARDS -->
  <g transform="translate(415, 40)">
    <text x="0" y="24" fill="url(#conn-title-grad)" font-size="28" font-weight="800" letter-spacing="-0.5">
      LET'S BUILD SOMETHING EPIC
    </text>
    <text x="0" y="46" fill="#38bdf8" font-family="{FONT_MONO}" font-size="12" font-weight="600" letter-spacing="1">
      // OPEN FOR SAAS COLLABORATIONS &amp; SENIOR ROLES
    </text>

    <!-- Social Card 1: LinkedIn -->
    <g transform="translate(0, 68)">
      <rect width="435" height="58" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <rect x="14" y="11" width="36" height="36" rx="8" fill="#0a66c2"/>
      <text x="32" y="35" fill="#ffffff" font-size="18" font-weight="800" text-anchor="middle">in</text>
      <text x="62" y="27" fill="#ffffff" font-size="14.5" font-weight="700">LinkedIn Profile</text>
      <text x="62" y="44" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11">linkedin.com/in/abhishek-tiwariiii</text>
      <g class="conn-nudge" transform="translate(395, 34)">
        <text x="0" y="0" fill="#38bdf8" font-size="20" font-weight="700">→</text>
      </g>
    </g>

    <!-- Social Card 2: Portfolio -->
    <g transform="translate(0, 138)">
      <rect width="435" height="58" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <rect x="14" y="11" width="36" height="36" rx="8" fill="#6366f1"/>
      <text x="32" y="35" fill="#ffffff" font-size="18" text-anchor="middle">🌐</text>
      <text x="62" y="27" fill="#ffffff" font-size="14.5" font-weight="700">Personal Portfolio &amp; Demos</text>
      <text x="62" y="44" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11">portfolio.getchintu.com</text>
      <g class="conn-nudge" transform="translate(395, 34)">
        <text x="0" y="0" fill="#6366f1" font-size="20" font-weight="700">→</text>
      </g>
    </g>

    <!-- Social Card 3: CHINTU AI -->
    <g transform="translate(0, 208)">
      <rect width="435" height="58" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <rect x="14" y="11" width="36" height="36" rx="8" fill="#8b5cf6"/>
      <text x="32" y="35" fill="#ffffff" font-size="18" text-anchor="middle">⚡</text>
      <text x="62" y="27" fill="#ffffff" font-size="14.5" font-weight="700">CHINTU AI (Founder &amp; Live App)</text>
      <text x="62" y="44" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11">getchintu.com</text>
      <g class="conn-nudge" transform="translate(395, 34)">
        <text x="0" y="0" fill="#8b5cf6" font-size="20" font-weight="700">→</text>
      </g>
    </g>

    <!-- Social Card 4: Direct Email -->
    <g transform="translate(0, 278)">
      <rect width="435" height="58" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <rect x="14" y="11" width="36" height="36" rx="8" fill="#ea4335"/>
      <text x="32" y="35" fill="#ffffff" font-size="18" text-anchor="middle">✉</text>
      <text x="62" y="27" fill="#ffffff" font-size="14.5" font-weight="700">Direct Contact &amp; Inquiries</text>
      <text x="62" y="44" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11">abhishektiwari@getchintu.com</text>
      <g class="conn-nudge" transform="translate(395, 34)">
        <text x="0" y="0" fill="#ea4335" font-size="20" font-weight="700">→</text>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(output_dir, "connect.svg"), "w", encoding="utf-8") as f:
    f.write(connect_svg)
with open(os.path.join(local_assets_dir, "connect.svg"), "w", encoding="utf-8") as f:
    f.write(connect_svg)

print("Updated connect.svg")

# ==============================================================================
# 6. README.MD (WITH 4 PROJECTS - RESUME TAILOR AT POSITION #2)
# ==============================================================================
readme_content = '''# Abhishek Tiwari — Full-Stack Developer & SaaS Builder

<div align="center">

<!-- ANIMATED SVG 01: HERO -->
<img src="./assets/hero.svg?v=1" alt="Abhishek Tiwari — Hero Profile" width="100%" />

<br/><br/>

<!-- ANIMATED SVG 02: ABOUT & CAPABILITIES -->
<img src="./assets/about-life.svg?v=1" alt="Abhishek Tiwari — Capabilities & Life Carousel" width="100%" />

<br/><br/>

<!-- ANIMATED SVG 03: TECH ARSENAL ORBIT -->
<img src="./assets/stack.svg?v=1" alt="Abhishek Tiwari — Tech Arsenal Orbit" width="100%" />

<br/><br/>

<!-- ANIMATED SVG 04: ID BADGE & VERIFIED METRICS -->
<img src="./assets/id-dashboard.svg?v=1" alt="Abhishek Tiwari — ID Badge & Credentials Dashboard" width="100%" />

<br/><br/>

<!-- ANIMATED SVG 05: CONNECT & SOCIAL CTA -->
<img src="./assets/connect.svg?v=1" alt="Connect with Abhishek Tiwari" width="100%" />

<br/>

<!-- REAL CLICKABLE SOCIAL BADGES (Required because GitHub disables links inside SVGs) -->
<a href="https://www.linkedin.com/in/abhishek-tiwariiii"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;
<a href="https://portfolio.getchintu.com"><img src="https://img.shields.io/badge/Portfolio-Visit_Live-6366f1?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>&nbsp;
<a href="https://getchintu.com"><img src="https://img.shields.io/badge/CHINTU_AI-Live_Platform-8B5CF6?style=for-the-badge&logo=rocket&logoColor=white" /></a>&nbsp;
<a href="https://github.com/Abhishek6827"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;
<a href="mailto:abhishektiwari@getchintu.com"><img src="https://img.shields.io/badge/Gmail-Hire_Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>

</div>

---

## 🚀 Featured Flagship Projects

<table>
  <thead>
    <tr>
      <th width="5%">#</th>
      <th width="30%">Project &amp; Live Demo</th>
      <th width="40%">Architecture &amp; Core Capabilities</th>
      <th width="25%">Tech Stack</th>
    </tr>
  </thead>
  <tbody>
    <!-- PROJECT 1: CHINTU AI -->
    <tr>
      <td align="center"><b>01</b></td>
      <td>
        <b>⚡ CHINTU AI</b><br/>
        <i>Real-Time AI Career Copilot &amp; Prep Platform</i><br/>
        <a href="https://getchintu.com"><b>Visit Live Platform ↗</b></a>
      </td>
      <td>
        • Multi-model LLM orchestration (Alibaba, OpenAI, Groq &amp; AssemblyAI).<br/>
        • Sub-200ms ultra-low-latency voice inference and screen OCR.<br/>
        • Cross-platform apps (Electron Mac DMG / Windows EXE + Android APK).<br/>
        • Razorpay 3-tier subscription billing with webhook automation.
      </td>
      <td>
        <code>Next.js 14</code> <code>TypeScript</code> <code>Electron</code> <code>Supabase</code> <code>Razorpay</code> <code>Groq</code>
      </td>
    </tr>
    <!-- PROJECT 2: AI RESUME TAILOR (AWS + JAVA) -->
    <tr>
      <td align="center"><b>02</b></td>
      <td>
        <b>📄 AI Resume Tailor &amp; LaTeX Engine</b><br/>
        <i>Cloud-Native ATS Tailoring &amp; Multi-LLM Router</i><br/>
        <a href="https://github.com/Abhishek6827/Resume-Extension"><b>View Project Repository ↗</b></a>
      </td>
      <td>
        • High-throughput <b>Java Spring Boot</b> backend deployed on <b>AWS Elastic Beanstalk</b>.<br/>
        • Dynamic multi-provider AI fallback router (Groq, Cerebras, NVIDIA, OpenRouter).<br/>
        • Document parsing with Apache PDFBox (PDF) &amp; Apache POI (DOCX).<br/>
        • Automated LaTeX TexLive compilation to ATS-optimized PDF resumes.<br/>
        • Modern Next.js glassmorphism Chrome Extension side-panel.
      </td>
      <td>
        <code>Java 17/21</code> <code>Spring Boot</code> <code>AWS Beanstalk</code> <code>Apache PDFBox</code> <code>LaTeX</code> <code>Next.js</code>
      </td>
    </tr>
    <!-- PROJECT 3: SOCIAL CONNECT -->
    <tr>
      <td align="center"><b>03</b></td>
      <td>
        <b>🟣 Social Connect</b><br/>
        <i>Real-Time Full-Stack Social &amp; WebRTC Platform</i><br/>
        <a href="https://socialconnect.getchintu.com/login"><b>Visit Live App ↗</b></a>
      </td>
      <td>
        • Peer-to-peer <b>WebRTC</b> audio &amp; video calls with ICE signaling.<br/>
        • Socket.io real-time chat with presence tracking, receipts &amp; emoji reactions.<br/>
        • JWT authentication, OAuth 2.0 (Google &amp; Facebook) and route guards.<br/>
        • Full feed, user profiles, activity streams, and media uploads.
      </td>
      <td>
        <code>Angular 17</code> <code>Express.js</code> <code>TypeScript</code> <code>MongoDB</code> <code>Socket.io</code> <code>WebRTC</code>
      </td>
    </tr>
    <!-- PROJECT 4: YOUTUBE AUTOMATION -->
    <tr>
      <td align="center"><b>04</b></td>
      <td>
        <b>🔴 YouTube Automation</b><br/>
        <i>AI-Powered Scheduled Content Upload Pipeline</i><br/>
        <a href="https://yt-automation-beta.vercel.app/"><b>Visit Live App ↗</b></a>
      </td>
      <td>
        • Automated workflow: Google Drive Scan → Multi-tier AI Metadata → Scheduled Upload.<br/>
        • 3-tier generation: AssemblyAI audio transcript + Gemini Vision frame analysis.<br/>
        • Post-upload copyright claim detection and auto-revert protection.<br/>
        • Multi-job scheduling with node-cron and NextAuth v5 session persistence.
      </td>
      <td>
        <code>Next.js 16</code> <code>PostgreSQL</code> <code>Prisma ORM</code> <code>Gemini 2.0</code> <code>AssemblyAI</code> <code>FFmpeg</code>
      </td>
    </tr>
  </tbody>
</table>

---

## 📊 Developer Metrics & Contribution Activity

<div align="center">

<img width="49%" src="https://github-readme-stats-7ihy.vercel.app/api?username=Abhishek6827&show_icons=true&theme=radical&hide_border=true&bg_color=0d1117&title_color=a855f7&icon_color=a855f7&text_color=c9d1d9&count_private=true&rank_icon=github" />
<img width="49%" src="https://github-readme-streak-stats-eight.vercel.app?user=Abhishek6827&theme=radical&hide_border=true&background=0d1117&ring=a855f7&fire=a855f7&currStreakLabel=a855f7" />

<br/>

<!-- Snake Animation -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake.svg" />
  <img alt="github-snake" src="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake.svg" />
</picture>

</div>

---

<div align="center">
  <sub>Crafted with passion &amp; precision by <a href="https://github.com/Abhishek6827">Abhishek Tiwari</a>. Powered by SVG animations &amp; GitHub Actions.</sub>
</div>
'''

with open(os.path.join(repo_dir, "Readme.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)
with open(os.path.join(local_assets_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Created Readme.md with 4 projects (Resume Tailor at #2)")

# ==============================================================================
# 7. PREVIEW.HTML
# ==============================================================================
preview_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GitHub Profile README Preview — Abhishek Tiwari</title>
  <style>
    body {{
      margin: 0;
      padding: 40px 20px;
      background: #0d1117;
      color: #c9d1d9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .container {{
      max-width: 900px;
      width: 100%;
    }}
    .card-preview {{
      margin-bottom: 24px;
      width: 100%;
    }}
    .card-preview img {{
      width: 100%;
      height: auto;
      display: block;
      border-radius: 20px;
    }}
    .test-controls {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 16px 24px;
      margin-bottom: 30px;
      width: 100%;
      box-sizing: border-box;
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      justify-content: space-between;
      align-items: center;
    }}
    .test-controls h2 {{
      margin: 0;
      font-size: 16px;
      color: #58a6ff;
    }}
    .btn {{
      background: #238636;
      color: white;
      border: none;
      padding: 8px 16px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      font-size: 13px;
    }}
    .btn-secondary {{
      background: #21262d;
      border: 1px solid #30363d;
    }}
    .table-container {{
      margin-top: 30px;
      width: 100%;
      border-collapse: collapse;
      background: #161b22;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #30363d;
    }}
    .table-container th, .table-container td {{
      padding: 12px 16px;
      text-align: left;
      border-bottom: 1px solid #30363d;
      font-size: 13px;
    }}
    .table-container th {{
      background: #21262d;
      color: #f0f6fc;
    }}
    code {{
      background: rgba(110,118,129,0.4);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 11px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="test-controls">
      <div>
        <h2>✅ Playbook Verification Testbed</h2>
        <span style="font-size: 12px; color: #8b949e;">Testing 5 SVGs + 4 Projects (Resume Tailor @ #2)</span>
      </div>
      <div>
        <button class="btn" onclick="toggleBackground()">Toggle Background (Dark/Light)</button>
        <button class="btn btn-secondary" onclick="reloadImages()">Refresh Images</button>
      </div>
    </div>

    <!-- SVG 1: Hero -->
    <div class="card-preview">
      <img src="./assets/hero.svg?v=1" alt="Hero SVG" id="img-hero" />
    </div>

    <!-- SVG 2: About & Life -->
    <div class="card-preview">
      <img src="./assets/about-life.svg?v=1" alt="About & Life SVG" id="img-about" />
    </div>

    <!-- SVG 3: Tech Stack -->
    <div class="card-preview">
      <img src="./assets/stack.svg?v=1" alt="Stack SVG" id="img-stack" />
    </div>

    <!-- SVG 4: ID Dashboard -->
    <div class="card-preview">
      <img src="./assets/id-dashboard.svg?v=1" alt="ID Dashboard SVG" id="img-id" />
    </div>

    <!-- SVG 5: Connect -->
    <div class="card-preview">
      <img src="./assets/connect.svg?v=1" alt="Connect SVG" id="img-connect" />
    </div>

    <!-- 4 Projects Summary Table -->
    <table class="table-container">
      <thead>
        <tr>
          <th>#</th>
          <th>Project</th>
          <th>Key Tech</th>
          <th>Highlights</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><b>01</b></td>
          <td><b>⚡ CHINTU AI</b></td>
          <td><code>Next.js 14</code> <code>Electron</code> <code>Groq</code></td>
          <td>Real-time AI career copilot, sub-200ms voice inference, 63+ languages.</td>
        </tr>
        <tr>
          <td><b>02</b></td>
          <td><b>📄 AI Resume Tailor</b></td>
          <td><code>Java 17/21</code> <code>AWS Beanstalk</code> <code>LaTeX</code></td>
          <td>ATS tailoring engine, Spring Boot on AWS, multi-provider AI fallback, PDF/DOCX.</td>
        </tr>
        <tr>
          <td><b>03</b></td>
          <td><b>🟣 Social Connect</b></td>
          <td><code>Angular 17</code> <code>Socket.io</code> <code>WebRTC</code></td>
          <td>Real-time chat &amp; P2P audio/video calling with presence tracking.</td>
        </tr>
        <tr>
          <td><b>04</b></td>
          <td><b>🔴 YouTube Automation</b></td>
          <td><code>Next.js 16</code> <code>Prisma</code> <code>Gemini 2.0</code></td>
          <td>Automated Google Drive to YouTube upload pipeline with copyright protection.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <script>
    let isLight = false;
    function toggleBackground() {{
      isLight = !isLight;
      document.body.style.background = isLight ? "#ffffff" : "#0d1117";
      document.body.style.color = isLight ? "#24292f" : "#c9d1d9";
    }}
    function reloadImages() {{
      const t = Date.now();
      ['hero', 'about', 'stack', 'id', 'connect'].forEach(name => {{
        const el = document.getElementById('img-' + name);
        if (el) {{
          el.src = './assets/' + (name === 'hero' ? 'hero' : name === 'about' ? 'about-life' : name === 'stack' ? 'stack' : name === 'id' ? 'id-dashboard' : 'connect') + '.svg?t=' + t;
        }}
      }});
    }}
  </script>
</body>
</html>'''

with open(os.path.join(repo_dir, "preview.html"), "w", encoding="utf-8") as f:
    f.write(preview_html)
with open(os.path.join(local_assets_dir, "preview.html"), "w", encoding="utf-8") as f:
    f.write(preview_html)

print("Created preview.html")

# ==============================================================================
# 8. UPLOAD-READY ZIP CREATION
# ==============================================================================
zip_path = os.path.join(repo_dir, "Abhishek6827-profile-package.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(os.path.join(repo_dir, "Readme.md"), arcname="Readme.md")
    zipf.write(os.path.join(repo_dir, "preview.html"), arcname="preview.html")
    for fname in ["hero.svg", "about-life.svg", "stack.svg", "id-dashboard.svg", "connect.svg", "id.png", "right_pointing.png"]:
        fpath = os.path.join(output_dir, fname)
        if os.path.exists(fpath):
            zipf.write(fpath, arcname=f"assets/{fname}")

# Also copy zip to local workspace
with open(zip_path, 'rb') as f_in:
    with open(os.path.join(local_assets_dir, "Abhishek6827-profile-package.zip"), 'wb') as f_out:
        f_out.write(f_in.read())

print("Created upload-ready ZIP: Abhishek6827-profile-package.zip")
