text = input().split()

res = []
for i in range(len(text)):
    for j in range(i, len(text)):
        res.append(text[i:j+1])
res.sort(key=len)
res.insert(0, [])
print(res)

