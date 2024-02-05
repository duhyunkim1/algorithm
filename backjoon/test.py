N = int(input())
answer = 0
for k in range(1, N+1):
    answer += k*(N//k)
print(answer)
