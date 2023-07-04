def solution(citations):
    citations.sort(reverse=True)
    len_c = len(citations)
    answer=0
    for i, h in enumerate(citations):
        if i+1>=h:
            answer = max([h, answer])
        else:
            answer = max([i+1, answer])
    return answer