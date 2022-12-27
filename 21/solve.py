# combinators: possible sums: {3, 4, 5, 6, 7, 8, 9}
def boom(i, d, score, pos):
    for summy in [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]:
        for a in range(summy[1]):
            field = pos[i] + summy[0]
            d += 3
            pos[i] = (field -1) % 10 + 1
            score[i] += pos[i]

            if score[0] >= 21 or score[1] >= 21:
                return
            i = (i + 1) % 2
            boom(i, d, score, pos)

pos = [int(a.split(": ")[1]) for a in open("input.txt").read().splitlines()]
i, d, score, di = 0, 0, [0,0], list(range(1,101))

while True:
    field = pos[i] + sum(di[(d+a)%100] for a in range(3))
    d += 3
    pos[i] = (field -1) % 10 + 1
    score[i] += pos[i]

    if score[0] >= 1000 or score[1] >= 1000:
        break
    i = (i + 1) % 2

print(min(score) * d)
