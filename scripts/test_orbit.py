import xml.etree.ElementTree as ET

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400" style="background:#070b16;">
  <circle cx="200" cy="200" r="120" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 4"/>
  <!-- Orbiting group rotating clockwise around (200, 200) -->
  <g>
    <animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="8s" repeatCount="indefinite"/>
    <!-- Pill 1 at (200 + 120, 200) -> local (320, 200) -->
    <g transform="translate(320, 200)">
      <!-- Counter-rotate around local (0, 0) -->
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="8s" repeatCount="indefinite" additive="sum"/>
      <rect x="-40" y="-15" width="80" height="30" rx="15" fill="#0b1224" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="0" y="4" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">React</text>
    </g>
    <!-- Pill 2 at (200 - 120, 200) -> local (80, 200) -->
    <g transform="translate(80, 200)">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="8s" repeatCount="indefinite" additive="sum"/>
      <rect x="-40" y="-15" width="80" height="30" rx="15" fill="#0b1224" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="0" y="4" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">Java</text>
    </g>
  </g>
</svg>'''

with open(r'd:\Desktop\Resume-Extension\profile-assets\test_orbit.svg', 'w') as f:
    f.write(svg)
ET.parse(r'd:\Desktop\Resume-Extension\profile-assets\test_orbit.svg')
print('test_orbit.svg created and validated successfully!')
