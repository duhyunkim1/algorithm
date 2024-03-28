from collections import deque
n = int(input())

result = [0 for _ in range(n+1)]
count = [0 for _ in range(n+1)]

time = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

queue = deque()    
for i in range(1, n+1):
    line = list(map(int, input().split(' ')))
    time[i] = line[0]
    result[i] = line[0]
    for b in line[2:]:
        graph[b].append(i)
        count[i] += 1
    if line[1] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    for x in graph[now]:
        count[x] -= 1
        result[x] = max(time[x]+result[now], result[x])
        
        if count[x] == 0:
            queue.append(x)

print(max(result))
        
