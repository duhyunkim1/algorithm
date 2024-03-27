a, b, c, x, y = map(int, input().split(' '))

answer = 0
if a+b > 2*c:
    min_value = min([x, y])
    answer += min_value*(2*c)
    x -= min_value   
    y -= min_value

answer += min([a, 2*c])*x
answer += min([b, 2*c])*y

print(answer)