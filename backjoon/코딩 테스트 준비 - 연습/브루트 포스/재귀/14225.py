n = int(input())
s = list(map(int, input().split()))

answer = [False for _ in range(100000*20+1)]
answer[0] = True

def dfs(visited, before, now):
    global answer
    answer[sum(now)] = True
    for idx, num in enumerate(s):
        if not visited[idx] and idx > before:
            visited[idx] = True
            dfs(visited, idx, now+[num])
            visited[idx] = False
            
dfs([False for _ in range(n)], -1, [])
for idx, a in enumerate(answer):
    if not a:
        print(idx)
        exit()
        