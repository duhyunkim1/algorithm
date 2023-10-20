N = int(input())
buildings = list(map(int, input().split(' ')))
answer = 0
for i in range(N):
    a = buildings[i]
    count = 0
    if i < N-1:
        for j in range(i+1, N):
            b = buildings[j]
            if j == i+1:
                high = ((a-b)/(i-j))    
                count+=1
                continue
            tmp = ((a-b)/(i-j))
            if tmp > high:
                high = tmp
                count+=1
            
    if i > 0:
        for j in range(i-1, -1, -1):
            b = buildings[j]
            if j == i-1:
                low = ((a-b)/(i-j))    
                count+=1
                continue
            tmp = ((a-b)/(i-j))
            if tmp < low:
                low = tmp
                count+=1
    if answer < count:
        answer = count
print(answer)

