# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None:
                return head
            current = head
            previous = None
            while current != None:
                nextNode = current.next
                current.next = previous
                
                previous = current
                current = nextNode
                
            return previous

        dummy = ListNode(0)
        dummy.next = head
        curr = head
        tail = dummy

        groupHead = head
        counter = 1
        while curr != None:
            nextNode = curr.next
            
            if counter % k == 0:
                curr.next = None
                reversedHead = reverseList(groupHead)
                tail.next = reversedHead
                groupHead.next = nextNode                
                tail = groupHead
                groupHead = nextNode
            
            counter += 1
            curr = nextNode
        return dummy.next