class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        left_r, right_r = 0, row - 1
        row = 0
        while left_r <= right_r:
            mid = (left_r + right_r) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            elif target > matrix[mid][-1]:
                left_r = mid + 1
            else:
                right_r = mid -1
        

        return target in matrix[row]