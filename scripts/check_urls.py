import urllib.request, ssl, socket
from concurrent.futures import ThreadPoolExecutor

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    ('Chintu AI', 'https://getchintu.com'),
    ('Resume Tailor', 'https://resume.getchintu.com'),
    ('Social Connect', 'https://socialconnect.getchintu.com/login'),
    ('YouTube Automation', 'https://automation.getchintu.com'),
    ('Tempusmail', 'https://tempomail.getchintu.com'),
    ('Myntra Clone', 'https://Abhishek6827.github.io/Myntra/'),
    ('Kanban WorkBoard', 'https://Abhishek6827.github.io/Kanban_WorkBoard/'),
    ('Market Explorer', 'https://abhishek6827.github.io/Market-Seasonality-Explorer/'),
    ('Skill Up', 'https://Abhishek6827.github.io/Skill_Up/'),
    ('Elante Mall', 'https://Abhishek6827.github.io/Elante_Mall/'),
    ('Portfolio (subdomain)', 'https://portfolio.getchintu.com'),
    ('Portfolio (github.io)', 'https://abhishek6827.github.io/Portfolio/')
]

def check(item):
    name, u = item
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=4, context=ctx) as resp:
            return f'[OK - {resp.status}] {name}: {u}'
    except Exception as e:
        return f'[FAIL - {e}] {name}: {u}'

with ThreadPoolExecutor(max_workers=12) as executor:
    results = list(executor.map(check, urls))

for r in results:
    print(r)
