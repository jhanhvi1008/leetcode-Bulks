class Solution:
    def maxDepth(self, root):
        # Base case: if the tree is empty
        if root is None:
            return 0

        # Find depth of left subtree
        left_depth = self.maxDepth(root.left)

        # Find depth of right subtree
        right_depth = self.maxDepth(root.right)

        # Return the larger depth + 1 for current node
        return max(left_depth, right_depth) + 1