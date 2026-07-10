# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
           return False
        visited = defaultdict(int)
        index = 0
        while head.next:
            idt = id(head)
            print(f"visted node {idt}")
            print(f"if {visited[idt]} less than {index}...")
            if visited[idt] and visited[idt] < index:
                 return True
            visited[id(head)] = index
            index = index + 1
            head = head.next
            
        return False
        