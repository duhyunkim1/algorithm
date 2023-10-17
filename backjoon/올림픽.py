N, K = map(int, input().split())
scores = []
for _ in range(N):
    score = list(map(int, input().split(' ')))
    scores.append(score)
order = sorted(scores, key=lambda x: (x[1], x[2], x[3]), reverse = True)
for i, score in enumerate(order):
    if score[0] == K:
        flag = 0
        answer = 0
        for j, sub_score in enumerate(order[:i]):
            if sub_score[1:] != score[1:]:
                answer += 1
                flag = 1
        print(answer+1)


