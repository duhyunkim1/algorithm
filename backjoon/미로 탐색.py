from collections import deque
def dfs():
    queue = deque([[0, 0, 1]])
    visited.append([0, 0])
    while queue:
        x, y, count = queue.popleft()
        if [x, y] == [N-1, M-1]:
            return count
        for dx, dy in zip(dx_ls, dy_ls):
            if 0<=x+dx<N and 0<=y+dy<M:
                if maps[x+dx][y+dy] == 1 and [x+dx, y+dy] not in visited:
                    visited.append([x+dx, y+dy])
                    queue.append([x+dx, y+dy, count+1])

N, M = map(int, input().split(' '))
maps = [[] for _ in range(N)]
for i in range(N):
    line = input()
    for num in line:
        maps[i].append(int(num))
dx_ls = [-1, 1, 0, 0]
dy_ls = [0, 0, -1, 1]
visited = []
count = dfs()
print(count)


