from collections import defaultdict
N = int(input())
A = list(map(int, input().split(' ')))
goods = defaultdict(list)
count = 0

for i, a in enumerate(A):
    for j, b in enumerate(A):
        if j<=i:
            continue
        goods[a+b].append([i,j])

for n in range(N):
    for i, j in goods[A[n]]:
        if i!=n and j!=n:
            count+=1
            break
        
print(count)
