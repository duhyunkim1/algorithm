def dfs(num):
    for x in graph[num]:
        if x not in visited:
            visited.append(x)
            dfs(x)
    
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = [1]
dfs(1)
print(len(visited)-1)
