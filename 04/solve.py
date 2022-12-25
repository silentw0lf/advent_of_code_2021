def bingo(field: list) -> bool:
    return any(all(i == 'x' for i in row) for row in field) or any(all(row[i] == 'x' for row in field) for i in range(len(field[0])))

def calc_final_score(field: list, r: int) -> int:
    return r * sum(sum(col for col in row if col != 'x') for row in field) 

with open('input.txt') as f:
    data = f.read().split("\n\n")
    randoms = [int(s) for s in data[0].split(',')]
    fields = [[[int(s) for s in row.split() if s.isdigit()] for row in field.split('\n')] for field in data[1:]]

fields_bingo =[]
first_bingo_found = False
last_bingo_found = False
for r in randoms:
    if last_bingo_found:
        break
    for i_f, field in enumerate(fields):
        for i_r, row in enumerate(field):
            for i_c, col in enumerate(row):
                if col == r:
                    fields[i_f][i_r][i_c] = 'x'
        for i_f, field in enumerate(fields):
            if not i_f in fields_bingo:
                if bingo(field):
                    fields_bingo.append(i_f)
                    if not first_bingo_found:
                        print(f"task 1: {calc_final_score(field, r)}")
                        first_bingo_found = True    
                    last_i_f = i_f
                    last_r = r
        if len(fields_bingo) == len(fields):
            last_bingo_found = True
            break

print(f"task 2: {calc_final_score(fields[last_i_f], last_r)}")




