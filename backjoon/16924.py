def check_length(maps, directions, n, m, N, M):
    length = 0
    flag = True
    while flag:
        for dx, dy in directions:
            if 0 <= n+dx*length < N and 0 <= m+dy*length < M:
                if maps[n+dx*length][m+dy*length] != '*':
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:            
            length += 1
    return length-1

def fill_maps(maps, directions, n, m, length):
    for s in range(length+1):
        for dx, dy in directions:
            maps[n+dx*s][m+dy*s] = '*'
    return maps

N, M = map(int, input().split(' '))
maps = []
for _ in range(N):
    maps.append([x for x in input()])
    
maps_for_fill = [['.']*M for _ in range(N)]
directions = [[-1,0], [1,0], [0,-1], [0,1]]
answer = []
for n in range(N):
    for m in range(M):
        length = check_length(maps, directions, n, m, N, M)
        if length > 0:
            answer.append([n+1, m+1, length])
            maps_for_fill = fill_maps(maps_for_fill, directions, n, m, length)    

if maps_for_fill == maps:
    c = len(answer)
    print(c)
    for i in range(c):
        a = list(map(str, answer[i]))
        print(' '.join(a))
else:
    print(-1)