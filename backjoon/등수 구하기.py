N, new, P = map(int, input().split(' '))
if N == 0:
    print(1)
    exit()
ranking = sorted(list(map(int, input().split(' '))), reverse=True)
if ranking[-1] >= new and N==P:
    print(-1)
    exit()
answer = N+1
for i in range(N):
    if ranking[i] <= new:
        answer = i+1
        break
print(answer)