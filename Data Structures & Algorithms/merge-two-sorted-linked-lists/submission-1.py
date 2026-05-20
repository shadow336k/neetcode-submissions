# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if list1:
                return list1
            elif list2:
                return list2
            else:
                return None
        fooby = ListNode(0)
        aptr = list1
        bptr = list2
        cptr = fooby
        while aptr and bptr:
            if (aptr.val <= bptr.val):
                cptr.next = aptr
                aptr = aptr.next
            else:
                cptr.next = bptr
                bptr = bptr.next
            cptr = cptr.next
        cptr.next = aptr if aptr else bptr
        return fooby.next
