# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        while head:
            
            # Check if current node is duplicate
            if head.next and head.val == head.next.val:
                
                # Skip all duplicate nodes
                while head.next and head.val == head.next.val:
                    head = head.next
                
                prev.next = head.next
            
            else:
                prev = prev.next
            
            head = head.next
        
        return dummy.next
        