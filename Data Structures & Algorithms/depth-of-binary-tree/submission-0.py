# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
            we are given root of binary tree and need to return depth
            depth is defined as # of nodes along longest ath from root down to farthest leaf node

            1
           2 3
             4
            depth = 3
        1 
      1

      2   3
        '''
        def bfs(node):
            if not node:
                return 0
            
            return 1 + max(bfs(node.right), bfs(node.left))
        
        return bfs(root)