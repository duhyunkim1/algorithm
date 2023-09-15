from collections import deque
def bfs():
    while queue:
        now, count = queue.popleft()
        if now == G:
            return count
        if now+U <= F and not visited[now+U]:
            queue.append([now+U, count+1])
            visited[now+U]=True
        if now-D >=1 and not visited[now-D]:
            queue.append([now-D, count+1])
            visited[now-D]=True
F, S, G, U, D = map(int, input().split(' '))
visited = [False] * 1000001
queue = deque([[S, 0]])
visited[S] = True
result = bfs()
if result == None:
    result = "use the stairs"
print(result)