# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head, x):
        
        # Two dummy lists
        smaller = ListNode(0)
        greater = ListNode(0)
        
        small = smaller
        large = greater
        
        current = head
        
        while current:
            
            if current.val < x:
                small.next = current
                small = small.next
            else:
                large.next = current
                large = large.next
            
            current = current.next
        
        # End greater list
        large.next = None
        
        # Connect two lists
        small.next = greater.next
        
        return smaller.next
        