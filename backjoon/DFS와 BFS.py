from collections import deque
def dfs(v):
    visited.append(v)
    for x in data[v]:
        if x not in visited:
            dfs(x)

def bfs(v):
    queue = deque([v])
    visited.append(v)
    while queue:
        now = queue.popleft()
        for x in data[now]:
            if x not in visited:
                queue.append(x)
                visited.append(x)
                
        
N, M, V = map(int, input().split(' '))
data = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split(' '))
    data[a].append(b)
    data[b].append(a)

for i in range(N+1):
    data[i].sort()

visited = []
dfs(V)
print(*visited)
visited = []
bfs(V)
print(*visited)


