"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}


        def dfs(node):
            if node == None:
                return None
            new_node = Node(node.val, [])
            seen[new_node.val] = new_node
            
            for neighbor in node.neighbors:
                if neighbor.val in seen:
                    new_node.neighbors.append(seen[neighbor.val])
                else:
                    new_node.neighbors.append(dfs(neighbor))
            return new_node
        
        return dfs(node)

        
        