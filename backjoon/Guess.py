k = int(input())
problem = input()
maps = [[-1 for _ in range(k)] for _ in range(k)]
now = 0
for i in range(k):
    for j in range(k):
        if i <= j:
            maps[i][j] = problem[now]
            now+=1
def check(c):
    flag = 0
    now = len(c)
    for i in range(now):
        tmp = sum(c[i:now+1])    
        compare = maps[i][now-1]
        if compare == '+':
            if tmp <= 0:
                flag = 1
                break
        elif compare == '-':
            if tmp >= 0:
                flag = 1
                break
        elif compare == '0':
            if tmp != 0:
                flag = 1
                break  
    return flag    
def get_case(ls, k, nums):
    flag = check(ls)
    if flag == 0: 
        if len(ls) == k:
            print(' '.join(map(str, ls)))
            exit()
        else:
            compare = maps[len(ls)][len(ls)]
            for num in nums:
                if compare == '+':
                    get_case(ls+[num], k, nums)
                elif compare == '-':
                    get_case(ls+[-num], k, nums)
                elif compare == '0':
                    get_case(ls+[0], k, nums)
                    break

nums = [x for x in range(1, 11)]
get_case([], k, nums)            
        