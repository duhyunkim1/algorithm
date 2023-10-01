from itertools import combinations
N, M, D = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(N)]
candidates = list(combinations([i for i in range(M)], 3))
answers = []
for candidate in candidates:
    answer = 0
    distance = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(3)]
    can1 = [N, candidate[0]]
    can2 = [N, candidate[1]]
    can3 = [N, candidate[2]]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                distance[0][i][j] = abs(i-can1[0]) + abs(j-can1[1])
                distance[1][i][j] = abs(i-can2[0]) + abs(j-can2[1])
                distance[2][i][j] = abs(i-can3[0]) + abs(j-can3[1])
    delete = []
    for z in range(N):
        attack = [[] for _ in range(3)]
        for k in range(3):
            for i in range(N-z):
                for j in range(M):
                    if 0 < distance[k][i][j] <= D and [i, j] not in delete:
                        attack[k].append([distance[k][i][j], i, j])    
                    distance[k][i][j] -= 1

        for k in range(3):
            attack[k].sort(key=(lambda x: (x[0], x[2])))
            if len(attack[k])>0:
                if attack[k][0][1:] in delete:
                    continue
                else:
                    delete.append(attack[k][0][1:])
    answers.append(len(delete))
print(max(answers))