def solution(number, k):
    answer = ''
    len_num = len(number)
    K = len_num - k
    start = 0
    while K != 0:
        cosider = number[start:len_num-K+1]
        max_value = -1
        for idx, num in enumerate(cosider):
            if max_value < int(num):
                max_value = int(num)
                max_idx = idx
                if int(num) == 9:
                    break
        answer += str(max_value)
        start += max_idx+1
        K -=1
    return answer