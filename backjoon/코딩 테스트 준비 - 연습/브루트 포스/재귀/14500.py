n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
direction = [[1,0], [-1,0], [0,-1], [0,1]]
answer = 0

def dfs(i, j, tmp, visited, count):
    global answer
    if count == 4:
        answer = max(answer, tmp)
        return
    
    for dx, dy in direction:
        if 0<=i+dx<n and 0<=j+dy<m and not visited[i+dx][j+dy]:
            visited[i+dx][j+dy] = True
            dfs(i+dx, j+dy, tmp+space[i+dx][j+dy], visited, count+1)
            if count == 2:
                dfs(i, j, tmp+space[i+dx][j+dy], visited, count+1)
            visited[i+dx][j+dy] = False
                
                      
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, space[i][j], visited, 1)
        visited[i][j] = False

print(answer)