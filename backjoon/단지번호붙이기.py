from collections import deque
def bfs(i, j):
    queue = deque([[i, j]])
    visited.append([i, j])
    count = 1
    while queue:
        x, y= queue.popleft()
        for dx, dy in zip(dx_ls, dy_ls):
            if 0<=x+dx<N and 0<=y+dy<N:
                if maps[x+dx][y+dy] == 1 and [x+dx, y+dy] not in visited:
                    queue.append([x+dx, y+dy])
                    visited.append([x+dx, y+dy])
                    count+=1
    return count
N = int(input())
maps = [[] for _ in range(N)]
for n in range(N):
    for x in input():
        maps[n].append(int(x))

visited = []
dx_ls = [1, -1, 0, 0]
dy_ls = [0, 0, 1, -1]
total = 0
results = []
for i in range(N):
    for j in range(N):
        if [i, j] in visited or maps[i][j] == 0:
            continue
        result = bfs(i, j)
        results.append(result)
print(len(results))
print(*sorted(results))