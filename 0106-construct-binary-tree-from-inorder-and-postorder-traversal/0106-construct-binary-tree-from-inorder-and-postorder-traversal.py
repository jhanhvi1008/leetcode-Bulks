# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
       def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # Map value -> index in inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        self.post_idx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            # Root is the current last element in postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)

            # Find root position in inorder
            idx = inorder_map[root_val]

            # Build right subtree first
            root.right = build(idx + 1, right)
            root.left = build(left, idx - 1)

            return root

        return build(0, len(inorder) - 1);
        