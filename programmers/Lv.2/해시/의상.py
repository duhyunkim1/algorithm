def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        name, kind = cloth 
        try:
            clothes_dict[kind].append(name)
        except:
            clothes_dict[kind] = []
            clothes_dict[kind].append(name)
    answer = 1
    for v in clothes_dict.values():
        answer*=(len(v)+1)
    answer-=1    
    return answer