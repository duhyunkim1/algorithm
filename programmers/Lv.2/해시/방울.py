def solution(bell):
    bell = [-1 if b == 1 else 1 for b in bell]
    bell_accum = [0]
    for b in bell:
        bell_accum.append(bell_accum[-1]+b)
    start = {}
    end = {}
    for i, x in enumerate(bell_accum):
        if x not in start:
            start[x] = i
        end[x] = i
    return max(end[x] - start[x] for x in end)