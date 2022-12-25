with open("input.txt", "r") as f:
    instrs = [(instr.split(" ")[0], int(instr.split(" ")[1])) for instr in f.read().splitlines()]

#1
pos = [0,0]
for dir, unit in instrs:
    if dir == "forward":
        pos[0] += unit
    elif dir == "down":
        pos[1] += unit    
    elif dir == "up":
        pos[1] -= unit
    else:
        raise Exception()
print(pos[0] * pos[1])

#2
pos = [0,0, 0]
for dir, unit in instrs:
    if dir == "forward":
        pos[0] += unit
        pos[1] += (pos[2] * unit)
    elif dir == "down":
        pos[2] += unit   
    elif dir == "up":
        pos[2] -= unit
    else:
        raise Exception()
print(pos[0] * pos[1])