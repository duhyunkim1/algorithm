N = int(input())
innings = [list(map(int, input().split(' '))) for _ in range(N)]
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

def play(b1, b2, b3, result, score, out):
    if result == 1:
        score += b3
        b1, b2, b3 = 1, b1, b2
    elif result == 2:
        score += (b2+b3)
        b1, b2, b3 = 0, 1, b1
    elif result == 3:
        score += (b1+b2+b3)
        b1, b2, b3 = 0, 0, 1
    elif result == 4:
        score += (b1+b2+b3+1)
        b1, b2, b3 = 0, 0, 0
    else:
        out+=1
    return b1, b2, b3, score, out
orders = permute([x for x in range(1,9)])
answer = 0
for order in orders:
    score = 0
    player_idx = 0
    for i, inning in enumerate(innings):
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out != 3:
            if player_idx == 3:
                b1, b2, b3, score, out = play(b1, b2, b3, inning[0], score, out)
            if player_idx < 3:
                b1, b2, b3, score, out = play(b1, b2, b3, inning[order[player_idx]], score, out)
            if player_idx > 3:
                b1, b2, b3, score, out = play(b1, b2, b3, inning[order[player_idx-1]], score, out)
            if player_idx < 8:
                player_idx += 1
            else:
                player_idx = 0
    if score > answer:
        answer = score
print(answer)