def solution(answers)
    answer = []
    one = 0
    two = 0
    three = 0
    a_one = [1,2,3,4,5]
    a_two = [2,1,2,3,2,4,2,5]
    a_three = [3,3,1,1,2,2,4,4,5,5]
    for i, x in enumerate(answers)
        if x == a_one[i%5]
            one+=1
        if x == a_two[i%8]
            two+=1
        if x == a_three[i%10]
            three+=1
    a_all = [one, two, three]
    max_value = max(a_all)
    for i, a in enumerate(a_all)
        if max_value == a
            answer.append(i+1)
    return answer