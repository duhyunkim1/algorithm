from collections import deque
def bfs():
    answer = 1
    queue = deque([[start_i, start_j, start_r]])
    visited.append([start_i, start_j])
    while queue:
        i, j, r = queue.popleft()
        tmp_r = r
        move = False
        for n in range(4):
            key = (tmp_r+3)%4
            tmp_r = key
            a, b = direction[key]
            new_x = i+a
            new_y = j+b
            if maps[new_x][new_y] == 0 and [new_x, new_y] not in visited and not move:
                queue.append([new_x, new_y, key])
                visited.append([new_x, new_y])
                answer+=1
                move = True
        if not move:
            a, b = direction[r]
            if maps[i-a][j-b] == 1:
                break
            else:
                queue.append([i-a, j-b, r])
    return answer
N, M = map(int, input().split(' '))
start_i, start_j, start_r = map(int, input().split(' '))
maps = []
visited = []

direction = {}
direction[0] = [-1,0]
direction[1] = [0,1]
direction[2] = [1,0]
direction[3] = [0,-1]
for _ in range(N):
    maps.append(list(map(int, input().split(' '))))
answer = bfs()
print(answer)