import heapq
N, M = map(int, input().split(' '))

inf = float("inf")
distance = [inf for _ in range(N+1)]
distance[1] = 0
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b,c))
    graph[b].append((a,c))
q = []
heapq.heappush(q, (0, 1))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next, value in graph[now]:
        if dist + value < distance[next]:
            distance[next] = dist+value
            heapq.heappush(q, (dist+value, next))
            
print(distance[N])