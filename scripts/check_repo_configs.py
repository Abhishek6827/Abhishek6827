import os, json

base = r'C:\Users\Abhishek\Documents\GitHub'
for item in os.listdir(base):
    p = os.path.join(base, item)
    if os.path.isdir(p):
        cname = os.path.join(p, 'CNAME')
        pkg = os.path.join(p, 'package.json')
        info = []
        if os.path.exists(cname):
            try:
                info.append('CNAME: ' + open(cname).read().strip())
            except: pass
        if os.path.exists(pkg):
            try:
                d = json.load(open(pkg, encoding='utf-8', errors='ignore'))
                if 'homepage' in d:
                    info.append('homepage: ' + str(d['homepage']))
            except: pass
        if info:
            s = " | ".join(info)
            print(f'{item}: {s}')
