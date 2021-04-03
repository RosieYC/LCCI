class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = matrix
        rows, cols = len(matrix), len(matrix[0])
        temp = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    temp.append((row, col))
        for x, y in temp:
            for i in range(rows):
                matrix[i][y] = 0 
            for i in range(cols):
                matrix[x][i] = 0
