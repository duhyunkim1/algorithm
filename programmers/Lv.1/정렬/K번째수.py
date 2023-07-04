def solution(array, commands):
    answer = []
    for command in commands:
        step1 = array[command[0]-1:command[1]]
        step1.sort()
        answer.append(step1[command[2]-1])
    return answer