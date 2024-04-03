# 다시
n = int(input())
answer = 0
space = [0 for _ in range(n)]

def check(space, row, col):
    for i in range(row):
        if space[i] == col:
            return False

    for i in range(row):
        if abs(space[i]-col) == (row-i):
            return False
    return True

def dfs(step):
    global answer    
    if step == n:
        answer += 1
        return
    
    for i in range(n):
        if check(space, step, i):
            space[step] = i
            dfs(step+1)
              
dfs(0)
print(answer)            
