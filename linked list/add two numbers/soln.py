# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        head = curr
        carry = 0
        while l1 and l2:
            digit_sum = (l1.val + l2.val + carry) % 10
            curr.next = ListNode(digit_sum)
            carry = (l1.val + l2.val + carry - digit_sum) // 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
            
        valNode = l1
        if l2: valNode = l2
        
        while valNode:
            digit_sum = (valNode.val + carry) % 10
            curr.next = ListNode(digit_sum)
            carry = (valNode.val + carry - digit_sum) // 10
            curr = curr.next
            valNode = valNode.next
        
        if carry:
            curr.next = ListNode(carry)

        return head.next
