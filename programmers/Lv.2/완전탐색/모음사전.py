from itertools import product
def solution(word):
    order = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for num in range(1,6):
        for w in product(order, repeat=num):
            w_sum = ''.join(w)
            dictionary.append(w_sum)
    dictionary.sort()
    answer = dictionary.index(word)
    return answer+1