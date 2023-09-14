from collections import deque
def dfs():
    while queue:
        now, count = queue.popleft()
        if now == k:
            return count
        for j in (now-1, now+1, now*2):
            if 0 <= j <= max_num and not visited[j]:
                visited[j]=True
                queue.append([j, count+1])
n, k = map(int, input().split(' ')) 
max_num = 100000
visited=[False] * (max_num+1)
queue = deque([[n, 0]])
visited.append(n)
result = dfs()
print(result)