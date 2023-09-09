def solution(numbers, target):
    answer = 0
    sum_ls = [numbers[0], -numbers[0]]
    for num in numbers[1:]:
        tmp_ls = []
        for tmp in sum_ls:
            tmp_ls.append(tmp+num)
            tmp_ls.append(tmp-num)
        sum_ls=tmp_ls
    for num in sum_ls:
        if num==target:
            answer+=1
    return answer