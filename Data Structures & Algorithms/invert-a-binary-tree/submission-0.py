# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
            goal: given root of binary tree (root) invert tree and return root

            1
           2 3
          4 5 6 7  

          1
         3  2

        '''

        def bfs(node):
            if not node:
                return 
            
            temp = node.right
            node.right = bfs(node.left)
            node.left = bfs(temp)

            return node
        return bfs(root)
            