text = input().split()

# for i in range(len(text)):
#     res.append(list(text[i]))
res_1 = []
for i in range(len(text)):
    for j in range(i, len(text)):
        res_1.append(text[i:j+1])

print(res_1)

