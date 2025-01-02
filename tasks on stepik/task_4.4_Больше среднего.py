n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n):
    average = sum(matrix[i]) / n
    count = 0
    for j in range(n):
        if matrix[i][j] > average:
            count += 1
    print(count)