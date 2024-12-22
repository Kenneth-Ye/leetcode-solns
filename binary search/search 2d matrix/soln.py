class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search its rows
        l = 0
        r = len(matrix) - 1
        index = -1
        while (l <= r):
            mid = l + (r - l) // 2
            if (target < matrix[mid][0]):
                r = mid - 1
            elif (target > matrix[mid][-1]):
                l = mid + 1
            elif (target >= matrix[mid][0] and target <= matrix[mid][-1]):
                index = mid
                break
        # search in seg
        if (index == -1): return False
        l = 0
        r = len(matrix[index]) - 1
        while(l <= r):
            if (matrix[index][l] == target or matrix[index][r] == target): return True
            middle = l + (r - l) // 2
            if (target < matrix[index][middle]):
                r = middle - 1
            elif (target > matrix[index][middle]):
                l = middle + 1
            else:
                return True
        return False
