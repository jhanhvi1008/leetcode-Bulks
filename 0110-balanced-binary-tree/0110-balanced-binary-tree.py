# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        
        # Function to calculate height
        def height(node):
            
            # Base case
            if not node:
                return 0

            # Find height of left subtree
            left_height = height(node.left)

            # If left subtree is already unbalanced
            if left_height == -1:
                return -1

            # Find height of right subtree
            right_height = height(node.right)

            # If right subtree is already unbalanced
            if right_height == -1:
                return -1

            # Check balance condition
            if abs(left_height - right_height) > 1:
                return -1

            # Return height of current node
            return max(left_height, right_height) + 1

        # Tree is balanced if height function doesn't return -1
        return height(root) != -1
        