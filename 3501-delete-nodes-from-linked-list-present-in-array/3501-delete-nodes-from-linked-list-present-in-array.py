# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        se = set(nums)
        while head:
            if head.val in se:
                head = head.next
            else:
                break
        dum = head
        while head:
            if head.val in se:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return dum
