# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def add(l1,l2,l3,c):
        #     if l1 and l2:
        #         s = l1.val + l2.val
        #         if s>=10:
        #             s = s%10
        #             l3.val = (s+c)
        #             l3.next = ListNode()
        #             c = 1
        #         else:
        #             l3.val = (s+c)
        #             l3.next = ListNode()
        #             c = 0
        #         add(l1.next,l2.next,l3.next,c)
        #     elif l1:
        #         s = l1.val+c
        #         if s>=10:
        #             s = s%10
        #             l3.val = (s+c)
        #             l3.next = ListNode()
        #             c =1
        #         else:
        #             l3.val = (s+c)
        #             l3.next = ListNode()
        #             c = 0
        #         add(l1.next,None,l3.next,c)
        #     elif l2:
        #         s = l2.val+c
        #         if s>=10:
        #             s = s%10
        #             l3.val = (s+c)
        #             l3.next = ListNode()
        #             c =1
        #         else:
        #             l3.val = (s+c)
        #             l3.next = ListNode()
        #             c = 0
        #         add(None,l2.next,l3.next,c)
        #     return 
        # n = ListNode()
        # add(l1,l2,n,0)
        # return n
        dummy = cur =ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //=10
        return dummy.next

