def solution(new, psb, nums):
    for i, x in enumerate(psb):
        for num in nums:
            if x == 1:        
               new[num+i] = 1 
    return new

n = int(input())
psb = [0 for x in range(50*n+1)]
nums = [1, 5, 10, 50]

for num in nums:
    psb[num] = 1

for _ in range(n-1):
    new = [0 for x in range(50*n+1)]
    psb = solution(new, psb, nums)
print(sum(psb))