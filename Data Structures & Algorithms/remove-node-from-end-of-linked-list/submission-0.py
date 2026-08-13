# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        theone = start
        curr = head
        for i in range(n):
            curr =  curr.next
        
        while curr != None:
            theone= theone.next
            curr = curr.next
        theone.next = theone.next.next
        return start.next