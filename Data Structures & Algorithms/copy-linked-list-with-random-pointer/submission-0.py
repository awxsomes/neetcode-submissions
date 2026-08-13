"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ductt = {}
        curr = head
        while curr:
            ductt[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                ductt[curr].next = ductt[curr.next]
            if curr.random:
                ductt[curr].random = ductt[curr.random]
            curr = curr.next
        return ductt[head]