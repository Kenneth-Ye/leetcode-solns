class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                current.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                current.next = ListNode(curr2.val)  
                curr2 = curr2.next
            current = current.next

        while curr1:
            current.next = ListNode(curr1.val)  
            curr1 = curr1.next
            current = current.next

        while curr2:
            current.next = ListNode(curr2.val)
            curr2 = curr2.next
            current = current.next
        return dummy.next
    
  