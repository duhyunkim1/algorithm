from itertools import product
import copy
N = int(input())
maps_init = [list(map(int, input().split(' '))) for _ in range(N)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def move(maps, i, j, dx, dy, done):
    cnt = 0 
    i_init = i
    j_init = j
    while 0<=i+dx<N and 0<=j+dy<N and maps[i+dx][j+dy] == 0:
        i+=dx
        j+=dy
        cnt+=1
    
    if i!= i_init or j!=j_init:
        maps[i][j] = maps[i_init][j_init]
        maps[i_init][j_init] = 0

    if 0<=i+dx<N and 0<=j+dy<N:
        if maps[i][j] == maps[i+dx][j+dy] and not done[i+dx][j+dy]:
            maps[i+dx][j+dy] *= 2
            maps[i][j] = 0
            done[i+dx][j+dy] = True

    return maps, done

orders = list(product([0,1,2,3], repeat=5))
# print(orders)
answer = 0

for order in orders:
    maps = copy.deepcopy(maps_init)
    for idx, o in enumerate(order):
        dx = dxs[o]
        dy = dys[o]
        done = [[False for _ in range(N)] for _ in range(N)]
        if o == 0:
            for i in range(N):
                for j in range(N):
                    if maps[i][j] != 0:  
                        maps, done = move(maps, i, j, dx, dy, done)
        if o == 1:
            for i in range(N-1, -1, -1):
                for j in range(N):
                    if maps[i][j] != 0:
                        maps, done = move(maps, i, j, dx, dy, done)   
        if o == 2:
            for j in range(N):
                for i in range(N):
                    if maps[i][j] != 0:
                        maps, done = move(maps, i, j, dx, dy, done)      
        if o == 3:
            for j in range(N-1, -1, -1):
                for i in range(N):
                    if maps[i][j] != 0:
                        maps, done = move(maps, i, j, dx, dy, done)
    all_v = []                                                                          
    for map in maps:
        for v in map:
            all_v.append(v)
    if answer < max(all_v):
        answer = max(all_v)
print(answer)