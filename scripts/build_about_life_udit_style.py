import io
import base64
import os
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

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 420" width="900" height="420" style="background:#070b16; border-radius:20px; font-family:{FONT_SANS};">
  <defs>
    <linearGradient id="al-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <pattern id="al-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
    <clipPath id="al-photo-clip">
      <rect width="130" height="150" rx="12"/>
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="900" height="420" rx="20" fill="#070b16"/>
  <rect width="900" height="420" fill="url(#al-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="418.5" rx="19.25" fill="none" stroke="url(#al-border)" stroke-width="1.5"/>

  <!-- ========================================================================= -->
  <!-- LEFT CARD: 01 / FROM THOUGHT TO THING (width: 385, height: 365) -->
  <!-- ========================================================================= -->
  <g transform="translate(45, 28)">
    <rect width="385" height="365" rx="16" fill="#0b1224" stroke="#1e293b" stroke-width="1.2"/>

    <!-- Section Header Tag -->
    <text x="24" y="32" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.2">
      01 / FROM THOUGHT TO THING
    </text>

    <!-- Main Title -->
    <text x="24" y="60" fill="#ffffff" font-size="20" font-weight="900" letter-spacing="0.5">
      IDEAS. BUILT DIFFERENT.
    </text>

    <!-- Browser / Terminal Mockup Container -->
    <g transform="translate(24, 82)">
      <rect width="337" height="128" rx="10" fill="#070b16" stroke="#1e293b" stroke-width="1"/>
      
      <!-- Window Controls (Traffic Lights) -->
      <circle cx="16" cy="16" r="4.5" fill="#ef4444"/>
      <circle cx="30" cy="16" r="4.5" fill="#eab308"/>
      <circle cx="44" cy="16" r="4.5" fill="#22c55e"/>

      <!-- URL Bar / Tab -->
      <rect x="62" y="7" width="180" height="18" rx="4" fill="#0b1224"/>
      <text x="72" y="19" fill="#64748b" font-family="{FONT_MONO}" font-size="9.5">github.com/Abhishek6827/build</text>

      <!-- Terminal Command -->
      <text x="16" y="48" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11.5" font-weight="600">
        &gt; turn_curiosity_into_impact()
      </text>

      <!-- 3 Workflow Boxes Connected With Arrows -->
      <g transform="translate(14, 66)">
        <!-- Step 1: Ideate -->
        <g transform="translate(0, 0)">
          <rect width="84" height="46" rx="6" fill="#0b1224" stroke="#247bff" stroke-width="1"/>
          <text x="10" y="20" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="800">01</text>
          <text x="10" y="36" fill="#ffffff" font-family="{FONT_MONO}" font-size="9" font-weight="700">IDEATE</text>
        </g>

        <!-- Arrow 1 -->
        <text x="94" y="28" fill="#475569" font-size="12" font-weight="bold" text-anchor="middle">→</text>

        <!-- Step 2: Engineer -->
        <g transform="translate(108, 0)">
          <rect width="94" height="46" rx="6" fill="#0b1224" stroke="#247bff" stroke-width="1"/>
          <text x="10" y="20" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="800">02</text>
          <text x="10" y="36" fill="#ffffff" font-family="{FONT_MONO}" font-size="9" font-weight="700">ENGINEER</text>
        </g>

        <!-- Arrow 2 -->
        <text x="212" y="28" fill="#475569" font-size="12" font-weight="bold" text-anchor="middle">→</text>

        <!-- Step 3: Ship (Glowing Red Accent) -->
        <g transform="translate(225, 0)">
          <rect width="84" height="46" rx="6" fill="#0b1224" stroke="#ff354f" stroke-width="1.4"/>
          <text x="10" y="20" fill="#ff354f" font-family="{FONT_MONO}" font-size="10" font-weight="800">03</text>
          <text x="10" y="36" fill="#ffffff" font-family="{FONT_MONO}" font-size="9" font-weight="700">SHIP</text>
        </g>
      </g>
    </g>

    <!-- 3 Capability Rows with Icons -->
    <g transform="translate(24, 226)">
      <!-- Row 1: Web & App Dev -->
      <g transform="translate(0, 0)">
        <text x="0" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="13" font-weight="bold">&lt;&gt;</text>
        <text x="22" y="16" fill="#ffffff" font-size="12.5" font-weight="700">Modern Web &amp; App Dev</text>
        <text x="22" y="31" fill="#94a3b8" font-size="10.5">From first interaction to production scalability.</text>
      </g>

      <!-- Row 2: AI & Cloud Integration -->
      <g transform="translate(0, 44)">
        <text x="0" y="16" fill="#38bdf8" font-size="13">☁️</text>
        <text x="22" y="16" fill="#ffffff" font-size="12.5" font-weight="700">AI &amp; Cloud Integration</text>
        <text x="22" y="31" fill="#94a3b8" font-size="10.5">Scalable cloud systems. Useful intelligence.</text>
      </g>

      <!-- Row 3: Architecture & Systems -->
      <g transform="translate(0, 88)">
        <text x="0" y="16" fill="#38bdf8" font-size="13">👥</text>
        <text x="22" y="16" fill="#ffffff" font-size="12.5" font-weight="700">Community &amp; Mentorship</text>
        <text x="22" y="31" fill="#94a3b8" font-size="10.5">Making the next step less uncertain for engineers.</text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- RIGHT CARD: 02 / LIFE OUTSIDE THE COMMIT (width: 405, height: 365) -->
  <!-- ========================================================================= -->
  <g transform="translate(450, 28)">
    <rect width="405" height="365" rx="16" fill="#0b1224" stroke="#1e293b" stroke-width="1.2"/>

    <!-- Section Header Tag -->
    <text x="24" y="32" fill="#ff354f" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.2">
      02 / LIFE OUTSIDE THE COMMIT
    </text>

    <!-- Main Title with Red & Blue Underline Strokes -->
    <text x="24" y="60" fill="#ffffff" font-size="20" font-weight="900" letter-spacing="0.5">
      MORE THAN A JOB TITLE.
    </text>
    <rect x="24" y="68" width="60" height="3" rx="1.5" fill="#247bff"/>
    <rect x="90" y="68" width="50" height="3" rx="1.5" fill="#ff354f"/>

    <!-- Content Card with Photo & 3 Core Principles -->
    <g transform="translate(24, 86)">
      <rect width="357" height="162" rx="12" fill="#070b16" stroke="#1e293b" stroke-width="1"/>

      <!-- Framed Photo on Left with Badge -->
      <g transform="translate(12, 10)">
        <g clip-path="url(#al-photo-clip)">
          <image href="data:image/png;base64,{photo_b64}" width="130" height="150" preserveAspectRatio="xMidYMid slice"/>
        </g>
        <rect width="130" height="150" rx="12" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.8"/>
        <!-- Badge at Bottom of Photo -->
        <g transform="translate(0, 126)">
          <rect width="130" height="24" rx="6" fill="#0b1224" stroke="#247bff" stroke-width="1" stroke-opacity="0.7"/>
          <text x="65" y="16" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9" font-weight="800" text-anchor="middle">
            ABHISHEK / FOUNDER
          </text>
        </g>
      </g>

      <!-- 3 Principles on Right Side of Photo -->
      <g transform="translate(156, 20)">
        <!-- Principle 1 -->
        <g transform="translate(0, 0)">
          <text x="0" y="18" fill="#ff354f" font-family="{FONT_MONO}" font-size="12" font-weight="800">01</text>
          <text x="28" y="18" fill="#ffffff" font-family="{FONT_MONO}" font-size="11" font-weight="700">FIND THE GAP</text>
          <text x="28" y="32" fill="#94a3b8" font-size="9.5">Spot user friction early.</text>
        </g>

        <!-- Principle 2 -->
        <g transform="translate(0, 44)">
          <text x="0" y="18" fill="#ff354f" font-family="{FONT_MONO}" font-size="12" font-weight="800">02</text>
          <text x="28" y="18" fill="#ffffff" font-family="{FONT_MONO}" font-size="11" font-weight="700">BUILD YOUR PLAN</text>
          <text x="28" y="32" fill="#94a3b8" font-size="9.5">Architect before you code.</text>
        </g>

        <!-- Principle 3 -->
        <g transform="translate(0, 88)">
          <text x="0" y="18" fill="#ff354f" font-family="{FONT_MONO}" font-size="12" font-weight="800">03</text>
          <text x="28" y="18" fill="#ffffff" font-family="{FONT_MONO}" font-size="11" font-weight="700">TAKE THE LEAP</text>
          <text x="28" y="32" fill="#94a3b8" font-size="9.5">Ship with relentless drive.</text>
        </g>
      </g>
    </g>

    <!-- Bottom Mentorship Callout: MAKE THE NEXT MOVE -->
    <g transform="translate(24, 264)">
      <text x="0" y="14" fill="#64748b" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">
        MAKE THE NEXT MOVE.
      </text>
      <text x="0" y="42" fill="#ffffff" font-size="18" font-weight="900">
        1:1 Career Mentorship
      </text>
      <text x="0" y="64" fill="#38bdf8" font-size="11.5">
        A clearer roadmap. A stronger engineer.
      </text>

      <!-- Counter Badge -->
      <text x="355" y="64" fill="#475569" font-family="{FONT_MONO}" font-size="10" font-weight="700" text-anchor="end">
        02 / 03
      </text>
    </g>
  </g>
</svg>'''

out_path = r'd:\Desktop\Resume-Extension\profile-assets\about-life.svg'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(svg)

ET.parse(out_path)
print("Successfully generated about-life.svg matching Screenshot 1! Valid XML!")
