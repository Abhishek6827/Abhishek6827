"""
Generate the uniform SVG suite for Abhishek Tiwari's GitHub profile.
Creates:
1. battle-log.svg (04 // BATTLE LOG - Timeline with 5 companies)
2. project-chintu.svg (05 // FLAGSHIP 01)
3. project-resume.svg (05 // FLAGSHIP 02 - AWS + Java Spring Boot)
4. project-social.svg (05 // FLAGSHIP 03)
5. project-youtube.svg (05 // FLAGSHIP 04)
6. more-projects.svg (06 // ECOSYSTEM REPOSITORY - 6 tiles)
7. stats-header.svg (07 // STATS THAT SPEAK - Section Header)
8. certifications.svg (08 // VERIFIED CREDENTIALS - 3 accreditation cards)
"""

import json
import os
import html
import xml.sax.saxutils

def esc(s):
    if not isinstance(s, str):
        return s
    # unescape any existing HTML entities first, then cleanly XML-escape
    s = html.unescape(s)
    return xml.sax.saxutils.escape(s)

icons_path = r"d:\Desktop\Resume-Extension\profile-assets\icons_data.json"
with open(icons_path, "r", encoding="utf-8") as f:
    ICONS = json.load(f)

def render_pill(name, x, y, border_color="#38bdf8", fill_color="#0b1224", text_color="#ffffff"):
    icon_info = ICONS.get(name, {})
    path_d = icon_info.get("d", "")
    icon_color = icon_info.get("color", "#38bdf8")
    is_multi = icon_info.get("is_multi_path", False)
    viewBox = icon_info.get("viewBox", "0 0 24 24")
    
    # dynamic width
    text_len = len(name)
    width = max(88, int(30 + text_len * 7.5 + 16))
    height = 26
    rx = 13
    
    # SVG snippet
    svg = f'<g transform="translate({x}, {y})">'
    svg += f'<rect width="{width}" height="{height}" rx="{rx}" fill="{fill_color}" stroke="{border_color}" stroke-width="1.2" stroke-opacity="0.9"/>'
    
    # Render icon
    if is_multi:
        paths_html = "".join([f'<path fill="{p.get("fill", "#fff")}" d="{p.get("d", "")}"/>' for p in icon_info.get("paths", [])])
        svg += f'<svg x="10" y="5" width="16" height="16" viewBox="{viewBox}">{paths_html}</svg>'
    elif path_d:
        svg += f'<svg x="10" y="5" width="16" height="16" viewBox="{viewBox}" fill="{icon_color}"><path d="{path_d}"/></svg>'
    else:
        svg += f'<circle cx="18" cy="13" r="5" fill="{border_color}"/>'
        
    svg += f'<text x="32" y="17" fill="{text_color}" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-size="11" font-weight="700">{esc(name)}</text>'
    svg += '</g>'
    return svg, width

