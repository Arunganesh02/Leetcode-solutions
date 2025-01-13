# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = head
        r = head
        while (r and r.next):
            l = l.next
            r = r.next.next
        prev = None
        while l:
            temp = l.next
            l.next = prev
            prev = l
            l = temp
        l = prev
        while l:
            if head.val != l.val:
                return False
            l = l.next
            head = head.next
        return True
        