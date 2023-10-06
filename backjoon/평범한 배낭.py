N, K = map(int, input().split(' '))
goods = [[0,0]]
for _ in range(N):
    goods.append(list(map(int, input().split(' '))))
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    w = goods[i][0]
    v = goods[i][1]
    for j in range(1, K+1):
        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v+knapsack[i-1][j-w], knapsack[i-1][j])
print(knapsack[N][K])
