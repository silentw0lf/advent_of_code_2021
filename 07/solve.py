
with open('input.txt') as f:
    curr_positions = [int(a) for a  in f.read().splitlines()[0].split(",")]
    higehst_pos = max(curr_positions)

fuels_total, fuels_total2 = [], []
for target_pos in range(higehst_pos + 1):
    fuel_target, fuel_target2 = 0, 0
    for pos in curr_positions:
        fuel_target += abs(target_pos - pos)
        n = abs(target_pos - pos)
        fuel_target2 += int(((n+1) * n)/2)
    fuels_total.append(fuel_target)
    fuels_total2.append(fuel_target2)

print(min(fuels_total)) # 1
print(min(fuels_total2)) # 2