# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        anotherone = 0
        while l1 != None or l2 != None or anotherone == 1:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            value = val1+val2+anotherone

            if value >= 10:
                value %= 10
                anotherone = 1
            else:
                anotherone = 0
            curr.next=ListNode(value)
            l1=l1.next if l1 != None else None
            l2=l2.next if l2 != None else None
            curr = curr.next
        return dummy.next