# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        infinity = float('inf')
        while head.next:
            head.val = infinity
            head = head.next
            if head.val >= infinity:
                return True
        return False