# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]
#matrix[0][1] = 20               #to modify an element out of a matrix and override
#to access individual element from the matrix
print(matrix[0][1])
print('')
for row in matrix:
    for element in row:
        print(element)