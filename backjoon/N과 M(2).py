n, m = map(int, input().split(' '))
numbers = [x for x in range(1, n+1)]

def dfs(ls, numbers, m):
    if len(ls) == m:
        print(' '.join(map(str, ls)))
    
    for idx, number in enumerate(numbers):
        if number not in ls:
            dfs(ls+[number], numbers[idx+1:], m)

dfs([], numbers, m)                    
