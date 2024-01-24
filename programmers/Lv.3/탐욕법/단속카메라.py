def solution(routes):
    routes.sort(key = lambda x: x[1])
    cam = -30000
    answer = 0
    for start, end in routes:
        if start <= cam and cam <= end:
            continue
        else:
            cam = end
            answer+=1
    return answer