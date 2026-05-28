# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        
        def isMirror(t1, t2):
            # Both nodes are null
            if not t1 and not t2:
                return True
            
            # One node is null
            if not t1 or not t2:
                return False
            
            # Check values and mirror structure
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))
        
        return isMirror(root, root)
        