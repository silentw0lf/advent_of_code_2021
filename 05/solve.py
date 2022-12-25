def get_overlaps(tups, diagonal: bool) -> int:
    max_x = max([t[0] for t in tuples] + [t[2] for t in tuples]) + 1 
    max_y = max([t[1] for t in tuples] + [t[3] for t in tuples]) + 1  
    mat = [[0] * max_x for i in range(max_y)]
    for x1, y1, x2, y2 in tups:
        if y1 == y2:
            max_x, min_x = max(x1, x2), min(x1, x2)
            while min_x <= max_x:
                mat[y1][min_x] += 1
                min_x += 1 
        elif x1 == x2:
            max_y, min_y = max(y1, y2), min(y1, y2)
            while min_y <= max_y:
                mat[min_y][x1] += 1
                min_y += 1 
        elif diagonal:
                mat[y1][x1] += 1
                while x1 < x2 and y1 < y2:
                    x1 += 1
                    y1 += 1
                    mat[y1][x1] += 1
                while x1 < x2 and y2 < y1:
                    x1 += 1
                    y1 -= 1
                    mat[y1][x1] += 1
                while x2 < x1 and y1 < y2:
                    x1 -= 1
                    y1 += 1
                    mat[y1][x1] += 1
                while x2 < x1 and y2 < y1:
                    x1 -= 1
                    y1 -= 1
                    mat[y1][x1] += 1
    return len([val for rows in mat for val in rows if val >= 2])


with open('input.txt') as f:
    data = [t.split(' -> ') for t in f.read().splitlines()]
    tuples = [[(int(a[0].split(',')[0])), int((a[0].split(',')[1])), int(a[1].split(',')[0]), int((a[1].split(',')[1]))] for a in data]

print(get_overlaps(tuples, diagonal=False)) # 1
print(get_overlaps(tuples, diagonal=True)) # 2

