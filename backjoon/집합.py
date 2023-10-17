import sys
M = int(input())
num_set = set()
for _ in range(M):
    inputs = list(sys.stdin.readline().rstrip().split(' '))
    f = inputs[0]
    try:
        x = int(inputs[1])
    except:
        if f == 'all':
            ls = []
            for x in range(1, 21):
                ls.append(x)
            num_set = set(ls)
        elif f == 'empty':
            num_set = set()
        continue
    if f == 'add':
        num_set.add(x)
    elif f == 'remove':
        num_set.discard(x)
    elif f == 'check':
        print(1 if x in num_set else 0)
    elif f == 'toggle':
        if x in num_set:
            num_set.discard(x)
        else:
            num_set.add(x)