basin = [[] for _ in range(1000)]
steps = [(0,1), (0,-1), (1,0), (-1,0)]

def find_basins(m: list, r: int, c: int, i: int):
    for n,r1,c1 in find_neigbours(m, r, c):
        if n != 9 and n > m[r][c]:
            if [n, r1,c1] not in basin[i]:
                basin[i].append([n, r1, c1])
                find_basins(m,r1,c1, i)

def find_neigbours(m: list, r: int, c: int) -> list:
    neighbours = []
    for s in steps:
        rn, cn = r + s[0], c + s[1]
        if rn < 0 or cn < 0 or rn > len(m) -1  or cn > len(m[0]) -1:
            continue
        neighbours.append((m[rn][cn], rn, cn))   
    return neighbours

with open("input.txt") as f:
    matrix = [[int(a) for a in line] for line in [list(l) for l in f.read().splitlines()]]

task1, task2, i = 0, 1, 0
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if all(matrix[r][c] < n[0] for n in find_neigbours(matrix,r,c)):
            task1 += matrix[r][c] + 1
            basin[i].append([matrix[r][c], r, c])
            find_basins(matrix, r, c, i)
            i += 1

for v in sorted([len(l) for l in basin if len(l) > 0])[-3:]:
    task2 *= v

print(task1) # 1
print(task2) # 2 