def permutation(ls, n, nums):
    if len(ls) == 6:
        print(' '.join(map(str, ls)))
        return
    for idx, num in enumerate(nums):
        if num not in ls:
            permutation(ls+[num], n, nums[idx+1:])
    return

case = 0 
while True:
    a = list(map(int, input().split(' ')))
    n = a[0]
    a = a[1:]
    a.sort()
    if n == 0:
        break
    if case > 0:
        print()
    case+=1
    permutation([], n, a)
