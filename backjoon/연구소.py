import copy
from itertools import permutations
N, M = map(int, input().split(' '))
maps_init = [list(map(int, input().split(' '))) for _ in range(N)]

blank = []
virus = []
for i in range(N):
    for j in range(M):
        if maps_init[i][j] == 0:
            blank.append([i, j])
        if maps_init[i][j] == 2:
            virus.append([i, j])
            
moves = [[-1,0],[1,0],[0,-1],[0,1]]
walls = permutations(blank, 3)        

def bfs(queue, maps):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    while queue:
        vi, vj = queue.pop(0)
        visited[vi][vj] = True
        for dx, dy in moves:
            if 0<=vi+dx<N and 0<=vj+dy<M and not visited[vi+dx][vj+dy]:
                visited[vi+dx][vj+dy] = True
                if maps[vi+dx][vj+dy] == 0:
                    maps[vi+dx][vj+dy] = 2
                    queue.append([vi+dx, vj+dy])
    return maps

answer =  0
for wall in walls:
    v = copy.deepcopy(virus)
    maps = copy.deepcopy(maps_init)
    for wi, wj in wall:
        maps[wi][wj] = 1
    maps = bfs(v, maps)
    count=0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                count+=1
    if answer < count:
        answer = count

print(answer)      
        
  