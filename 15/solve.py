import heapq

neighbors = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def get_neighbours(r, c, m):
    vals = []
    for s in neighbors:
        rn, cn = r+s[0], c+s[1]
        if 0 <= rn and 0 <= cn and rn < len(m) and cn < len(m[0]):
            vals.append((rn, cn))
    return vals


def dijk(m, cost_node):
    visited, cost_node = set(), [(0, start)]

    while cost_node:
        cost, current = heapq.heappop(cost_node)
        if current not in visited:
            if current == (len(m[0])-1, len(m)-1):
                return cost
            for neigh in get_neighbours(current[0], current[1], m):
                n_cost = m[neigh[1]][neigh[0]] + cost
                heapq.heappush(cost_node, (n_cost, neigh))

            visited.add(current)


m = [[int(a) for a in line] for line in open("input.txt").read().splitlines()]
m_big = [[(m[r % len(m)][c % len(m)] + int(c/len(m)) + int(r/len(m)) - 1) %
          9 + 1 for c in range(len(m) * 5)] for r in range(len(m) * 5)]

start = (0, 0)
print(dijk(m, start))
print(dijk(m_big, start))
