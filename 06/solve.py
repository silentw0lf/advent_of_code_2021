with open('input.txt') as f:
    fishs = [int(a) for a  in f.read().split("\n")[0].split(",")]
    days_left = [fishs.count(d) for d in range(9)]

for t in range(1, 256 + 1):
    reset = days_left[0]
    days_left[:8] = days_left[1:9] 
    days_left[6] += reset  
    days_left[8] = reset
    if t == 80:
        print(sum(days_left))
print(sum(days_left))
