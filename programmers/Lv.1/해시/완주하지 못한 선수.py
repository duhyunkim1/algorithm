def solution(participant, completion):
    dictionary = {}
    value = 0
    for p in participant:
        dictionary[hash(p)] = p
        value += hash(p)
        
    for c in completion:
        value -= hash(c)
    
    return dictionary[value]