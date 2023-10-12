N = int(input())
numbers = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))

def dfs(number, oper):
    global results
    if len(number) == 1:
        results.append(number[0])
        return

    for i in range(4):
        num = number[:]
        if oper[i] > 0:
            a = num.pop(0)
            b = num.pop(0)
            if i == 0:
                num.insert(0, a+b)
            if i == 1:
                num.insert(0, a-b)
            if i == 2:
                num.insert(0, a*b)
            if i == 3:
                if a<0 and b>0:
                    num.insert(0, -(-a//b))
                else:
                    num.insert(0, a//b)
            new_oper = oper[:]
            new_oper[i] -= 1
            dfs(num, new_oper)
results = []
dfs(numbers, operators)
print(max(results))
print(min(results))