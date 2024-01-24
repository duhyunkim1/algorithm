from collections import deque
def bfs(points, characterX, characterY, itemX, itemY, dx, dy):
    queue = deque([[characterX, characterY,0]])
    visited = [[False for _ in range(102)] for _ in range(102)]
    while queue:
        i, j, count = queue.popleft()
        if i == itemX and j == itemY:
            return count
        for x, y in zip(dx, dy):
            new_i = i+x
            new_j = j+y
            if 0<=new_i<102 and 0<=new_j<102 and not visited[new_i][new_j] and points[new_i][new_j]==1:
                queue.append([new_i, new_j, count+1])
                visited[new_i][new_j] = True
def solution(rectangle, characterX, characterY, itemX, itemY):
    points = [[-1 for _ in range(102)] for _ in range(102)]
    for box in rectangle:
        new = [2*x for x in box]
        for x in range(new[0], new[2]+1):
            for y in range(new[1],new[3]+1):
                if new[0]<x<new[2] and new[1]<y<new[3]:
                    points[x][y]=0
                elif points[x][y] !=0:
                    points[x][y]=1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = bfs(points, 2*characterX, 2*characterY, 2*itemX, 2*itemY, dx, dy)
    return answer/2