N = int(input())
cases = [list(map(int, input().split(' '))) for _ in range(N)] 
answers = []

for i, case in enumerate(cases):
    answer = 0
    for j, sub_case in enumerate(cases):
        if i == j:
            continue
        if case[0] < sub_case[0] and case[1] < sub_case[1]:
            answer += 1
    answers.append(answer)
answers = [str(x+1) for x in answers]
print(' '.join(answers))