import json
import os
import io
import base64
import xml.etree.ElementTree as ET
from PIL import Image

def get_optimized_b64(path, size=(220, 220)):
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('ascii')

photo_b64 = get_optimized_b64(r'd:\Desktop\Resume-Extension\profile-assets\id.png')

FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 480" width="900" height="480" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
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
    <linearGradient id="id-bar-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <clipPath id="id-avatar-circle">
      <circle cx="110" cy="115" r="48"/>
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
      0% {{ transform: rotate(-6deg); }}
      8% {{ transform: rotate(5deg); }}
      16% {{ transform: rotate(-3.5deg); }}
      24% {{ transform: rotate(2.2deg); }}
      32% {{ transform: rotate(-1.5deg); }}
      40% {{ transform: rotate(1.5deg); }}
      48% {{ transform: rotate(-1.5deg); }}
      56% {{ transform: rotate(1.5deg); }}
      64% {{ transform: rotate(-1.5deg); }}
      72% {{ transform: rotate(1.5deg); }}
      80% {{ transform: rotate(-1.5deg); }}
      88% {{ transform: rotate(1.5deg); }}
      96% {{ transform: rotate(-1.5deg); }}
      100% {{ transform: rotate(-6deg); }}
    }}
  </style>

  <!-- Background Base -->
  <rect width="900" height="480" rx="20" fill="#070b16"/>
  <rect width="900" height="480" fill="url(#id-dash-glow)"/>
  <rect width="900" height="480" fill="url(#id-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="478.5" rx="19.25" fill="none" stroke="url(#id-border)" stroke-width="1.5"/>

  <!-- Top Header Title: Matching Screenshot 2 (06 // BUILDER PASS) -->
  <g transform="translate(50, 26)">
    <rect width="180" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="90" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      06 // BUILDER PASS
    </text>
    <text x="240" y="16" fill="#475569" font-family="{FONT_MONO}" font-size="11" font-weight="700">AT-6827</text>
  </g>

  <!-- LEFT: PHYSICAL LANYARD & ID BADGE ASSEMBLY (Center X: 195) -->
  <g class="id-lanyard-assembly">
    <!-- Woven Fabric Lanyard Straps -->
    <path d="M 175 -20 L 188 56 L 202 56 L 215 -20 Z" fill="url(#id-lanyard-strap)"/>
    <path d="M 188 56 L 195 72 L 202 56 Z" fill="#0b1224"/>

    <!-- Metal Lobster Clasp & Ring -->
    <g transform="translate(195, 74)">
      <circle cx="0" cy="0" r="10" fill="none" stroke="url(#id-metal-clasp)" stroke-width="3"/>
      <path d="M -6 6 L 6 6 L 4 16 L -4 16 Z" fill="url(#id-metal-clasp)"/>
      <rect x="-8" y="16" width="16" height="5" rx="2" fill="#334155"/>
      <rect x="-10" y="21" width="20" height="7" rx="3" fill="#0f172a" stroke="#334155" stroke-width="0.8"/>
    </g>

    <!-- Plastic ID Card Body (220 x 330) -->
    <g transform="translate(85, 102)">
      <rect width="220" height="330" rx="16" fill="#0b1224" stroke="#1e293b" stroke-width="1.2"/>
      <rect x="0.75" y="0.75" width="218.5" height="328.5" rx="15.25" fill="none" stroke="#247bff" stroke-width="1" stroke-opacity="0.4"/>

      <!-- Slot Punch Hole -->
      <rect x="92" y="10" width="36" height="6" rx="3" fill="#070b16" stroke="#1e293b" stroke-width="1"/>

      <!-- Company & Live Pass Header -->
      <g transform="translate(18, 30)">
        <text x="0" y="14" fill="#ffffff" font-family="{FONT_MONO}" font-size="11" font-weight="800" letter-spacing="0.5">CHINTU AI</text>
        <rect x="130" y="2" width="56" height="16" rx="4" fill="#070b16" stroke="#22c55e" stroke-width="0.8"/>
        <text x="158" y="13" fill="#22c55e" font-family="{FONT_MONO}" font-size="8.5" font-weight="700" text-anchor="middle">LIVE PASS</text>
      </g>

      <!-- Avatar Photo Frame -->
      <g transform="translate(0, 0)">
        <circle cx="110" cy="115" r="50" fill="none" stroke="#247bff" stroke-width="2"/>
        <g clip-path="url(#id-avatar-circle)">
          <image href="data:image/png;base64,{photo_b64}" x="60" y="65" width="100" height="100" preserveAspectRatio="xMidYMid slice"/>
        </g>
      </g>

      <!-- Dev Details -->
      <g transform="translate(110, 185)" text-anchor="middle">
        <text x="0" y="0" fill="#ffffff" font-size="15" font-weight="800">ABHISHEK TIWARI</text>
        <text x="0" y="18" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9.5" font-weight="600">FOUNDER &amp; FULL-STACK LEAD</text>
        <text x="0" y="32" fill="#64748b" font-family="{FONT_MONO}" font-size="8.5">LUCKNOW // INDIA</text>
      </g>

      <!-- Gold Chip -->
      <g transform="translate(20, 235)">
        <rect x="0" y="0" width="28" height="20" rx="4" fill="#ca8a04" stroke="#eab308" stroke-width="0.8"/>
        <line x1="8" y1="0" x2="8" y2="20" stroke="#a16207" stroke-width="0.8"/>
        <line x1="20" y1="0" x2="20" y2="20" stroke="#a16207" stroke-width="0.8"/>
        <text x="38" y="14" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">AUTHENTICATED KEY</text>
      </g>

      <!-- Barcode Lines -->
      <g transform="translate(20, 268)">
        <rect x="0" y="0" width="3" height="28" fill="#f8fafc"/>
        <rect x="5" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="9" y="0" width="4" height="28" fill="#f8fafc"/>
        <rect x="16" y="0" width="2" height="28" fill="#f8fafc"/>
        <rect x="21" y="0" width="1" height="28" fill="#f8fafc"/>
        <rect x="25" y="0" width="3" height="28" fill="#f8fafc"/>
        <rect x="31" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="35" y="0" width="4.5" height="28" fill="#f8fafc"/>
        <rect x="42" y="0" width="2" height="28" fill="#f8fafc"/>
        <rect x="47" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="51" y="0" width="3" height="28" fill="#f8fafc"/>
        <rect x="56" y="0" width="2" height="28" fill="#f8fafc"/>
        <rect x="61" y="0" width="4" height="28" fill="#f8fafc"/>
        <rect x="68" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="72" y="0" width="2" height="28" fill="#f8fafc"/>
        <rect x="76" y="0" width="3.5" height="28" fill="#f8fafc"/>
        <rect x="83" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="87" y="0" width="4" height="28" fill="#f8fafc"/>
        <rect x="94" y="0" width="2" height="28" fill="#f8fafc"/>
        <rect x="99" y="0" width="3" height="28" fill="#f8fafc"/>
        <rect x="105" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="109" y="0" width="4" height="28" fill="#f8fafc"/>
        <rect x="116" y="0" width="2" height="28" fill="#f8fafc"/>
        <rect x="121" y="0" width="3" height="28" fill="#f8fafc"/>
        <rect x="127" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="131" y="0" width="4" height="28" fill="#f8fafc"/>
        <rect x="138" y="0" width="2.5" height="28" fill="#f8fafc"/>
        <rect x="144" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="148" y="0" width="3" height="28" fill="#f8fafc"/>
        <rect x="154" y="0" width="2" height="28" fill="#f8fafc"/>
        <rect x="159" y="0" width="4" height="28" fill="#f8fafc"/>
        <rect x="166" y="0" width="1.5" height="28" fill="#f8fafc"/>
        <rect x="170" y="0" width="2.5" height="28" fill="#f8fafc"/>
        <rect x="175" y="0" width="4" height="28" fill="#f8fafc"/>
        <text x="90" y="38" fill="#64748b" font-family="{FONT_MONO}" font-size="8" text-anchor="middle">AT-BUILDER-ID-6827</text>
      </g>
    </g>
  </g>

  <!-- RIGHT: MATCHING SCREENSHOT 2 (Stats Boxes + Most-Starred Repos + Now Badge) -->
  <g transform="translate(345, 65)">
    <!-- 3 Stat Metric Boxes Side by Side -->
    <g transform="translate(0, 0)">
      <!-- Box 1: Contributions -->
      <g transform="translate(0, 0)">
        <rect width="160" height="64" rx="10" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
        <text x="18" y="22" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700">CONTRIBUTIONS</text>
        <text x="18" y="48" fill="#ff354f" font-family="{FONT_MONO}" font-size="22" font-weight="900">3,558+</text>
        <text x="100" y="48" fill="#64748b" font-family="{FONT_MONO}" font-size="9">LIFETIME</text>
      </g>

      <!-- Box 2: Repositories -->
      <g transform="translate(175, 0)">
        <rect width="160" height="64" rx="10" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
        <text x="18" y="22" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700">REPOSITORIES</text>
        <text x="18" y="48" fill="#38bdf8" font-family="{FONT_MONO}" font-size="22" font-weight="900">33</text>
        <text x="65" y="48" fill="#64748b" font-family="{FONT_MONO}" font-size="9">PUBLIC GITHUB</text>
      </g>

      <!-- Box 3: Stars -->
      <g transform="translate(350, 0)">
        <rect width="150" height="64" rx="10" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
        <text x="18" y="22" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700">REPO STARS</text>
        <text x="18" y="48" fill="#34d399" font-family="{FONT_MONO}" font-size="22" font-weight="900">34</text>
        <text x="60" y="48" fill="#64748b" font-family="{FONT_MONO}" font-size="9">RECEIVED</text>
      </g>
    </g>

    <!-- Section Header: MOST-STARRED / PUBLIC REPOSITORIES -->
    <text x="0" y="96" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">
      MOST-STARRED / FEATURED REPOSITORIES
    </text>

    <!-- 4 Progress Bar Rows Matching Screenshot 2 -->
    <g transform="translate(0, 110)">
      <!-- Row 1: Resume-Extension (Java + AWS) -->
      <g transform="translate(0, 0)">
        <text x="0" y="0" fill="#e2e8f0" font-family="{FONT_MONO}" font-size="11.5" font-weight="600">Resume-Extension (Java Spring Boot + AWS)</text>
        <rect y="6" width="500" height="6" rx="3" fill="#1e293b"/>
        <rect y="6" width="475" height="6" rx="3" fill="url(#id-bar-grad)"/>
      </g>

      <!-- Row 2: getchintu.com -->
      <g transform="translate(0, 36)">
        <text x="0" y="0" fill="#e2e8f0" font-family="{FONT_MONO}" font-size="11.5" font-weight="600">getchintu.com (AI Career Copilot Platform)</text>
        <rect y="6" width="500" height="6" rx="3" fill="#1e293b"/>
        <rect y="6" width="445" height="6" rx="3" fill="url(#id-bar-grad)"/>
      </g>

      <!-- Row 3: SocialConnect -->
      <g transform="translate(0, 72)">
        <text x="0" y="0" fill="#e2e8f0" font-family="{FONT_MONO}" font-size="11.5" font-weight="600">SocialConnect (Real-Time WebRTC &amp; Chat)</text>
        <rect y="6" width="500" height="6" rx="3" fill="#1e293b"/>
        <rect y="6" width="395" height="6" rx="3" fill="url(#id-bar-grad)"/>
      </g>

      <!-- Row 4: YouTube Automation -->
      <g transform="translate(0, 108)">
        <text x="0" y="0" fill="#e2e8f0" font-family="{FONT_MONO}" font-size="11.5" font-weight="600">yt-automation (Gemini Vision + Drive API)</text>
        <rect y="6" width="500" height="6" rx="3" fill="#1e293b"/>
        <rect y="6" width="345" height="6" rx="3" fill="url(#id-bar-grad)"/>
      </g>
    </g>

    <!-- Bottom "NOW" Badge & Announcement Matching Screenshot 2 -->
    <g transform="translate(0, 276)">
      <rect width="46" height="20" rx="4" fill="#ff354f"/>
      <text x="23" y="14" fill="#ffffff" font-family="{FONT_MONO}" font-size="10" font-weight="800" text-anchor="middle">NOW</text>
      
      <text x="56" y="15" fill="#ffffff" font-size="13.5" font-weight="800">Building cross-platform AI at CHINTU AI</text>
      <text x="0" y="36" fill="#94a3b8" font-size="11">Architecting multi-model LLM copilot workflows &amp; high-throughput cloud engines.</text>
    </g>

    <!-- Bottom Watermark Matching Screenshot 2 -->
    <text x="0" y="358" fill="#1e293b" font-family="{FONT_MONO}" font-size="15" font-weight="900" letter-spacing="2">
      BEHIND THE CODE.
    </text>
  </g>
</svg>'''

out_path = r'd:\Desktop\Resume-Extension\profile-assets\id-dashboard.svg'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(svg)

ET.parse(out_path)
print("Successfully generated id-dashboard.svg matching Screenshot 2! Valid XML!")
