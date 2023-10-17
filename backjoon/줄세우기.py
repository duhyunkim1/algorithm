import sys
P = int(input())
for _ in range(P):
    case = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    T = case[0]
    line = [case[1]]
    count = 0
    for student in case[2:]:
        done = False
        for i, s in enumerate(line):
            if student < s: 
                count += len(line) - i
                line.insert(i, student)
                done = True
                break
        if done == False:
            line.append(student)
    print(T, count)

