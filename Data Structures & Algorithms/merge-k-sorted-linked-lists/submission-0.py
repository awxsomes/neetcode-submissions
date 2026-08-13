# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if list1 == None:
                return list2
            if list2 == None:
                return list1
            newlist = ListNode(0)
            head=  newlist
            while list1!= None and list2 != None:


                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next

                else:
                    head.next = list2
                    list2=list2.next
                head=head.next
            
            if list1 is not None:
                head.next = list1
            elif list2 is not None:
                head.next = list2
            return newlist.next
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            newList = mergeTwoLists(list1, list2)
            lists.append(newList)
        return lists[0]