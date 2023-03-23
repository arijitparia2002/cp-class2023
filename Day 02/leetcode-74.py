# 74. Search a 2D Matrix
# Solution link : https://leetcode.com/problems/search-a-2d-matrix/solutions/3332645/simple-binary-search-solution-with-python/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])

        low = 0
        high = row*col - 1

        while low <= high:
            mid = (low + high) // 2

            i, j = mid // col, mid % col
            print(mid,i,j)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False