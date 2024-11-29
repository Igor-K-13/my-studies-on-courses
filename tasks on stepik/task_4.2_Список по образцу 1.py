n = int(input())
my_list = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        my_list.append(j)
    print(my_list)
    my_list.clear()


