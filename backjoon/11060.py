n = int(input())
a = list(map(int, input().split()))
dp = [-1 for _ in range(n+100)]
dp[0] = 0
for i in range(n):
    if dp[i] == -1:
        continue
    
    for j in range(1, a[i]+1):
        if dp[i+j] == -1:
            dp[i+j] = dp[i]+1
        else:
            dp[i+j] = min(dp[i+j], dp[i]+1)

print(dp[n-1])