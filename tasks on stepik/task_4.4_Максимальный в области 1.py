n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
max_elem = matrix[0][0]
for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
print(max_elem)