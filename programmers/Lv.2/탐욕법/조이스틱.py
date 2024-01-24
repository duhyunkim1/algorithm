def solution(name):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    len_alphabet = len(alphabet)
    last_idx = -1
    up_down = 0
    a_idx = []
    for idx, apb in enumerate(name):
        location = alphabet.index(apb)
        up_down += min(location, len_alphabet-location)
        if apb != 'A':
            last_idx = idx  
        if apb == 'A' and idx != 0:
            start_idx = idx
            for idx, apb in enumerate(name[start_idx:]):
                if apb == 'A':
                    end_idx = start_idx+idx
                else:
                    break
            a_idx.append([start_idx, end_idx])
    if len(name) == 1 or last_idx == -1:
        return up_down

    left_right = last_idx
    for start, end in a_idx:
        move = min(2*(start-1) + len(name)-end-1, start-1 + 2*(len(name)-end-1))
        if move < left_right:
            print(start, end)
            left_right = move
    return up_down + left_right