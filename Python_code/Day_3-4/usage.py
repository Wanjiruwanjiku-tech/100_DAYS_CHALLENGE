from functions import add_matrices
from functions import subtract_matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix2 = [
    [7, 8, 9],
    [10, 11, 12]
]

result = add_matrices(matrix1, matrix2)
print('Your result is: {}'.format(result))

result = subtract_matrices(matrix2, matrix1)
print('Your Subtraction result is: {}'.format(result))