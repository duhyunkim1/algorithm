def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
num1, num2 = map(int, input().split(' '))
g = gcd(num1, num2)
print(g)
print(num1*num2//g)