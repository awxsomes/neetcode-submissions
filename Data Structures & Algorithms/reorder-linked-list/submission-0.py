# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        turtle, hare = head, head

        while hare != None and hare.next != None:
            
            hare= hare.next.next
            turtle=turtle.next
        midpoint = turtle


        current = midpoint.next
        midpoint.next = None


        previous = None
        while current != None:
            nextNode = current.next
            current.next = previous
            
            previous = current
            current = nextNode
            
        reverse = previous



        while reverse != None:
            nextHead = head.next
            nextReverse = reverse.next

            head.next = reverse
            reverse.next=nextHead

            head = nextHead
            reverse = nextReverse