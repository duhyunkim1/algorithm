n = int(input())
a = list(map(int, input().split(' ')))

for i in range(1, n):
    tmp = a[i]+a[i-1]
    if tmp > a[i]:
        a[i] = tmp
print(max(a))
