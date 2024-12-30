# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # head.next = dummy, dummy.next = temp
        # 0 -> 6 -> 1 -> 2 -> 3 -> 4 -> 5
        # 0 -> 6 -> 1 -> 5 -> 2 -> 3 -> 4
        # 0 -> 6 -> 1 -> 5 -> 2 -> 4 -> 3
        fast = head.next
        slow = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        currSec = slow.next
        prev = None
        slow.next = None
        while(currSec):
            temp = currSec.next
            currSec.next = prev
            prev = currSec
            currSec = temp
        # second half len <= first half
        second = prev
        while (second):
            temp1 = head.next
            temp2 = second.next
            head.next = second
            second.next = temp1
            head = temp1
            second = temp2
