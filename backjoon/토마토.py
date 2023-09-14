from collections import deque
def bfs(queue):
    count=0
    while queue:
        h, n, m, count = queue.popleft()
        for dx, dy, dz in zip(dx_ls, dy_ls, dz_ls):
            tmp_h = h+dz
            tmp_n = n+dx
            tmp_m = m+dy
            if 0<=tmp_h<H and 0<=tmp_n<N and 0<=tmp_m<M:
                if box[tmp_h][tmp_n][tmp_m] == 0:
                    box[tmp_h][tmp_n][tmp_m] = 1
                    queue.append([tmp_h, tmp_n, tmp_m, count+1])
    return count
M, N, H = map(int, input().split(' '))
box = [[[] for _ in range(N)] for _ in range(H)] 

for h in range(H):
    for n in range(N):
        box[h][n]=list(map(int, input().split(' ')))

dx_ls = [-1, 1, 0, 0, 0, 0]
dy_ls = [0, 0, -1, 1, 0, 0]
dz_ls = [0, 0, 0, 0, -1, 1]
visited = []
results = []
queue_start = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue_start.append([h, n, m, 0])
result = bfs(queue_start)
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                result = -1
print(result)
