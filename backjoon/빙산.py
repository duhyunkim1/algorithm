from collections import deque
def bfs1(i, j, visited):
    queue = deque([[i,j]])
    visited[i][j] = True
    while queue:
        i, j = queue.popleft()
        for x, y in zip(dx, dy):
            new_i = i+x
            new_j = j+y
            if 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j]:
                    if maps[new_i][new_j] == 0:
                        queue.append([new_i, new_j])
                        visited[new_i][new_j] = True
                    if maps[new_i][new_j] > 0:
                        maps[new_i][new_j] -= 1
                        if maps[new_i][new_j] == 0:
                            visited[new_i][new_j] = True
    return visited

def bfs2(i, j, visited):
    queue = deque([[i,j]])
    visited[i][j] = True
    while queue:
        i, j = queue.popleft()
        for x, y in zip(dx, dy):
            new_i = i+x
            new_j = j+y
            if 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j]:
                if maps[new_i][new_j] > 0:
                    queue.append([new_i, new_j])
                    visited[new_i][new_j] = True
    return visited
N, M = map(int, input().split(' '))
maps = []
for n in range(N):
    maps.append(list(map(int, input().split(' '))))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer=0
while True:
    answer+=1
    visited_new = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0 and not visited_new[i][j]:
                visited_new = bfs1(i, j, visited_new)
    visited_new = [[False for _ in range(M)] for _ in range(N)]                
    count = 0 
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0 and not visited_new[i][j]:
                count += 1
                visited_new = bfs2(i, j, visited_new)

    if count >= 2:
        print(answer)
        break
    if maps == [[0 for _ in range(M)] for _ in range(N)] or answer>10000:
        print(0)
        break

    
