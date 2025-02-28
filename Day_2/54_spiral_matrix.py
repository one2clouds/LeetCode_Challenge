def spiral_matrix(matrix):
    output = []
    while matrix:
        # take out the first row of matrix from left to right so matrix not reversed 
        output += matrix.pop(0)

        # take out last element from each row from top to bottom so matrix not reversed 
        if matrix and matrix[0]:
            for row in matrix:
                output.append(row.pop())
        
        # take out last row from right to left so matrix reversed 
        if matrix: 
            output += matrix.pop()[::-1]

        # reverse the matrix from down to up and take first element from down to up ## matrix is reversed
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                output.append(row.pop(0))
    return output



if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiral_matrix(matrix))
