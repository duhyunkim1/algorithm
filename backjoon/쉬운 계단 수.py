dp = [[0]*10 for _ in range(101)]
dp[1] = [0] + [1] * 9

for i in range(2, 101):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    
    for k in range(1,9):
        dp[i][k] += dp[i-1][k-1]
        dp[i][k] += dp[i-1][k+1]
    
    for k in range(10):
        dp[i][k]%=1000000000
print(sum(dp[int(input())])%1000000000)

