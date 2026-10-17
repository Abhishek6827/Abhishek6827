import urllib.request, re

url = 'https://github.com/Abhishek6827'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')
    for m in re.finditer(r'<img[^>]+src="([^">]+)"', html):
        src = m.group(1)
        if 'about-life' in src or 'stack' in src:
            print('Found img src:', src)
