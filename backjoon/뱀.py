N = int(input())
K = int(input())
apples = [list(map(int, input().split(' '))) for _ in range(K)]
L = int(input())
moves = [list(input().split(' ')) for _ in range(L)]
maps = [['.' for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if [i, j] in apples:
            maps[i][j] = 'A'
for i, move in enumerate(moves):
    if i == 0:
        move[0] = int(move[0])
    else:
        before = 0
        for m in moves[:i]:
            before+=m[0]
        move[0] = int(move[0]) - before
moves.append([100, 'Last'])

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d_idx = 0
snake = [[1, 1]]

def move_snake(maps, snake, time, direction):
    dx = direction[0]
    dy = direction[1]
    over = False
    while time > 0:
        time-=1
        i, j = snake[0]
        if not (1 <= i+dx <= N and 1 <= j+dy <= N):
            over = True
            break
        elif [i+dx, j+dy] in snake: 
            over = True
            break
        else:
            snake.insert(0, [i+dx, j+dy])
            if maps[i+dx][j+dy] != 'A': 
                snake = snake[:-1]
            else:
                maps[i+dx][j+dy] = '.'
    return snake, time, over

answer = 0
for time, d in moves:
    answer+=time
    snake, remain_time, over = move_snake(maps, snake, time, directions[d_idx])
    if over:
        answer-=remain_time
        break
    if d == 'D':
        d_idx = (d_idx+1)%4
    elif d == 'L':
        d_idx -= 1
        if d_idx < -4:
            d_idx = -1

print(answer)

