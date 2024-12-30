# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #get size
        count = 0
        curr = head
        while (curr):
            count += 1
            curr = curr.next
        if (n == count): return head.next

        curr = head
        target = count - n
        count = 1
        while (count != target):
            count += 1
            curr = curr.next
        curr.next = curr.next.next
        return head
