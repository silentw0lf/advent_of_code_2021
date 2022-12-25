
with open("input.txt", "r") as f:
    bins = f.read().splitlines()

def get_ratings(listing: list, ident: str) -> int:
    l = listing.copy()
    for i in range(len(listing[0])):
        ones = sum(int(bin[i]) & 1 for bin in l)
        if ident == "co2":
            check = 1 if ones < len(l) - ones else 0
        elif ident == "oxygen":
            check = 1 if ones >= len(l) - ones else 0
        for bin in l[:]:  
            if len(l) <= 1:
                break
            if int(bin[i]) != check:
                l.remove(bin)
    return int(l[0], 2)

# 1
gamma = 0
for i in range(len(bins[0])):
    ones = sum(int(bin[i]) & 1 for bin in bins)
    gamma_bit = 1 if ones > len(bins) - ones else 0
    gamma |= gamma_bit << (len(bins[0]) -1 - i)

epsilon = ~gamma + 2 ** len(bins[0])
print(gamma * epsilon)

#2
print(get_ratings(bins, "co2") * get_ratings(bins, "oxygen"))