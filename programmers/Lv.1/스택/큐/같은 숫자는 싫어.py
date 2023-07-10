def solution(arr):
    answer = []
    for i, x in enumerate(arr):
        if i == 0:
            answer.append(x)
        if answer[-1] != x:
            answer.append(x)
    return answer