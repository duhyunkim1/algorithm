def solution(numbers, target):        
    def dfs(num_ls, target_v, answer):
        if len(num_ls) == 0:
            if target_v == target:
                answer+=1
        else:
            answer = dfs(num_ls[1:], target_v + num_ls[0], answer)
            answer = dfs(num_ls[1:], target_v - num_ls[0], answer)
        return answer 
    answer = dfs(numbers, 0, 0)
    return answer