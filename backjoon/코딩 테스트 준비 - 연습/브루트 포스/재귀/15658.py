n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))
        
cases = []
def dfs(operator, now):
    global cases
    if len(now) == n-1:
        cases.append(now)
        return
    for order in range(0, 4):
        if operator[order] > 0:
            operator[order] -= 1
            dfs(operator, now+[order])
            operator[order] += 1
        
dfs(operator, [])

def calculate(case):
    result = a[0]
    for idx in range(n-1):
        o = case[idx]
        if o == 0:
            result += a[idx+1]
        elif o == 1:
            result -= a[idx+1]
        elif o == 2:
            result *= a[idx+1]
        else:
            if result < 0:
                result = -(abs(result)//a[idx+1])
            else:
                result = abs(result)//a[idx+1]
    return result
            
results = []    
for case in cases:
    results.append(calculate(case))
print(max(results))
print(min(results))