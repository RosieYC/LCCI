class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        end = len(matrix)-1
        while((end-start)>=1):
            for y in range(start, end):
               temp = matrix[start][y] # matrix[0,0]
               matrix[start][y] = matrix[end-y+start][start] # matrix[0,0] = matrix[4, 0]
               matrix[end-y+start][start] = matrix[end][end-y+start]  # matrix[4,0] = matrix[4,4]
               matrix[end][end-y+start] = matrix[y][end] # matrix[4,4] = matrix[0, 4]
               matrix[y][end] = temp
            end -= 1
            start +=1
