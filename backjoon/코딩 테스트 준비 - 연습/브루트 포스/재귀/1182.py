n, s = map(int, input().split())
a = list(map(int, input().split()))

answer = 0
def dfs(before, visited, now):
    global answer
    if len(now)>0 and sum(now) == s:
        answer += 1

    for idx, num in enumerate(a):
        if not visited[idx] and before<idx:
            visited[idx]=True
            dfs(idx, visited, now+[num])
            visited[idx]=False
            
dfs(-1, [False for _ in range(n)], [])
print(answer)