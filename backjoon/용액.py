import sys
N = int(input())
liquid = list(map(int, input().split(' ')))
liquid = sorted(liquid, key = lambda x: abs(x))

value = sys.maxsize
for i in range(N-1):
    if value > abs(liquid[i] + liquid[i+1]):
        value = abs(liquid[i] + liquid[i+1])
        answer = [liquid[i], liquid[i+1]]

print(' '.join([str(x) for x in sorted(answer)]))
