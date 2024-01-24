def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    for p in people:
        answer += 1
        if people[-1] <= limit-p:
            people.pop()
    return answer
