class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.sumMat[r+1][c+1] = self.sumMat[r+1][c] + self.sumMat[r][c+1] - self.sumMat[r][c] + matrix[r][c]

        print(self.sumMat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.sumMat[row2+1][col2+1] -
                self.sumMat[row2+1][col1] -
                self.sumMat[row1][col2+1] +
                self.sumMat[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)