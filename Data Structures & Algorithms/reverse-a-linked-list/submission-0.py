# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head == []:
            return None
        prev = None
        cur = head
        while cur.next:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur.next = prev
#        while head.next:
 #           temp = head.next
 #           head.next = head
 #           head = temp
        return cur

