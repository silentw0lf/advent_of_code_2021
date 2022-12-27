with open('input.txt') as f:
    coor, instrs = f.read().split('\n\n')
    instrs = [(t.split("=")[0][-1] , int(t.split("=")[1])) for t in instrs.splitlines()]
    coor = {(int(t[1]), int(t[0])): "#" for t in [c.split(',') for c in coor.split('\n')]}

for i, (s, lim) in enumerate(instrs):
    idx = 0 if s == 'y' else 1
    origami = [k for k in coor if k[idx] > lim]
    for r, c in origami:
        t1, t2 = (lim - abs(r - lim), c) if s == 'y' else (r, lim - abs(c - lim))
        coor[(t1, t2)] = "#"
        del coor[(r, c)]
    if i == 0:
        print(len(coor))

for r in range(max(t[0] for t in coor.keys())+1):
    l = []
    for c in range(max(t[1] for t in coor.keys())+1):
        l.append("#" if (r,c) in coor else " ")
    print(*l)