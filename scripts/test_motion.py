import xml.etree.ElementTree as ET

svg = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 600 300" width="600" height="300" style="background:#070b16;">
  <defs>
    <!-- Elliptical Path for Orbit 1 -->
    <path id="orbit1" d="M -160,0 a 160,55 0 1,0 320,0 a 160,55 0 1,0 -320,0" fill="none"/>
    <path id="orbit2" d="M -240,0 a 240,80 0 1,0 480,0 a 240,80 0 1,0 -480,0" fill="none"/>
  </defs>

  <!-- Center (300, 150) -->
  <g transform="translate(300, 150)">
    <!-- Orbit guide lines -->
    <ellipse cx="0" cy="0" rx="160" ry="55" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-opacity="0.4" stroke-dasharray="4 4"/>
    <ellipse cx="0" cy="0" rx="240" ry="80" fill="none" stroke="#ff354f" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="6 6"/>

    <!-- Sun Core -->
    <circle cx="0" cy="0" r="25" fill="#0b1224" stroke="#38bdf8" stroke-width="2"/>
    <text x="0" y="4" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">CHINTU</text>

    <!-- Planet 1 on Orbit 1 -->
    <g>
      <animateMotion dur="12s" repeatCount="indefinite" begin="0s">
        <mpath xlink:href="#orbit1"/>
      </animateMotion>
      <rect x="-35" y="-13" width="70" height="26" rx="13" fill="#0b1224" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="0" y="4" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">React</text>
    </g>

    <!-- Planet 2 on Orbit 1 (offset by 6s) -->
    <g>
      <animateMotion dur="12s" repeatCount="indefinite" begin="-6s">
        <mpath xlink:href="#orbit1"/>
      </animateMotion>
      <rect x="-35" y="-13" width="70" height="26" rx="13" fill="#0b1224" stroke="#60a5fa" stroke-width="1.2"/>
      <text x="0" y="4" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Next.js</text>
    </g>

    <!-- Planet 3 on Orbit 2 -->
    <g>
      <animateMotion dur="18s" repeatCount="indefinite" begin="0s">
        <mpath xlink:href="#orbit2"/>
      </animateMotion>
      <rect x="-35" y="-13" width="70" height="26" rx="13" fill="#0b1224" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="0" y="4" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Java</text>
    </g>

    <!-- Planet 4 on Orbit 2 (offset by 9s) -->
    <g>
      <animateMotion dur="18s" repeatCount="indefinite" begin="-9s">
        <mpath xlink:href="#orbit2"/>
      </animateMotion>
      <rect x="-35" y="-13" width="70" height="26" rx="13" fill="#0b1224" stroke="#ff9900" stroke-width="1.2"/>
      <text x="0" y="4" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">AWS</text>
    </g>
  </g>
</svg>'''

with open(r'd:\Desktop\Resume-Extension\profile-assets\test_motion.svg', 'w') as f:
    f.write(svg)
ET.parse(r'd:\Desktop\Resume-Extension\profile-assets\test_motion.svg')
print('test_motion.svg is valid XML!')
