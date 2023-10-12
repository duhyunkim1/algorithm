N = int(input())
tasks = [list(map(int, input().split(' '))) for _ in range(N)]
answer = 0
def dfs(tasks, count):
    global answer
    if count > answer:
        answer = count
    for idx in range(len(tasks)):
        period = tasks[idx][0]
        gain = tasks[idx][1]
        if idx+period <= len(tasks):
            remain_tasks = tasks[idx+period:]
            dfs(remain_tasks, count+gain)

dfs(tasks, 0)
print(answer)