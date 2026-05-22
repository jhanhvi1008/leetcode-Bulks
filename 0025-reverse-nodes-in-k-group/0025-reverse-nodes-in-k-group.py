# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # Find the kth node
            kth = prev_group

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_group = kth.next

            # Reverse the group
            prev = next_group
            curr = prev_group.next

            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect reversed group
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
        