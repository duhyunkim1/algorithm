while True:
    triangle = list(map(int, input().split(' ')))
    triangle = sorted(triangle, reverse=True)
    if triangle == [0, 0, 0]:
        break
    elif triangle[0] >= sum(triangle[1:]):
        print("Invalid")
    elif triangle[0] == triangle[1] == triangle[2]:
        print("Equilateral")
    elif triangle[0] == triangle[1] or triangle[0] == triangle[2] or triangle[1] == triangle[2]:
        print("Isosceles")
    else:
        print("Scalene")