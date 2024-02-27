from itertools import combinations, permutations
n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split(' '))))

cases = []    
person = [x for x in range(n)]
for i in range(1, int(n//2)+1):
    cases.extend(list(combinations(person, i)))

answer = 100*20*20*10

for case in cases:
    score1 = 0
    for a in case:
        for b in case:
            score1 += maps[a][b]

    case2 = []    
    for p in person:
        if p not in case:
            case2.append(p)
    
    score2 = 0
    for a in case2:
        for b in case2:
            score2 += maps[a][b]       
    
    if answer > abs(score1-score2):
        answer = abs(score1-score2)
        if answer == 0:
            break
print(answer)        