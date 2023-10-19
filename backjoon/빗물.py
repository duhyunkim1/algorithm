H, W = map(int, input().split(' '))
rains = list(map(int, input().split(' ')))
maps = [[0 for _ in range(W)] for _ in range(H)]
for r, num in enumerate(rains):
    for h in range(H-1, -1, -1):
        if num > 0:
            maps[h][r] = 1
            num -= 1

answer = 0
for i in range(H):
    start = None
    for j in range(W):
        if maps[i][j] == 1:
            if start == None or start+1 == j:
                start = j 
                end = None
            elif end == None:
                end = j
                answer += end-start-1
                start = j
                end = None
                
print(answer)
