class Solution:
    def preorderTraversal(self, root):
        result = []

        if root is None:
            return result

        stack = [root]

        while stack:
            node = stack.pop()

            # Visit the root
            result.append(node.val)

            # Add right first
            if node.right:
                stack.append(node.right)

            # Add left second
            if node.left:
                stack.append(node.left)

        return result
        
        