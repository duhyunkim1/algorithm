import copy
def solution(triangle):
    original = copy.deepcopy(triangle)
    for i, line in enumerate(triangle[:-1]):
        for j, num in enumerate(line):
            if num+original[i+1][j] > triangle[i+1][j]:
                triangle[i+1][j] = num+original[i+1][j]
            if num+original[i+1][j+1] > triangle[i+1][j+1]:
                triangle[i+1][j+1] = num+original[i+1][j+1]
    return max(triangle[-1])