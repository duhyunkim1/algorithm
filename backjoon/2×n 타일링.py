dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
n = int(input())
for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)