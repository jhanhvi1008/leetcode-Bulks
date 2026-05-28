# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        
        # If tree is empty
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        # Traverse until queue becomes empty
        while queue:
            
            level = []
            level_size = len(queue)
            
            # Process all nodes of current level
            for i in range(level_size):
                
                node = queue.popleft()
                level.append(node.val)
                
                # Add left child
                if node.left:
                    queue.append(node.left)
                
                # Add right child
                if node.right:
                    queue.append(node.right)
            
            # Add current level to result
            result.append(level)
        
        return result
        