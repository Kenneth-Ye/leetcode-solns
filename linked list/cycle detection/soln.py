# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next if slow else None
        while slow and fast:
            if (slow == fast):
                return True
            else:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast=fast.next
        return False
