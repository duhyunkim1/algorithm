n, m = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))
numbers.sort()

def dfs(ls, numbers, m):
    if len(ls) == m:
        print(' '.join(map(str, ls)))
    else:    
        for idx, number in enumerate(numbers):
            dfs(ls+[number], numbers, m)

dfs([], numbers, m)                    