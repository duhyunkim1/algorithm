def calculate(ls):
    result = int(ls[0])
    for i, x in enumerate(ls):
        if x == '*':
            result *= int(ls[i+1])
        elif x == '+':
            result += int(ls[i+1]) 
        elif x == '-':
            result -= int(ls[i+1])
    return result

def dfs(ls):
    global answer
    tmp = calculate(ls)
    if tmp > answer:
        answer = tmp
    for idx in range(len(ls)-1):
        if idx%2 != 0:
            continue
        if type(ls[idx]) != int or type(ls[idx+2]) != int:
            continue
        value = calculate(ls[idx:idx+3])
        dfs(ls[:idx]+[str(value)]+ls[idx+3:])
    

n = int(input())
case = [int(x) if i%2 ==0 else x for i,x in enumerate(input())]

answer = -2**31    
dfs(case)
    
print(answer)