from itertools import combinations
kids = []
for _ in range(9):
    kids.append(int(input()))

total = sum(kids)
kids.sort()
perm = combinations(list(range(9)), 2)

for idx1, idx2 in perm:
    if total - (kids[idx1] + kids[idx2]) == 100:
        for idx, kid in enumerate(kids):
            if idx != idx1 and idx != idx2:
                print(kid)
        break
    
    


