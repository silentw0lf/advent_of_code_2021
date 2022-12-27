points1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
points2 = {")": 1, "]": 2, "}": 3, ">": 4}
open_close = {"(": ")", "[": "]", "{": "}", "<": ">"}

with open("input.txt") as f:
    lines =  f.read().splitlines()

score1 = 0
vals = []
for l in lines[:]:
    incomp = True
    while True:
        tmp = l
        for p in ["()", "[]", "{}", "<>"]:
            l = l.replace(p, "")
        if l == tmp:
            break

    for i in range(len(l)):
        if l[i] not in ["(", "[", "{", "<"]:
            score1 += points1[l[i]]
            incomp = False
            break
    
    if incomp:
        val = 0
        for c in reversed(l):
            val *= 5
            val+= points2[open_close[c]]
        vals.append(val)
        
print(score1) # 1
print(sorted(vals)[int(len(vals) /2 - 0.5)]) # 2
