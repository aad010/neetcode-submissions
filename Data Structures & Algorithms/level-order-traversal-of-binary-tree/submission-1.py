from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        vals = []
        queue = deque([root])

        while queue:
            level = []
            level_len = len(queue)

            for i in range(level_len):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            vals.append(level)

        return vals