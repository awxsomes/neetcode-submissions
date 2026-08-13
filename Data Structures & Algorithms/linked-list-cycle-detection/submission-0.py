# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle, hare = head, head

        while hare != None and hare.next != None:
            
            hare= hare.next.next
            turtle=turtle.next
            if turtle == hare:
                return True
        return False