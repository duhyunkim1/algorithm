import sys
N, M = list(map(int, sys.stdin.readline().split()))
table = []
for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))
    
dp = [[0]*(N+1) for _ in range(N+1)]    
for x in range(1, N+1):
    for y in range(1, N+1):
        dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] + table[x-1][y-1]
                
for _ in range(M):
    answer = 0 
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)