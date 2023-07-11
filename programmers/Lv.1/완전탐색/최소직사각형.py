def solution(sizes):
    min_value = []
    max_value = []
    for size in sizes:
        min_value.append(min(size))
        max_value.append(max(size))
    answer = max(min_value)*max(max_value)
    return answer