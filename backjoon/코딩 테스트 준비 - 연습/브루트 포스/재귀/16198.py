n = int(input())
w = list(map(int, input().split()))
answer = 0
def dfs(ls, energy):
    global answer
    if len(ls) < 3:
        answer = max(answer, energy)
        
    for idx in range(1, len(ls)-1):
        dfs(ls[:idx]+ls[idx+1:], energy+ls[idx-1]*ls[idx+1])

dfs(w, 0)        
print(answer)