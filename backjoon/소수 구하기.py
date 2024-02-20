m, n = map(int, input().split(' '))

is_del = [False for _ in range(n+2)]

for idx in range(2, n+1):
    if idx >= m and is_del[idx] == False:
        print(idx)
    i = 1
    while i*idx <= n:
        is_del[i*idx] = True
        i += 1