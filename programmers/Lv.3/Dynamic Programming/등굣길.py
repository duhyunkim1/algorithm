def solution(m, n, puddles):
    maps = [[0 for _ in range(m+1)] for _ in range(n+1)]
    maps[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i== 1 and j==1:
                continue
            if [i, j] in puddles:
                maps[j][i] = 0
            else:
                maps[j][i] = maps[j-1][i] + maps[j][i-1]
    return maps[-1][-1]%1000000007