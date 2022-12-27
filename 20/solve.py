from collections import defaultdict

def get_indx(outp, r, c):
    idx = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            bit = 1 if outp[r+dr, c+dc] == '#' else 0
            idx = (idx << 1) | bit
    return idx

def enhance(outp_old, iea, defa='.'):
  outp = defaultdict(lambda: defa)
  for r,c in list(outp_old.keys()):
    for dr in [-1, 0, 1]:
      for dc in [-1, 0, 1]:
        rn, rc = r+dr, c+dc
        outp[rn, rc] = iea[get_indx(outp_old, rn, rc)]
  return outp


iea, inp = open('input.txt').read().split('\n\n')
inp = [list(line) for line in inp.splitlines()]

outp = defaultdict(lambda: '.')
for r in range(len(inp)):
    for c in range(len(inp[0])):
        outp[r,c] = inp[r][c]

for i in range(50):
    defa = iea[0] if i % 2 == 0 or iea[0] == '.' else iea[-1]
    outp = enhance(outp, iea, defa)
    if i == 1:
        print(sum([1 for point in outp if outp[point] == '#'])) #  1

print(sum([1 for point in outp if outp[point] == '#'])) # 2
