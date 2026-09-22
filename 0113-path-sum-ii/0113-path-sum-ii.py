class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, path, current_sum):
            if node is None:
                return

            # Add current node
            path.append(node.val)
            current_sum += node.val

            # Check if this is a leaf and sum matches
            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    result.append(path.copy())

            # Visit left and right
            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)

            # Backtrack
            path.pop()

        dfs(root, [], 0)

        return result
        