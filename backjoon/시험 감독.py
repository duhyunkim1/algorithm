N = int(input())
A = list(map(int, input().split(' ')))
B, C = map(int, input().split(' '))
answer = 0
for idx in range(N):
    A[idx] -= B
    answer += 1
    
for idx in range(N):
    if A[idx] <= 0:
        continue
    value = A[idx]//C
    if A[idx]%C == 0:
        answer += value
    else:
        answer += (value+1)
        
print(answer)