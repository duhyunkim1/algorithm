n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    max_num = 0
    for j in range(i):
        if a[j] < a[i] and max_num < dp[j]:
            max_num = dp[j]
    dp[i] += max_num
        
print(max(dp))
