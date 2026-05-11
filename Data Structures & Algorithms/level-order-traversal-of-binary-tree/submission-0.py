# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            given root
            return level order traversal of it as nested list 
            with each sublist contains the values of nodes at a 
            particular level from left to right

             1
           2   3
          4 5 6 7

          [[1]]
          go to next level
          [2,3]
          [[1],[2,3],[4,5,6,7]]
        '''
        res = []
        def dfs(root, index):
            if not root:
                return res
            if len(res) == index:
                res.append([])

            res[index].append(root.val)
            dfs(root.left, index + 1)
            dfs(root.right, index + 1)

        dfs(root, 0)
        return res
        



