n, m = map(int, input().split())
space = [input() for _ in range(n)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]
answer = 11    

coin = []
for i in range(n):
    for j in range(m):
        if space[i][j] == 'o':
            coin.append([i,j])

def move(x, y, dx, dy):
    nx = x+dx
    ny = y+dy
    
    if not (0<=nx<n and 0<=ny<m):
        return -1, -1, 0
    
    if space[nx][ny] == '#':
        return x, y, 1
    else:
        return nx, ny, 2

def dfs(x1, y1, x2, y2, step):
    global answer
    if step > 10:
        return
    
    if ([x1, y1] == [-1, -1] and [x2, y2] != [-1, -1]) or ([x1, y1] != [-1, -1] and [x2, y2] == [-1, -1]):
        answer = min(answer, step)
        return
    
    for dx, dy in direction:
        nx1, ny1, is_move1 = move(x1, y1, dx, dy)
        nx2, ny2, is_move2 = move(x2, y2, dx, dy)
                
        if [is_move1, is_move2] not in [[0,0], [1,1]]:
            dfs(nx1, ny1, nx2, ny2, step+1)
            
        
dfs(coin[0][0],coin[0][1],coin[1][0],coin[1][1], 0)
if answer > 10:
    print(-1)
else:
    print(answer)
