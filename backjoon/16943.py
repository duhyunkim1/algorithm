from itertools import permutations
A, B = input().split(' ')

b_v = int(B)
A = [x for x in A]
B = [x for x in B]
c = -1

for perm in permutations(A):
    a = ''.join(perm)
    if a[0] == '0':
        continue
    a = int(a)
    if a < b_v:
        c = max(c, a)
        
print(c)
        
    