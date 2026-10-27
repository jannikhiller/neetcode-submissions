from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect_left(matrix, target, key=lambda r: r[-1])
        if row >= len(matrix):
            return False
        col = bisect_left(matrix[row], target)
        return col < len(matrix[row]) and matrix[row][col] == target
        
        