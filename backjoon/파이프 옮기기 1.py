N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split(' '))))
answer = [[[0,0,0] for _ in range(len(maps[0]))]for _ in range(len(maps))]

answer[0][1][0] = 1
for j in range(2,len(maps[0])):
    if maps[0][j] == 0 :
        answer[0][j][0] = answer[0][j-1][0]
    
for i in range(1,len(maps)):
    for j in range(1,len(maps[0])):
        a = answer[i][j-1]
        b = answer[i-1][j]
        c = answer[i-1][j-1]
        if maps[i][j] == 0 and maps[i-1][j] == 0 and maps[i][j-1] == 0:
            answer[i][j][2] = c[0] + c[1] + c[2]
        if maps[i][j] == 0:
            answer[i][j][0] = a[0] + a[2] 
            answer[i][j][1] = b[2] + b[1]
print(sum(answer[-1][-1]))
