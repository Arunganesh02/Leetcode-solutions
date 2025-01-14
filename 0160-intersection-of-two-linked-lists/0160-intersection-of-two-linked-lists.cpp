/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode * one = headA;
        ListNode * two = headB;
        while ( one != two ){
            if(!one) one = headB;
            else one = one->next;
            if(!two) two = headA;
            else two = two->next;
        }
        return one;
    }
};