class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        print(l, r)
        while l <= r:
            m = (l + r) // 2
            r_val = m // len(matrix[0])
            c = m % len(matrix[0])
            print(r_val)
            if matrix[r_val][c] == target:
                return True 
            elif matrix[r_val][c] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False