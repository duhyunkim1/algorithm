def find_answer(next, answer, n):
    if len(answer) == n:
        print(' '.join(map(str, answer)))
        exit()
    start = answer[-1]
    if next[start][0] != -1:
        find_answer(next, answer+[next[start][0]], n)
    if next[start][1] != -1:
        find_answer(next, answer+[next[start][1]], n)

n = int(input())
nums = list(map(int, input().split(' ')))

next = {}
for num in nums:
    next[num] = [-1, -1]
    if num*2 in nums:
        next[num][0] = num*2
    if num//3 in nums:
        if num%3 == 0:
            next[num][1] = num//3
   
for num in nums:
    find_answer(next, [num], n)