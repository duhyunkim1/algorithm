from itertools import permutations
def solution(k_init, dungeons):
    answer=0
    num_d = len(dungeons)
    paths = permutations(list(range(num_d)), num_d)
    for path in paths:
        k = k_init
        count = 0
        for p in path:
            if k >= dungeons[p][0] and k >= dungeons[p][1]:
                k -= dungeons[p][1]
                count+=1
            else:
                break
        if answer < count:
            answer = count
    return answer