def solve(it: int) -> int:
    tmpl, insts = open("input.txt").read().split('\n\n')
    rules = {i[0]: i[1] for i in [x.split(' -> ') for x in insts.splitlines()]}
    cnt = {c: tmpl.count(c) for c in set(tmpl).union(set(rules.values()))}
    cnt_r = {c: tmpl.count(c) for c in rules}
    
    for _ in range(it):
        tmp = dict()
        for r, c in cnt_r.items():
            if c != 0:
                font_tup, back_tup = r[0] + rules[r], rules[r] + r[1]
                if font_tup in rules:
                    tmp[font_tup] = tmp.get(font_tup, 0) + c
                if back_tup in rules:
                    tmp[back_tup] = tmp.get(back_tup, 0) + c
                cnt[rules[r]] += c
        cnt_r = tmp
    return max(cnt.values()) - min(cnt.values())

print(solve(10))
print(solve(40))
