N, M, x, y, K = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(N)]
moves = list(map(int, input().split(' ')))
direction = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}

dice = [[0,0],[0,0],[0,0]]

def move_dice(dice, move):
    if move == 1:
        dice = [[dice[1][1], dice[1][0]], [dice[0][0], dice[0][1]], [dice[2][0], dice[2][1]]]
    if move == 2:
        dice = [[dice[1][0], dice[1][1]], [dice[0][1], dice[0][0]], [dice[2][0], dice[2][1]]]
    if move == 3:
        dice = [[dice[2][1], dice[2][0]], [dice[1][0], dice[1][1]], [dice[0][0], dice[0][1]]]
    if move == 4:
        dice = [[dice[2][0], dice[2][1]], [dice[1][0], dice[1][1]], [dice[0][1], dice[0][0]]]
    return dice

for move in moves:
    dx, dy = direction[move]
    if not(0 <= x+dx < N and 0 <= y+dy < M):
        continue
    dice = move_dice(dice, move)
    x += dx
    y += dy
    if maps[x][y] == 0:
        maps[x][y] = dice[0][1]
    else:
        dice[0][1] = maps[x][y]
        maps[x][y] = 0
    print(dice[0][0])
        