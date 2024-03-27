from itertools import combinations

def check(com, l, r, x):
    com = list(com)
    
    sum_v = sum(com)
    min_v = min(com)
    max_v = max(com)
    if l<=sum_v and r>=sum_v and max_v-min_v >= x:
        is_pos = 1
    else:
        is_pos = 0
    return is_pos
        
n, l, r, x = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

answer = 0
for i in range(2, n+1):
    for com in combinations(a, i):
        answer += check(com, l, r, x)
print(answer)