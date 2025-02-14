# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dum = head.next
        # su = 0
        # newhead = None
        # while( dum.next != None):
        #     if dum.val != 0:
        #         su += dum.val
        #     else:
        #         if not newhead:
        #             newhead = ListNode(su)
        #             newdum = newhead
        #         else:
        #             newhead.next = ListNode(su)
        #             newhead = newhead.next
        #         su = 0
        #     dum = dum.next
        
        # if not newhead:
        #     newhead = ListNode(su)
        #     newdum = newhead
        # else:
        #     newhead.next = ListNode(su)
        #     newhead = newhead.next

        # return newdum
        dum  = head
        ptri = head
        head = head.next
        while (head.next):
            if head.val != 0:
                ptri.val += head.val
            else:
                ptri.next = head
                ptri = head
            head = head.next
        ptri.next = None
        return dum