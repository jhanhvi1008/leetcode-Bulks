class Solution:
    def sortedListToBST(self, head):
        
        # Base case
        if not head:
            return None
        
        # Find the middle node
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # slow is the middle node
        root = TreeNode(slow.val)
        
        # Split the linked list into two halves
        if prev:
            prev.next = None
        
        # If there is only one node
        if slow == head:
            root.left = None
        else:
            root.left = self.sortedListToBST(head)
        
        root.right = self.sortedListToBST(slow.next)
        
        return root