class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        row = len(matrix)
        col = len(matrix[0])
        start_row, start_col, end_row, end_col = 0,0,row, col 
        result = []
        if row == 1:
            return matrix[0]
        if col == 1 :
            for i in range(start_row, end_row):
                result.append(matrix[i][end_col-1])
            return result
        k  = max(row, col)-2
        cur = 1
        while end_row > start_row and end_col > start_col :
            if cur == 1 :
                for i in range(start_col, end_col):
                    result.append(matrix[start_row][i])
                start_row += 1 
                cur = 2
            elif cur == 2:
                if k != max(row, col)-2:
                    end_row -= 1 
                for i in range(start_row, end_row):
                    result.append(matrix[i][end_col-1])
                end_col -= 1 
                cur = 3
            elif cur == 3:
                if k != max(row, col)-2:
                    start_col += 1 
                for i in range(end_col-1, start_col-1, -1):
                    result.append(matrix[end_row-1][i])
                end_row -=1 
                cur = 4
            elif cur ==4:
                if k != max(row, col)-2:
                    start_row += 1 
                if end_row <0:
                    break
                for i in range(end_row-1, start_row-1, -1):
                    result.append(matrix[i][start_col])
                start_col += 1 
                if k != max(row, col)-2:
                    end_col -= 1 
                cur = 1
            else:
                break
        return result