# -------------------------------------------------------------
# 1. BATTLE LOG SVG (width: 900, height: 530)
# -------------------------------------------------------------
def build_battle_log():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 530" width="900" height="530" style="background:#070b16; border-radius:20px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="bl-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <pattern id="bl-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
    <linearGradient id="bl-timeline-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="25%" stop-color="#f59e0b"/>
      <stop offset="50%" stop-color="#34d399"/>
      <stop offset="75%" stop-color="#a78bfa"/>
      <stop offset="100%" stop-color="#f43f5e"/>
    </linearGradient>
  </defs>

  <!-- Background Base -->
  <rect width="900" height="530" rx="20" fill="#070b16"/>
  <rect width="900" height="530" fill="url(#bl-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="528.5" rx="19.25" fill="none" stroke="url(#bl-border)" stroke-width="1.5"/>

  <!-- Top Header Title -->
  <g transform="translate(50, 32)">
    <rect width="170" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="85" y="16" fill="#38bdf8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      03 // BATTLE LOG
    </text>
    <text x="185" y="16" fill="#94a3b8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11">CAREER TIMELINE &amp; PRODUCTION IMPACT</text>

    <!-- Top Right Active Badge -->
    <g transform="translate(630, 0)">
      <rect width="170" height="24" rx="6" fill="#0b1224" stroke="#10b981" stroke-width="1" stroke-opacity="0.8"/>
      <circle cx="16" cy="12" r="4" fill="#10b981"/>
      <text x="28" y="16" fill="#34d399" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="0.5">ACTIVE CONTRIBUTOR</text>
    </g>
  </g>

  <!-- Vertical Timeline Spine -->
  <line x1="85" y1="88" x2="85" y2="475" stroke="url(#bl-timeline-grad)" stroke-width="2.5" stroke-dasharray="4 3" stroke-opacity="0.6"/>

  <!-- 5 Career Milestones -->
'''
    milestones = [
        {
            "y": 80,
            "role": "Founder & Full-Stack Developer",
            "company": "CHINTU AI",
            "dates": "02/2026 – Present",
            "date_bg": "#0e172a",
            "date_color": "#38bdf8",
            "dot_color": "#38bdf8",
            "desc": "Built cross-platform AI Career Copilot (Desktop DMG/EXE + Android APK + Web). Multi-model LLM orchestration (Groq <200ms, OpenAI), voice synthesis & 3-tier Razorpay billing."
        },
        {
            "y": 165,
            "role": "Full Stack Developer",
            "company": "Indian Capital & Investment Ltd.",
            "dates": "11/2025 – 02/2026",
            "date_bg": "#0e172a",
            "date_color": "#f59e0b",
            "dot_color": "#f59e0b",
            "desc": "Architected automated payment pipelines (Stripe + Zoho), webhooks & Resend notifications. Built Notion API workflows for real-time asset intelligence."
        },
        {
            "y": 248,
            "role": "Software Developer",
            "company": "Vasnaani Education",
            "dates": "08/2024 – 10/2025",
            "date_bg": "#0e172a",
            "date_color": "#34d399",
            "dot_color": "#34d399",
            "desc": "Led development of official education portal with Django REST APIs & React frontend. Optimized bundle performance and resolved critical UI/UX bottlenecks."
        },
        {
            "y": 331,
            "role": "Full-Stack Developer Intern",
            "company": "Hoping Minds",
            "dates": "01/2024 – 06/2024",
            "date_bg": "#0e172a",
            "date_color": "#a78bfa",
            "dot_color": "#a78bfa",
            "desc": "Delivered responsive full-stack features in cross-functional agile sprints. Standardized Redux state management and clean modular UI components."
        },
        {
            "y": 414,
            "role": "Web Developer",
            "company": "Quizario",
            "dates": "11/2023 – 12/2023",
            "date_bg": "#0e172a",
            "date_color": "#f43f5e",
            "dot_color": "#f43f5e",
            "desc": "Created interactive assessment & quiz platform with real-time scoring, secure student authentication, state persistence, and responsive layouts."
        }
    ]

    for m in milestones:
        y = m["y"]
        svg += f'''
  <!-- Milestone: {esc(m["company"])} -->
  <g transform="translate(50, {y})">
    <!-- Glowing Timeline Node -->
    <circle cx="35" cy="20" r="10" fill="#070b16" stroke="{m["dot_color"]}" stroke-width="2.5"/>
    <circle cx="35" cy="20" r="4" fill="{m["dot_color"]}"/>

    <!-- Content Card -->
    <rect x="58" y="0" width="742" height="74" rx="10" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>

    <!-- Role & Company -->
    <text x="74" y="22" fill="#ffffff" font-size="14.5" font-weight="700">{esc(m["role"])}</text>
    <text x="74" y="40" fill="{m["dot_color"]}" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="12" font-weight="600">⚡ {esc(m["company"])}</text>

    <!-- Date Badge (Right Aligned) -->
    <g transform="translate(600, 10)">
      <rect width="130" height="22" rx="5" fill="{m["date_bg"]}" stroke="{m["date_color"]}" stroke-width="0.9" stroke-opacity="0.7"/>
      <text x="65" y="15" fill="{m["date_color"]}" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="600" text-anchor="middle">📅 {esc(m["dates"])}</text>
    </g>

    <!-- Description -->
    <text x="74" y="58" fill="#94a3b8" font-size="11.5">{esc(m["desc"])}</text>
  </g>
'''

    svg += '</svg>'
    return svg

# -------------------------------------------------------------
# 2. FLAGSHIP PROJECT CARD BUILDER (width: 900, height: 250)
# -------------------------------------------------------------
def build_project_card(index_str, title, subtitle, highlights, techs, cta_text, cta_link, accent_color="#38bdf8", border_glow="#247bff"):
    safe_id = index_str.replace(" ", "_").replace("/", "_")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 250" width="900" height="250" style="background:#070b16; border-radius:20px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="p-border-{safe_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{border_glow}" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="{border_glow}" stop-opacity="0.3"/>
    </linearGradient>
    <pattern id="p-dots-{safe_id}" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <!-- Background Base -->
  <rect width="900" height="250" rx="20" fill="#070b16"/>
  <rect width="900" height="250" fill="url(#p-dots-{safe_id})"/>
  <rect x="0.75" y="0.75" width="898.5" height="248.5" rx="19.25" fill="none" stroke="url(#p-border-{safe_id})" stroke-width="1.5"/>

  <!-- Left Accent Bar -->
  <rect x="2" y="24" width="4" height="202" rx="2" fill="{accent_color}"/>

  <!-- Top Header Title & CTA -->
  <g transform="translate(50, 26)">
    <rect width="180" height="24" rx="6" fill="#0e172a" stroke="{border_glow}" stroke-width="1" stroke-opacity="0.6"/>
    <text x="90" y="16" fill="{accent_color}" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="1.2">
      {esc(index_str)}
    </text>

    <!-- CTA Button on Right -->
    <a xlink:href="{esc(cta_link)}" target="_blank" style="cursor: pointer;">
      <g transform="translate(630, 0)">
        <rect width="170" height="26" rx="6" fill="#0b1224" stroke="{accent_color}" stroke-width="1.2"/>
        <text x="85" y="17" fill="{accent_color}" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11" font-weight="800" text-anchor="middle" letter-spacing="0.5">
          {esc(cta_text)}
        </text>
      </g>
    </a>
  </g>

  <!-- Project Title & Subtitle -->
  <g transform="translate(50, 68)">
    <text x="0" y="20" fill="#ffffff" font-size="19" font-weight="800">{esc(title)}</text>
    <text x="0" y="42" fill="{accent_color}" font-size="12.5" font-style="italic">"{esc(subtitle)}"</text>
  </g>

  <!-- 4 Architectural Highlights (2x2 Grid) -->
  <g transform="translate(50, 126)">
    <!-- Row 1 -->
    <g transform="translate(0, 0)">
      <rect width="385" height="30" rx="6" fill="#0b1224" stroke="#1e293b" stroke-width="0.9"/>
      <text x="12" y="19" fill="#e2e8f0" font-size="11.5">{esc(highlights[0])}</text>
    </g>
    <g transform="translate(415, 0)">
      <rect width="385" height="30" rx="6" fill="#0b1224" stroke="#1e293b" stroke-width="0.9"/>
      <text x="12" y="19" fill="#e2e8f0" font-size="11.5">{esc(highlights[1])}</text>
    </g>

    <!-- Row 2 -->
    <g transform="translate(0, 38)">
      <rect width="385" height="30" rx="6" fill="#0b1224" stroke="#1e293b" stroke-width="0.9"/>
      <text x="12" y="19" fill="#e2e8f0" font-size="11.5">{esc(highlights[2])}</text>
    </g>
    <g transform="translate(415, 38)">
      <rect width="385" height="30" rx="6" fill="#0b1224" stroke="#1e293b" stroke-width="0.9"/>
      <text x="12" y="19" fill="#e2e8f0" font-size="11.5">{esc(highlights[3])}</text>
    </g>
  </g>

  <!-- Bottom Tech Stack Pills Row -->
  <g transform="translate(50, 206)">
'''
    current_x = 0
    for t in techs:
        pill_svg, pill_w = render_pill(t, current_x, 0, border_color=accent_color)
        svg += pill_svg + "\n"
        current_x += pill_w + 10

    svg += '''  </g>
</svg>'''
    return svg

# -------------------------------------------------------------
# 3. MORE PROJECTS SVG (width: 900, height: 320)
# -------------------------------------------------------------
def build_more_projects():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 320" width="900" height="320" style="background:#070b16; border-radius:20px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="mp-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <pattern id="mp-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <!-- Background Base -->
  <rect width="900" height="320" rx="20" fill="#070b16"/>
  <rect width="900" height="320" fill="url(#mp-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="318.5" rx="19.25" fill="none" stroke="url(#mp-border)" stroke-width="1.5"/>

  <!-- Top Header Title -->
  <g transform="translate(50, 28)">
    <rect width="210" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="105" y="16" fill="#38bdf8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="1.2">
      05 // ECOSYSTEM APPS
    </text>
    <text x="225" y="16" fill="#94a3b8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11">ADDITIONAL PRODUCTION DEPLOYMENTS</text>

    <!-- Right Header CTA -->
    <a xlink:href="https://portfolio.getchintu.com" target="_blank" style="cursor: pointer;">
      <g transform="translate(630, 0)">
        <rect width="170" height="24" rx="6" fill="#0b1224" stroke="#6366f1" stroke-width="1.1"/>
        <text x="85" y="16" fill="#818cf8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="700" text-anchor="middle">EXPLORE ALL APPS ↗</text>
      </g>
    </a>
  </g>

  <!-- 6 Tiles in 3 Cols x 2 Rows -->
  <g transform="translate(50, 72)">
'''
    tiles = [
        {"col": 0, "row": 0, "name": "Tempusmail", "desc": "Disposable email service with real-time webhooks", "stack": "Next.js · Firebase · Tailwind", "link": "https://tempomail.getchintu.com", "badge": "LIVE ↗", "color": "#f97316"},
        {"col": 1, "row": 0, "name": "Myntra Clone", "desc": "Fashion e-commerce platform & cart state flow", "stack": "React · Redux · CSS3", "link": "https://abhishek6827.github.io/E-commerce/", "badge": "LIVE ↗", "color": "#ec4899"},
        {"col": 2, "row": 0, "name": "Kanban WorkBoard", "desc": "Project board with drag-and-drop & Django backend", "stack": "Django · React · Redux", "link": "https://abhishek6827.github.io/Kanban_WorkBoard/", "badge": "LIVE ↗", "color": "#38bdf8"},
        {"col": 0, "row": 1, "name": "Market Explorer", "desc": "Seasonal market trend calendar & visualizer", "stack": "React · Tailwind CSS", "link": "https://abhishek6827.github.io/Market-Seasonality-Explorer/", "badge": "LIVE ↗", "color": "#eab308"},
        {"col": 1, "row": 1, "name": "Skill Up", "desc": "Online interactive course & learning platform", "stack": "React · Firebase Auth", "link": "https://abhishek6827.github.io/Skill_Up/", "badge": "LIVE ↗", "color": "#10b981"},
        {"col": 2, "row": 1, "name": "Elante Mall", "desc": "Commercial shopping mall directory & showcase", "stack": "React · JavaScript · CSS", "link": "https://abhishek6827.github.io/Elante_Mall/", "badge": "LIVE ↗", "color": "#a855f7"}
    ]

    col_w = 256
    row_h = 105
    for t in tiles:
        x = t["col"] * (col_w + 16)
        y = t["row"] * (row_h + 14)
        svg += f'''
    <!-- Tile: {esc(t["name"])} -->
    <a xlink:href="{esc(t["link"])}" target="_blank" style="cursor: pointer;">
      <g transform="translate({x}, {y})">
        <rect width="{col_w}" height="{row_h}" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
        <text x="16" y="24" fill="#ffffff" font-size="14.5" font-weight="700">{esc(t["name"])}</text>

        <!-- Mini Link Badge -->
        <g transform="translate({col_w - 75}, 12)">
          <rect width="60" height="18" rx="4" fill="#0e172a" stroke="{t["color"]}" stroke-width="0.8"/>
          <text x="30" y="13" fill="{t["color"]}" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="9" font-weight="700" text-anchor="middle">{esc(t["badge"])}</text>
        </g>

        <text x="16" y="48" fill="#94a3b8" font-size="11">{esc(t["desc"])}</text>
        <rect x="16" y="72" width="{col_w - 32}" height="20" rx="4" fill="#070b16"/>
        <text x="24" y="86" fill="{t["color"]}" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10" font-weight="600">{esc(t["stack"])}</text>
      </g>
    </a>
'''

    svg += '''  </g>
</svg>'''
    return svg

# -------------------------------------------------------------
# 4. STATS HEADER SVG (width: 900, height: 90)
# -------------------------------------------------------------
def build_stats_header():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 90" width="900" height="90" style="background:#070b16; border-radius:20px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="sh-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <pattern id="sh-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <!-- Background Base -->
  <rect width="900" height="90" rx="20" fill="#070b16"/>
  <rect width="900" height="90" fill="url(#sh-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="88.5" rx="19.25" fill="none" stroke="url(#sh-border)" stroke-width="1.5"/>

  <!-- Content -->
  <g transform="translate(50, 32)">
    <rect width="210" height="26" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.6"/>
    <text x="105" y="17" fill="#38bdf8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5">
      06 // STATS THAT SPEAK
    </text>
    <text x="228" y="18" fill="#94a3b8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11.5">REAL-TIME GITHUB INTELLIGENCE &amp; STREAKS</text>

    <!-- Right Live Counter Badge -->
    <g transform="translate(630, 0)">
      <rect width="170" height="26" rx="6" fill="#0b1224" stroke="#a855f7" stroke-width="1"/>
      <circle cx="16" cy="13" r="4" fill="#a855f7"/>
      <text x="28" y="17" fill="#c084fc" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="700">VERIFIED METRICS ⚡</text>
    </g>
  </g>
</svg>'''
    return svg

# -------------------------------------------------------------
# 5. CERTIFICATIONS SVG (width: 900, height: 210)
# -------------------------------------------------------------
def build_certifications():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 210" width="900" height="210" style="background:#070b16; border-radius:20px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="cert-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
    <pattern id="cert-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <!-- Background Base -->
  <rect width="900" height="210" rx="20" fill="#070b16"/>
  <rect width="900" height="210" fill="url(#cert-dots)"/>
  <rect x="0.75" y="0.75" width="898.5" height="208.5" rx="19.25" fill="none" stroke="url(#cert-border)" stroke-width="1.5"/>

  <!-- Top Header Title -->
  <g transform="translate(50, 24)">
    <rect width="210" height="24" rx="6" fill="#0e172a" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="105" y="16" fill="#38bdf8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="1.2">
      07 // ACCREDITATIONS
    </text>
    <text x="225" y="16" fill="#94a3b8" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11">VERIFIED INDUSTRY CERTIFICATIONS</text>
  </g>

  <!-- 3 Credential Cards Side by Side -->
  <g transform="translate(50, 64)">
    <!-- Cert 1: Meta -->
    <g transform="translate(0, 0)">
      <rect width="254" height="120" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <g transform="translate(16, 16)">
        <rect width="80" height="22" rx="5" fill="#0668e1"/>
        <text x="40" y="15" fill="#ffffff" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11" font-weight="700" text-anchor="middle">META</text>
        <rect x="156" y="0" width="66" height="22" rx="5" fill="#0e172a" stroke="#0668e1" stroke-width="0.8"/>
        <text x="189" y="15" fill="#60a5fa" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="600" text-anchor="middle">2025</text>
      </g>
      <text x="16" y="66" fill="#ffffff" font-size="14" font-weight="700">React Developer</text>
      <text x="16" y="84" fill="#94a3b8" font-size="11">Component Architecture &amp; State</text>
      <text x="16" y="104" fill="#38bdf8" font-size="10.5" font-weight="600">✓ Verified Certification</text>
    </g>

    <!-- Cert 2: FCC Full Stack -->
    <g transform="translate(273, 0)">
      <rect width="254" height="120" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <g transform="translate(16, 16)">
        <rect width="80" height="22" rx="5" fill="#0a0a23" stroke="#f59e0b" stroke-width="0.9"/>
        <text x="40" y="15" fill="#fbbf24" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11" font-weight="700" text-anchor="middle">FCC</text>
        <rect x="156" y="0" width="66" height="22" rx="5" fill="#0e172a" stroke="#f59e0b" stroke-width="0.8"/>
        <text x="189" y="15" fill="#fbbf24" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="600" text-anchor="middle">2024</text>
      </g>
      <text x="16" y="66" fill="#ffffff" font-size="14" font-weight="700">Full Stack Web Dev</text>
      <text x="16" y="84" fill="#94a3b8" font-size="11">Enterprise Backends &amp; APIs</text>
      <text x="16" y="104" fill="#f59e0b" font-size="10.5" font-weight="600">✓ Verified Accreditation</text>
    </g>

    <!-- Cert 3: FCC Algorithms -->
    <g transform="translate(546, 0)">
      <rect width="254" height="120" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1"/>
      <g transform="translate(16, 16)">
        <rect width="80" height="22" rx="5" fill="#0a0a23" stroke="#10b981" stroke-width="0.9"/>
        <text x="40" y="15" fill="#34d399" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="11" font-weight="700" text-anchor="middle">FCC</text>
        <rect x="156" y="0" width="66" height="22" rx="5" fill="#0e172a" stroke="#10b981" stroke-width="0.8"/>
        <text x="189" y="15" fill="#34d399" font-family="'Fira Code', 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace" font-size="10.5" font-weight="600" text-anchor="middle">2023</text>
      </g>
      <text x="16" y="66" fill="#ffffff" font-size="14" font-weight="700">JS Algorithms &amp; DSA</text>
      <text x="16" y="84" fill="#94a3b8" font-size="11">Data Structures &amp; Complexity</text>
      <text x="16" y="104" fill="#34d399" font-size="10.5" font-weight="600">✓ Verified Competency</text>
    </g>
  </g>
</svg>'''
    return svg

# Write all SVGs to profile-assets
out_dir = r"d:\Desktop\Resume-Extension\profile-assets"

# 1. Battle log
with open(os.path.join(out_dir, "battle-log.svg"), "w", encoding="utf-8") as f:
    f.write(build_battle_log())
print("Built battle-log.svg")

# 2. Project 1: CHINTU AI
chintu_highlights = [
    "🤖 Multi-Model: Groq (<200ms), OpenAI & Alibaba",
    "🎙️ Voice & Vision: Space-to-talk voice & OCR parser",
    "💳 Subscriptions: 3-tier Razorpay billing & webhooks",
    "🖥️ Cross-Platform: Electron (Mac/Win) + Android APK + Web"
]
with open(os.path.join(out_dir, "project-chintu.svg"), "w", encoding="utf-8") as f:
    f.write(build_project_card(
        index_str="04 // FLAGSHIP 01",
        title="CHINTU AI — Real-Time Career Intelligence & AI Copilot",
        subtitle="AI career copilot platform for interviews, assessments & resume tailoring",
        highlights=chintu_highlights,
        techs=["Next.js", "TypeScript", "Electron", "Supabase", "Razorpay"],
        cta_text="LIVE PLATFORM ↗",
        cta_link="https://getchintu.com",
        accent_color="#38bdf8",
        border_glow="#247bff"
    ))
print("Built project-chintu.svg")

# 3. Project 2: AI Resume Tailor (AWS + Java)
resume_highlights = [
    "☁️ Cloud Hosting: Deployed on AWS Elastic Beanstalk (Corretto 17)",
    "☕ Java Spring Boot: Reactive WebClient & non-blocking routing",
    "🧠 Multi-Provider AI: Fallback across Groq, Cerebras & NVIDIA",
    "📄 Document Engine: Apache PDFBox + POI & ATS LaTeX compilation"
]
with open(os.path.join(out_dir, "project-resume.svg"), "w", encoding="utf-8") as f:
    f.write(build_project_card(
        index_str="04 // FLAGSHIP 02",
        title="AI Resume Tailor & LaTeX Engine (AWS + Java Spring Boot)",
        subtitle="Cloud-native resume tailoring engine with high-throughput Java microservices",
        highlights=resume_highlights,
        techs=["Java", "Spring", "AWS", "Next.js", "TypeScript"],
        cta_text="LIVE PLATFORM ↗",
        cta_link="https://resume.getchintu.com",
        accent_color="#f59e0b",
        border_glow="#f59e0b"
    ))
print("Built project-resume.svg")

# 4. Project 3: Social Connect
social_highlights = [
    "💬 Real-Time Chat: Socket.io instant messaging & reactions",
    "📞 WebRTC Calls: Peer-to-peer audio & video call signaling",
    "🔐 Authentication: JWT with bcrypt, Google & FB OAuth 2.0",
    "👤 Social Ecosystem: User profiles, activity feeds & dashboards"
]
with open(os.path.join(out_dir, "project-social.svg"), "w", encoding="utf-8") as f:
    f.write(build_project_card(
        index_str="04 // FLAGSHIP 03",
        title="Social Connect — Full-Stack Real-Time Social Platform",
        subtitle="Real-time social media application with WebRTC video/audio & chat",
        highlights=social_highlights,
        techs=["Angular", "TypeScript", "Express", "Node.js", "MongoDB"],
        cta_text="LIVE APP ↗",
        cta_link="https://socialconnect.getchintu.com/login",
        accent_color="#a855f7",
        border_glow="#8b5cf6"
    ))
print("Built project-social.svg")

# 5. Project 4: YouTube Automation
yt_highlights = [
    "🤖 3-Tier AI Engine: AssemblyAI audio transcription + Gemini Vision",
    "📁 Google Drive API: Multi-folder monitoring & deduplication",
    "📤 YouTube API v3: Automated scheduled publishing with cron",
    "🛡️ Copyright Safety: Post-upload claim polling & auto-revert"
]
with open(os.path.join(out_dir, "project-youtube.svg"), "w", encoding="utf-8") as f:
    f.write(build_project_card(
        index_str="04 // FLAGSHIP 04",
        title="YouTube Automation — AI Video Metadata & Upload Pipeline",
        subtitle="Automated YouTube content workflow: Drive → Gemini Vision → Scheduled Upload",
        highlights=yt_highlights,
        techs=["Next.js", "TypeScript", "PostgreSQL", "Gemini", "Tailwind"],
        cta_text="LIVE PIPELINE ↗",
        cta_link="https://automation.getchintu.com",
        accent_color="#f43f5e",
        border_glow="#ff354f"
    ))
print("Built project-youtube.svg")

# 6. More Projects
with open(os.path.join(out_dir, "more-projects.svg"), "w", encoding="utf-8") as f:
    f.write(build_more_projects())
print("Built more-projects.svg")

# 7. Stats Header
with open(os.path.join(out_dir, "stats-header.svg"), "w", encoding="utf-8") as f:
    f.write(build_stats_header())
print("Built stats-header.svg")

# 8. Certifications
with open(os.path.join(out_dir, "certifications.svg"), "w", encoding="utf-8") as f:
    f.write(build_certifications())
print("Built certifications.svg")

print("ALL UNIFORM SVGs GENERATED SUCCESSFULLY!")
