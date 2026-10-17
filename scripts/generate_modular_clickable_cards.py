import os
import base64
import io
import xml.etree.ElementTree as ET
from PIL import Image

output_dir = r"D:\Desktop\Projects\Abhishek6827\assets"
local_assets_dir = r"d:\Desktop\Resume-Extension\profile-assets"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(local_assets_dir, exist_ok=True)

# 1. Base64 encode pointing character image
pointing_png_path = r"C:\Users\Abhishek\Downloads\right_pointing.png"
if not os.path.exists(pointing_png_path):
    pointing_png_path = os.path.join(local_assets_dir, "right_pointing.png")

with Image.open(pointing_png_path) as img:
    img = img.convert("RGBA")
    max_dim = 650
    if max(img.size) > max_dim:
        img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    pointing_b64 = base64.b64encode(buf.getvalue()).decode('ascii')

# Save a copy in local_assets_dir
with open(os.path.join(local_assets_dir, "right_pointing.png"), "wb") as f:
    f.write(buf.getvalue())

FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"

# -------------------------------------------------------------
# CONNECT HEADER (width: 900, height: 185)
# -------------------------------------------------------------
def build_connect_header():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 185" width="900" height="185" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="ch-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="ch-title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#93c5fd"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <radialGradient id="ch-char-glow" cx="130" cy="95" r="110" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.28"/>
      <stop offset="60%" stop-color="#ff354f" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0"/>
    </radialGradient>
    <pattern id="ch-dots" width="24" height="24" patternUnits="userSpaceOnUse">
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
      50% {{ transform: translateY(-5px); }}
    }}
    .conn-pulse {{
      animation: connPulse 2s ease-in-out infinite;
    }}
    @keyframes connPulse {{
      0%, 100% {{ opacity: 0.9; }}
      50% {{ opacity: 0.4; }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="185" rx="20" fill="#070b16"/>
  <rect width="900" height="185" fill="url(#ch-dots)"/>
  <circle cx="130" cy="95" r="110" fill="url(#ch-char-glow)"/>
  <rect x="0.75" y="0.75" width="898.5" height="183.5" rx="19.25" fill="none" stroke="url(#ch-border)" stroke-width="1.5"/>

  <!-- LEFT: CHARACTER CUTOUT (Abhishek pointing right/down) -->
  <g class="conn-float" transform="translate(15, 5)">
    <ellipse cx="115" cy="88" rx="80" ry="80" fill="none" stroke="#247bff" stroke-width="1" stroke-opacity="0.25" stroke-dasharray="4 4"/>
    <ellipse cx="115" cy="88" rx="98" ry="98" fill="none" stroke="#ff354f" stroke-width="1" stroke-opacity="0.15" stroke-dasharray="6 6"/>
    <image href="data:image/png;base64,{pointing_b64}" x="-10" y="-12" width="250" height="200" preserveAspectRatio="xMidYMid meet"/>
  </g>

  <!-- RIGHT: TITLE & CALL TO ACTION -->
  <g transform="translate(260, 26)">
    <rect width="180" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.6"/>
    <circle cx="14" cy="12" r="4" fill="#38bdf8" class="conn-pulse"/>
    <text x="26" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1">
      05 // LET'S CONNECT ⚡
    </text>

    <!-- Availability Live Badge -->
    <g transform="translate(430, 0)">
      <rect width="180" height="24" rx="6" fill="#0b1224" stroke="#10b981" stroke-width="1"/>
      <circle cx="14" cy="12" r="3.5" fill="#10b981" class="conn-pulse"/>
      <text x="26" y="16" fill="#34d399" font-family="{FONT_MONO}" font-size="10" font-weight="700">ACTIVE &amp; AVAILABLE</text>
    </g>

    <text x="0" y="66" fill="url(#ch-title-grad)" font-size="28" font-weight="800" letter-spacing="-0.5">
      LET'S BUILD SOMETHING EPIC
    </text>
    <text x="0" y="94" fill="#94a3b8" font-family="{FONT_MONO}" font-size="12" font-weight="500">
      Full-Stack AI Engineering · Scalable Cloud Platforms · Open Source Collaboration
    </text>

    <!-- Instruction Subtitle -->
    <g transform="translate(0, 118)">
      <rect width="610" height="26" rx="6" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <text x="14" y="17" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10.5" font-weight="600">
        SELECT ANY CHANNEL BELOW FOR DIRECT REAL-TIME COMMUNICATION ↘
      </text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# CONNECT BUTTON CARD (width: 440, height: 76)
# -------------------------------------------------------------
def build_connect_button(icon_type, title, subtitle, badge_text, badge_color, border_color):
    icon_svg = ""
    if icon_type == "linkedin":
        icon_svg = '''
      <rect width="40" height="40" rx="9" fill="#0a66c2"/>
      <text x="20" y="27" fill="#ffffff" font-size="20" font-weight="800" text-anchor="middle">in</text>
        '''
    elif icon_type == "portfolio":
        icon_svg = '''
      <rect width="40" height="40" rx="9" fill="#4f46e5"/>
      <circle cx="20" cy="20" r="11" fill="none" stroke="#ffffff" stroke-width="1.8"/>
      <ellipse cx="20" cy="20" rx="5.5" ry="11" fill="none" stroke="#ffffff" stroke-width="1.4"/>
      <line x1="9" y1="20" x2="31" y2="20" stroke="#ffffff" stroke-width="1.4"/>
        '''
    elif icon_type == "chintu":
        icon_svg = '''
      <rect width="40" height="40" rx="9" fill="#7c3aed"/>
      <path d="M22 9 L13 22 L19 22 L17 31 L27 18 L21 18 Z" fill="#ffffff"/>
        '''
    elif icon_type == "email":
        icon_svg = '''
      <rect width="40" height="40" rx="9" fill="#ea4335"/>
      <rect x="10" y="13" width="20" height="14" rx="2" fill="none" stroke="#ffffff" stroke-width="1.8"/>
      <path d="M10 14 L20 21 L30 14" fill="none" stroke="#ffffff" stroke-width="1.8"/>
        '''

    esc_title = html.escape(title)
    esc_subtitle = html.escape(subtitle)
    esc_badge_text = html.escape(badge_text)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 76" width="440" height="76" style="background:#0b1224; border-radius:12px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="btn-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{border_color}" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="{border_color}" stop-opacity="0.15"/>
    </linearGradient>
  </defs>

  <style>
    @media (prefers-reduced-motion: reduce) {{
      .btn-arrow {{ animation: none !important; }}
    }}
    .btn-arrow {{
      animation: btnArrow 1.5s ease-in-out infinite;
    }}
    @keyframes btnArrow {{
      0%, 100% {{ transform: translateX(0); }}
      50% {{ transform: translateX(4px); }}
    }}
  </style>

  <!-- Card Background & Border -->
  <rect width="440" height="76" rx="12" fill="#0b1224"/>
  <rect x="0.75" y="0.75" width="438.5" height="74.5" rx="11.25" fill="none" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="0.75" y="0.75" width="438.5" height="74.5" rx="11.25" fill="none" stroke="url(#btn-glow)" stroke-width="1.2"/>

  <!-- Left Icon -->
  <g transform="translate(16, 18)">
    {icon_svg}
  </g>

  <!-- Center Text -->
  <g transform="translate(70, 24)">
    <text x="0" y="14" fill="#ffffff" font-size="14.5" font-weight="700">{esc_title}</text>
    <text x="0" y="32" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11">{esc_subtitle}</text>
  </g>

  <!-- Right Action Badge -->
  <g transform="translate(325, 25)">
    <rect width="98" height="26" rx="6" fill="#0e172a" stroke="{badge_color}" stroke-width="1"/>
    <text x="43" y="17" fill="{badge_color}" font-family="{FONT_MONO}" font-size="10" font-weight="700" text-anchor="middle">{esc_badge_text}</text>
    <g class="btn-arrow" transform="translate(74, 17)">
      <text x="0" y="0" fill="{badge_color}" font-size="12" font-weight="700">→</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# MORE PROJECTS HEADER (width: 900, height: 76)
# -------------------------------------------------------------
def build_more_projects_header():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 76" width="900" height="76" style="background:#070b16; border-radius:16px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="mph-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <pattern id="mph-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <!-- Background Base -->
  <rect width="900" height="76" rx="16" fill="#070b16"/>
  <rect width="900" height="76" fill="url(#mph-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="74.5" rx="15.25" fill="none" stroke="url(#mph-border)" stroke-width="1.5"/>

  <!-- Content -->
  <g transform="translate(36, 25)">
    <rect width="190" height="26" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.6"/>
    <text x="95" y="17" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.2">
      06 // ECOSYSTEM APPS
    </text>
    <text x="210" y="18" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11.5">
      ADDITIONAL PRODUCTION DEPLOYMENTS &amp; TOOLS
    </text>

    <!-- Right Badge -->
    <g transform="translate(650, 0)">
      <rect width="176" height="26" rx="6" fill="#0b1224" stroke="#6366f1" stroke-width="1.1"/>
      <text x="88" y="17" fill="#818cf8" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" text-anchor="middle">EXPLORE ALL APPS ↗</text>
    </g>
  </g>
</svg>'''

import html

# -------------------------------------------------------------
# MORE PROJECTS TILE (width: 440, height: 104)
# -------------------------------------------------------------
def build_project_tile(name, desc, stack, badge, color):
    esc_name = html.escape(name)
    esc_desc = html.escape(desc)
    esc_stack = html.escape(stack)
    esc_badge = html.escape(badge)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 104" width="440" height="104" style="background:#0b1224; border-radius:12px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="tile-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="{color}" stop-opacity="0.05"/>
    </linearGradient>
  </defs>

  <style>
    @media (prefers-reduced-motion: reduce) {{
      .tile-nudge {{ animation: none !important; }}
    }}
    .tile-nudge {{
      animation: tileNudge 1.6s ease-in-out infinite;
    }}
    @keyframes tileNudge {{
      0%, 100% {{ transform: translateX(0); }}
      50% {{ transform: translateX(3px); }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="440" height="104" rx="12" fill="#0b1224"/>
  <rect x="0.75" y="0.75" width="438.5" height="102.5" rx="11.25" fill="none" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="0.75" y="0.75" width="438.5" height="102.5" rx="11.25" fill="none" stroke="url(#tile-grad)" stroke-width="1.2"/>

  <!-- Content -->
  <g transform="translate(20, 18)">
    <!-- Top Row: Name and Live Badge -->
    <text x="0" y="14" fill="#ffffff" font-size="15" font-weight="700">{esc_name}</text>

    <!-- Badge on Right -->
    <g class="tile-nudge" transform="translate(315, 0)">
      <rect width="84" height="22" rx="5" fill="#0e172a" stroke="{color}" stroke-width="0.9"/>
      <text x="42" y="15" fill="{color}" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" text-anchor="middle">{esc_badge}</text>
    </g>

    <!-- Description -->
    <text x="0" y="38" fill="#94a3b8" font-size="11.5">{esc_desc}</text>

    <!-- Tech Stack Pill Bar -->
    <g transform="translate(0, 50)">
      <rect width="400" height="20" rx="4" fill="#070b16"/>
      <circle cx="12" cy="10" r="3" fill="{color}"/>
      <text x="22" y="14" fill="{color}" font-family="{FONT_MONO}" font-size="10" font-weight="600">{esc_stack}</text>
    </g>
  </g>
</svg>'''

# Generate all SVGs
files_to_write = {
    "connect-header.svg": build_connect_header(),
    "connect-linkedin.svg": build_connect_button("linkedin", "LinkedIn Profile", "in/abhishek-tiwariiii", "CONNECT", "#38bdf8", "#0a66c2"),
    "connect-portfolio.svg": build_connect_button("portfolio", "Personal Portfolio", "portfolio.getchintu.com", "EXPLORE", "#818cf8", "#6366f1"),
    "connect-chintu.svg": build_connect_button("chintu", "CHINTU AI Platform", "getchintu.com", "LAUNCH", "#c084fc", "#8b5cf6"),
    "connect-email.svg": build_connect_button("email", "Direct Email", "abhishektiwari@getchintu.com", "SEND MAIL", "#f87171", "#ea4335"),
    "more-projects-header.svg": build_more_projects_header(),
    "tile-tempusmail.svg": build_project_tile("Tempusmail", "Disposable email service with real-time webhooks", "Next.js · Firebase · Tailwind", "LIVE APP ↗", "#f97316"),
    "tile-myntra.svg": build_project_tile("Myntra Clone", "Fashion e-commerce platform & cart state flow", "React · Redux · CSS3", "LIVE APP ↗", "#ec4899"),
    "tile-kanban.svg": build_project_tile("Kanban WorkBoard", "Project board with drag-and-drop & Django backend", "Django · React · Redux", "LIVE APP ↗", "#38bdf8"),
    "tile-market.svg": build_project_tile("Market Seasonality Explorer", "Seasonal market trend calendar & visualizer", "React · Tailwind CSS", "LIVE APP ↗", "#eab308"),
    "tile-skillup.svg": build_project_tile("Skill Up", "Online interactive course & learning platform", "React · Firebase Auth", "LIVE APP ↗", "#10b981"),
    "tile-elante.svg": build_project_tile("Elante Mall", "Commercial shopping mall directory & showcase", "React · JavaScript · CSS", "LIVE APP ↗", "#a855f7")
}

# Validate XML and write
for filename, content in files_to_write.items():
    try:
        ET.fromstring(content)
        print(f"[OK] Valid XML: {filename}")
    except ET.ParseError as e:
        print(f"[ERROR] XML Error in {filename}: {e}")
        raise e

    # Write to repo assets
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)
    # Write to local workspace profile-assets
    with open(os.path.join(local_assets_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

print("\nAll 12 modular SVGs successfully validated and generated!")
