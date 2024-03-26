num = {}
num['d'] = 10
num['c'] = 26

q = input()

if len(q) == 0:
    print(0)
    exit()

before = q[0]
answer = num[before]
for x in q[1:]:
    if before == x:
        answer *= (num[x]-1)
    else:
        answer *= (num[x])
    before = x
        
print(answer)