# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
            given roots of p and q
            return True if trees are equiv else false

            1   1
           2 3 2 3

        1  1
       2 3 23
        '''

        def dfs(rootOne, rootTwo):
            if not rootOne and not rootTwo:
                return True
            
            if (not rootOne and rootTwo) or (rootOne and not rootTwo):
                return False 

            if rootOne.val == rootTwo.val:
                return True and dfs(rootOne.left, rootTwo.left) and dfs(rootOne.right, rootTwo.right)
            else:
                return False
        
        return dfs(p, q)