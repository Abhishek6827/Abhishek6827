import os

paths = [
    r'C:\Users\Abhishek\Documents\GitHub',
    r'D:\Desktop',
    r'D:\Desktop\Projects'
]

for p in paths:
    print(f'=== {p} ===')
    if os.path.exists(p):
        try:
            for item in sorted(os.listdir(p)):
                full = os.path.join(p, item)
                t = 'DIR' if os.path.isdir(full) else 'FILE'
                print(f'  [{t}] {item}')
        except Exception as e:
            print('  Err:', e)
    else:
        print('  DOES NOT EXIST')
