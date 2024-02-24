def plus(x, goal):
    if x > goal:
        return
    
    if x == goal:
        global answer
        answer+=1
        return 
    
    for i in range(1,4):
        plus(x+i, goal)

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    plus(0, n)
    print(answer)