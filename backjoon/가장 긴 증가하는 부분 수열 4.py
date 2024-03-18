n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]
dp_idx = [-1 for _ in range(n)]

for i in range(1, n):
    max_num = 0
    max_idx = -1
    for j in range(i):
        if a[j] < a[i] and max_num < dp[j]:
            max_num = dp[j]
            max_idx = j
    dp[i] += max_num
    dp_idx[i] = max_idx
answer = max(dp)
idx = dp.index(answer)
answer_ls = []
while idx != -1:
    answer_ls.append(a[idx])
    idx = dp_idx[idx]
answer_ls.reverse()
print(answer)
print(' '.join(map(str, answer_ls)))

