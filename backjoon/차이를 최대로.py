def calcuate(a):
    i = 0
    value = 0
    while i < len(a)-1:
        value += abs(a[i]-a[i+1])
        i += 1
    return value

def permutation(ls, n, nums, visited):
    if len(ls) == n:
        tmp = calcuate(ls)
        global answer
        if answer < tmp:
            answer = tmp
        return
    for idx, num in enumerate(nums):
        if not visited[idx]:
            visited[idx] = True
            permutation(ls+[num], n, nums, visited)
            visited[idx] = False
    return

n = int(input())
a = list(map(int, input().split(' ')))
a.sort()
answer = 0
visited = [False for _ in range(n+1)]
permutation([], n, a, visited)
print(answer)