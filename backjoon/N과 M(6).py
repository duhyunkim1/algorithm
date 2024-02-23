n, m = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))
numbers.sort()

def dfs(ls, numbers, m):
    if len(ls) == m:
        print(' '.join(map(str, ls)))
    
    for idx, number in enumerate(numbers):
        if number not in ls:
            dfs(ls+[number], numbers[idx+1:], m)

dfs([], numbers, m)                    
