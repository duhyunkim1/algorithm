def check(ls):
    tmp = ls[0]-ls[1]
    for idx in range(1, len(ls)-1):
        if tmp != ls[idx]-ls[idx+1]:
            return False
    return True

def sol(b, diff, answer, n):
    global results
    for i in range(2, n):
        if diff == (b[i-1]-(b[i]-1)):
            b[i] -= 1
            answer += 1
            
        elif diff == (b[i-1]-(b[i]+1)):
            b[i] += 1
            answer += 1
    if check(b):
        results.append(answer)        
            
            
n = int(input())
b_init = list(map(int, input().split(' ')))
if n == 1 or n == 2:
    print(0)
else:
    cases =[-1, 1, 0]
    results =[]
    for x in cases:
        for y in cases:
            b_init[0] += x
            b_init[1] += y
            sol(b_init[:], b_init[0]-b_init[1], abs(x)+abs(y), n)
            b_init[0] -= x
            b_init[1] -= y
            
    if len(results) != 0:
        print(min(results))
    else:
        print(-1)
