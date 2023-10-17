inputs = input()
dictonary = {}

for x in inputs:
    try:
        dictonary[x.upper()] += 1
    except:
        dictonary[x.upper()] = 1
all = []
for k, v in dictonary.items():
    all.append([k, v])
all = sorted(all, key = lambda x: x[1], reverse=True)

if len(all)>1 and all[0][1] == all[1][1]:
    print("?")
    exit()
print(all[0][0])
