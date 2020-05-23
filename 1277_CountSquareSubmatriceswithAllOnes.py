class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        out = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and i>0 and j>0:
                    matrix[i][j] = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])+1
                out += matrix[i][j]
        return out
