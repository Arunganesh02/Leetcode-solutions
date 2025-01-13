/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* l = head;
        ListNode* r = head;
        while ((r != NULL) &&(r->next!= NULL)){
            l = l->next;
            r = r->next->next;
        }
        ListNode* dummy = l;
        ListNode * prev = NULL;
        ListNode * temp;
        while (dummy){
            temp = dummy->next;
            dummy->next = prev;
            prev = dummy;
            dummy = temp;
        }
        l = prev;

        while(l){
            if (head->val != l->val){
                return false;
            }
            l = l->next;
            head = head->next;
        }
        return true;
    }
};