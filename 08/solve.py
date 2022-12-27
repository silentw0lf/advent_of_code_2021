from typing import List

with open("input.txt") as f:
    lines = [l.strip().split(" | ") for l in f.readlines()]
    lines = [[a.split(), b.split()] for (a,b) in lines]

def numb_to_set_mapp(input: set) -> List[set]:
    d, s  = [set()] * 10,  dict()

    d[1] = set([i for i in input if len(i) == 2][0])
    d[4] = set([i for i in input if len(i) == 4][0])
    d[7] = set([i for i in input if len(i) == 3][0])
    d[8] = set([i for i in input if len(i) == 7][0])

    # helpers
    dig_235 = [set(i) for i in input if len(i) == 5]
    mutal_235 = dig_235[0].intersection(dig_235[1]).intersection(dig_235[2])
    dig_690 = [set(i) for i in input if len(i) == 6]

    # 7 segments of a number
    s["hor_ob"] = d[7]  - d[1]
    s["hor_mi"] = mutal_235.intersection(d[4]) 
    s["hor_re"] = mutal_235 - d[4] - d[7]  
    s["ver_un_re"] = [i.intersection(d[1]) for i in dig_690 if len(i.intersection(d[1])) == 1][0] 
    s["ver_ob_re"] = d[1] - s["ver_un_re"] 
    s["ver_ob_li"] = d[4] - d[1] - s["hor_mi"] 
    s["ver_un_le"] = set('abcdefg') - s["hor_ob"] -  s["ver_ob_li"] - s["ver_ob_re"] - s["hor_mi"] -s["ver_un_re"] -s["hor_re"] 
    
    d[2] = mutal_235.union(s["ver_ob_re"]).union(s["ver_un_le"])
    d[5] = mutal_235.union(s["ver_ob_li"]).union(s["ver_un_re"])
    d[3] = mutal_235.union(d[1])
    d[0] = d[8] - s["hor_mi"]
    d[6] = d[8] - s["ver_ob_re"]
    d[9] = d[8] - s["ver_un_le"]     
    
    return d

# 1
print(len([x for l in lines for x in l[1] if len(x) in {2, 3, 4, 7}]))

# 2
summ = 0
for input, output in lines:   
    mapping = numb_to_set_mapp(input)
    summ +=  sum([int(mapping.index(set(o)) * (10 ** (3-i))) for i,o in enumerate(output)])
print(summ)