# If any cell is 0, set its entire row and column to 0 in-place

def matrix_zeroes(matrix):
    if not matrix or not matrix[0]:
        return []

    zero_rows = set()
    zero_cols = set()

    m, n  = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    return matrix


print(matrix_zeroes([[1, 2, 3], [4, 5, 0], [7, 8, 9]]))