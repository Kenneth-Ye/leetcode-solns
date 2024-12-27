# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3
        #           p.   c.   r
        # 0 <- 1 <- 2 -> 3
        # 3 -> 2 -> 1 -> 0
        curr = head
        prev = None
        while(curr):
            right = curr.next
            curr.next = prev
            prev = curr
            curr = right
        return prev
