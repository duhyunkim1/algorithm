from collections import deque
N, L, R = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(N)]

moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
answer = 0

while True:
    one_day = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue = deque([[i, j]])
                contry = [[i, j]]
                visited[i][j] = True
                while queue:
                    r, c = queue.popleft()
                    for dx, dy in moves:
                        if 0<=r+dx<N and 0<=c+dy<N and not visited[r+dx][c+dy]: 
                            if L <= abs(maps[r][c]-maps[r+dx][c+dy]) <= R:
                                contry.append([r+dx, c+dy])
                                queue.append([r+dx, c+dy])
                                visited[r+dx][c+dy] = True
                one_day.append(contry)

    if len(one_day) == N*N:
        break
    for combined in one_day:
        total = 0
        for r, c in combined:
            total += maps[r][c]
        for r, c in combined:
            maps[r][c] = int(total/len(combined))
    answer +=1 
print(answer)


20 20 20
20 20 20 
40 20 10 

50/3 17

20 20 20 
20 20 16
40 16 16 