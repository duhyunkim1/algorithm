from itertools import permutations
k = int(input())
problem = list(input().split(' '))

answers = []
cases = permutations(list(range(0,10)), k+1)
for c in cases:
    flag = 0
    for i in range(k):
        if problem[i] == '<':
            if c[i] > c[i+1]:
                flag = 1
                break
        elif problem[i] == '>':
            if c[i] < c[i+1]:
                flag = 1
                break
    if flag == 0:
        answers.append(''.join(map(str, c)))
        
print(max(answers))
print(min(answers))
         