matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix) # Initial 2D list

print("matrix[0]:"+str(matrix[0])) # First row
print("matrix[1][2]:"+str(matrix[1][2])) # Element at row 1, column 2

matrix[0][1] = 10
print(matrix) # After modifying an element


