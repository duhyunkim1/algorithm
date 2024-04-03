k = int(input())
oper = list(input().split())

def dfs(step, ls):
    global answer
    if step == k:
        answer.append(''.join(map(str, ls)))
        return

    if oper[step] == '<':
        for x in range(ls[-1]+1, 10):
            if x not in ls:
                dfs(step+1, ls+[x])
    else:
        for x in range(0, ls[-1]):
            if x not in ls:
                dfs(step+1, ls+[x])
                
answer = []
for x in range(10):
    dfs(0, [x])
print(max(answer))
print(min(answer))