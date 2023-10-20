import heapq
N = int(input())
M = int(input())

graph = [list(map(int, input().split(' '))) for _ in range(N)]

city = list(map(int, input().split(' ')))
city = [x-1 for x in city]

def dst(start, end):
    visited = [0 for _ in range(N)]
    visited[start] = 1
    q = []
    heapq.heappush(q,(0, start))
    while q:
        dist, now = heapq.heappop(q) 
        for next, value in enumerate(graph[now]):
            if value == 0:
                continue
            if visited[next] == 1:
                continue
            heapq.heappush(q, (dist+1, next))
            visited[next] =1
    return visited[end]    

answer = 0
for i in range(len(city)-1):
    if dst(city[i], city[i+1]) != 1:
        print("NO")
        exit()
print("YES")