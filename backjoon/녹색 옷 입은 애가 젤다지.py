import heapq
count =0
while True:
    count += 1
    N = int(input())
    if N == 0:
        break
    maps = [list(map(int, input().split(' '))) for _ in range(N)]
    inf = float('inf')
    paths = [[inf for _ in range(N)] for _ in range(N)]
    moves = [[-1,0],[1,0],[0,-1],[0,1]]
    paths[0][0] = maps[0][0]
    q = []
    heapq.heappush(q, (maps[0][0], [0,0]))
    while q:
        money, (r, c) = heapq.heappop(q)
        for dx, dy in moves:
            if 0<=r+dx<N and 0<=c+dy<N:
                if paths[r+dx][c+dy] > money+maps[r+dx][c+dy]:
                    paths[r+dx][c+dy] = money+maps[r+dx][c+dy]
                    heapq.heappush(q, (paths[r+dx][c+dy], [r+dx, c+dy]))
    answer = paths[-1][-1]
    print(f'Problem {count}: {answer}')