from collections import deque
def solution(maps):
    m, n = len(maps), len(maps[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    distance = {(0,0): 1}
    points = deque([(0,0)])
    visited[0][0] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while points:
        x, y = points.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and maps[nx][ny] == 1:
                if (nx, ny) == (m-1 , n-1):
                    return distance[(x, y)] + 1
                visited[nx][ny] = True
                distance[(nx,ny)] = distance[(x,y)] + 1
                points.append((nx,ny))
    return -1