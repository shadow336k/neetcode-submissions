# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow_ptr = head
        fast_ptr = head
        #stop = 0
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            #print(f"slow = {slow_ptr.val}")
            fast_ptr = fast_ptr.next.next
            #print(f"fast = {fast_ptr.val}")
            if slow_ptr == fast_ptr:
                return True
         #   stop = stop + 1
         #   if stop > 10:
         #       break
        return False