def add_matrices(matrix1, matrix2):
    # check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print ('Matrices must have same dimensions for addition')
    
    # Add the results
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def subtract_matrices(matrixone, matrixtwo):
    # Check for same dimensions
    if len(matrixone) != len(matrixtwo) or len(matrixone[0]) != len(matrixtwo[0]):
        print('Matrices must have same dimensions for subtraction')

    # Subtract the results

    result = []
    for i in range(len(matrixone)):
        row = []
        for j in range(len(matrixone[0])):
            row.append(matrixone[i][j] - matrixtwo[i][j])
        result.append(row)
    
    return result