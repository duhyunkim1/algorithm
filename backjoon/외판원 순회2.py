def calcuate(a, w):
    i = 0
    value = 0
    a.append(a[0])
    while i < len(a)-1:
        if w[a[i]][a[i+1]] == 0:
            return False
        value += w[a[i]][a[i+1]]
        i += 1 
    return value

def permutation(ls, n, nums, visited, w):
    if len(ls) == n:
        tmp = calcuate(ls, w)
        
        global answer
        if tmp is not False and answer > tmp:
            answer = tmp
        return
    for idx, num in enumerate(nums):
        if not visited[idx]:
            visited[idx] = True
            permutation(ls+[num], n, nums, visited, w)
            visited[idx] = False
    return

n = int(input())
w = []
for _ in range(n):
    w.append(list(map(int, input().split(' '))))
a = [x for x in range(n)]
answer = 1000000*n
visited = [False for _ in range(n+1)]
visited[0] = True
permutation([0], n, a, visited, w)
print(answer)