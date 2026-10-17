import http.client, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

paths = [
    '/E-commerce/',
    '/Market-Seasonality-Explorer/',
    '/Skill_Up/',
    '/Kanban_Workboard/',
    '/Kanban_WorkBoard/',
    '/Elante_Mall/',
    '/Bharat-Clock/',
    '/Calculator/',
    '/Password_Generator/',
    '/Birthday-Hub/',
    '/Currency_Converter/',
    '/Tic-Tac-Toe/'
]

for p in paths:
    try:
        conn = http.client.HTTPSConnection('185.199.108.153', 443, context=ctx, timeout=4)
        headers = {'Host': 'abhishek6827.github.io', 'User-Agent': 'Mozilla/5.0'}
        conn.request('GET', p, headers=headers)
        resp = conn.getresponse()
        loc = resp.getheader('Location')
        print(f'[{resp.status}] {p} -> {loc if loc else "OK"}')
    except Exception as e:
        print(f'[ERR] {p}: {e}')
