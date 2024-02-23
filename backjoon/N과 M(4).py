n, m = map(int, input().split(' '))
numbers = [x for x in range(1, n+1)]

def dfs(ls, numbers, m):
    if len(ls) == m+1:
        print(' '.join(map(str, ls[1:])))
    else:    
        for idx, number in enumerate(numbers):
            if number >= ls[-1]:
                dfs(ls+[number], numbers, m)

dfs([0], numbers, m)                    
