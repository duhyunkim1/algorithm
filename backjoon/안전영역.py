from collections import deque
from copy import deepcopy
def bfs(queue, rained):
    while queue:
        i, j = queue.popleft()
        for x, y in zip(dx, dy):
            next_i = i+x
            next_j = j+y
            if 0 <= next_i < N and 0 <= next_j < N:
                if rained[next_i][next_j] != -1:
                    queue.append([next_i, next_j])
                    rained[next_i][next_j] = -1
    return rained

N = int(input())
maps = [[]for _ in range(N)]
all_values = set([0])
for n in range(N):
    inputs = list(map(int, input().split(' ')))
    maps[n] = inputs
    all_values.update(inputs)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
num_region = 0
for v in all_values:
    results = []
    rained_new = deepcopy(maps)
    for i in range(N):
        for j in range(N):
            if rained_new[i][j] <= v:
                rained_new[i][j] = -1
    region = 0
    for i in range(N):
        for j in range(N):        
            if rained_new[i][j] != -1:
                queue_new = deque([[i,j]])
                rained_new[i][j] = -1
                rained_new = bfs(queue_new, rained_new)
                region += 1
    if region > num_region:
        num_region = region
print(num_region)
    