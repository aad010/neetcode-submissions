class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
            given mxn 2-d integer array (matrix) and a target value
            each row is in non-decreasing order
            first int of every row is greater than the last int of previous row (importnt fs)

            if target is there return true else false!

            [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
            3 rows and 4 columns = 1 
            left = 0, right = 12
            11 + 0 / 2 = 5
            5 // 3 = 1 
            5 % 4 = 1
            middle = 5 
            right = 4
            left = 0
            0 + 4 // 2 = 2 
            3  4
            5 + 0 // 2 = 2
            '''
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        while left <= right:
            middle = (right + left) // 2
            middleRow = middle // len(matrix[0])
            middleCol = middle % len(matrix[0])
            if matrix[middleRow][middleCol] == target:
                return True
            elif matrix[middleRow][middleCol] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return False