# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # Start with the leftmost node of each level
        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                # Connect left child -> right child
                current.left.next = current.right

                # Connect right child -> next node's left child
                if current.next:
                    current.right.next = current.next.left

                current = current.next

            # Move to the next level
            leftmost = leftmost.left

        return root
        