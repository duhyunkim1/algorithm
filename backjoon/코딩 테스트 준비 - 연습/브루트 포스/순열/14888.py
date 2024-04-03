n = int(input())
nums = list(map(int, input().split( )))
oper = []
for i, x in enumerate(list(map(int, input().split( )))):
    for _ in range(x):
        oper.append(i)

orders = []   
def permutations(ls, visited):
    if False not in visited:
        orders.append(ls)
    
    for i, x in enumerate(oper):
        if not visited[i]:
            visited[i] = True
            permutations(ls+[x], visited)
            visited[i] = False
            
permutations([], [False for _ in range(len(oper))])            

max_v = -1000000000
min_v = 1000000000
for order in orders:
    answer = nums[0]
    for i, o in enumerate(order):
        if o == 0:
            answer += nums[i+1]
        elif o == 1:
            answer -= nums[i+1]
        elif o == 2:
            answer *= nums[i+1]
        else:
            tmp = abs(answer)//nums[i+1]
            if answer < 0:
                answer = -tmp
            else:
                answer = tmp
            
    max_v = max(max_v, answer)
    min_v = min(min_v, answer)
    
print(max_v)
print(min_v)