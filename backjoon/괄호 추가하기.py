def dfs(case):
    answer = int(case[0])
    for i, x in enumerate(case[:-1]):
        if i%2 == 1:
            if case[i] == '+':
                answer += int(case[i+1])
            if case[i] == '*':
                answer *= int(case[i+1])
            if case[i] == '-':
                answer -= int(case[i+1])
    results.append(int(answer))
    
    for i, x in enumerate(case[:-1]):
        if type(x) != int or type(case[i+2]) != int:
            continue
        if case[i+1] == '+':
            tmp = case[i] + case[i+2]
        if case[i+1] == '*':
            tmp = case[i] * case[i+2]
        if case[i+1] == '-':
            tmp = case[i] - case[i+2]
        new_case = case[:i] + [str(tmp)] + case[i+3:]
        dfs(new_case)
N = int(input())
inputs = input()
case = []
for i in range(N):
    if i%2 == 0:
        case.append(int(inputs[i]))
    else:
        case.append(inputs[i])
results = []

dfs(case)
print(max(results))