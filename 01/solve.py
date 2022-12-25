with open("input.txt") as f:
    depths = [int(a) for a in f.readlines()]

# 1
counter, i = 0, 0
while(i + 1 < len(depths)):
    if depths[i + 1] > depths[i]:
        counter+=1
    i += 1    
print(counter)

# 2 
counter, i = 0, 0
while(i + 3 < len(depths)):
    if sum(depths[i+1:i+4]) > sum(depths[i:i+3]):
        counter+=1
    i += 1    
print(counter)
