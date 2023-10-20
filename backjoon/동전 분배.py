def solution(N):
    coins = [list(map(int, input().split(' '))) for _ in range(N)]
    coins = sorted(coins, key=lambda x: x[0], reverse=True)

    total = 0
    for value, cnt in coins:
        total += (value*cnt)
    if total % 2 != 0:
        print(0)
        return
    half = total//2
    dp = [True] + [False] * half
    for value, cnt in coins:
        for now in range(half, value-1, -1):
            if dp[now-value]:
                for j in range(cnt):
                    if now + value*j <= half:
                        dp[now + value*j] = True
                    else:
                        break
    if dp[-1]:
        print(1)
        return
    print(0)
    return
        
for _ in range(3):
    solution(int(input()))