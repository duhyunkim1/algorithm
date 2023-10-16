def solution(genres, plays):
    answer = []
    count_g = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        try:
            count_g[genre].append([i, play])
        except:
            count_g[genre] = [[i, play]]
    
    orders = []
    for k, v in count_g.items():
        sum_value = 0
        for _, x in v:
            sum_value+=x
        orders.append([k, v, sum_value])
    orders = sorted(orders, key = lambda x: x[2], reverse=True)
    
    answer = []
    for order in orders:
        cut = min([2, len(order[1])])
        for x, _ in sorted(order[1], key = lambda x: x[1], reverse=True)[:cut]:
            answer.append(x)
    return answer