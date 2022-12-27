import re

x_min, x_max, y_min, y_max = [int(a) for a in re.findall('-?\d+', open("input.txt").read())]
max_hit = 0
for x in range(x_max):
    for y in range(y_min, 1000):
        pos = (0,0)
        velo = (x,y)
        maxi = 0
        while True:
            pos = (pos[0] + velo[0], pos[1] + velo[1])
            xvelodiff = +1 if velo[0] < 0 else -1 if velo[0] > 0 else 0 
            velo = (velo[0] + xvelodiff, velo[1] - 1)
            maxi = pos[1] if pos[1] > maxi else maxi


            if pos[0] > x_max or pos[1] < y_min:
                break

            if pos[0] <= x_max and pos[0] >= x_min and pos[1] <= y_max and pos[1] >= y_min:
                max_hit = maxi if maxi > max_hit else max_hit
                break

print(max_hit)
