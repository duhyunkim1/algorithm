from collections import deque
def bfs(start):
    queue = deque([[start, 0]])
    visited.append(start)
    while queue:
        now, count = queue.popleft()
        for x in graph[now]:
            if x == end:
                print(count+1)
                exit()
            if x not in visited:
                queue.append([x, count+1])
                visited.append(x)
n = int(input())
start, end = map(int, input().split(' '))
m = int(input())
graph = [[] for _ in range(101)]
visited = []
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
bfs(start)
print(-1)
