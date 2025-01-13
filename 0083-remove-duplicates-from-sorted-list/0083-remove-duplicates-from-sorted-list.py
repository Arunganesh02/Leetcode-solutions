# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        l = head
        r = head.next
        while (r):
            if l.val == r.val:
                r = r.next
            else:
                l.next = r
                l = l.next
                r = r.next
        l.next = None
        return head