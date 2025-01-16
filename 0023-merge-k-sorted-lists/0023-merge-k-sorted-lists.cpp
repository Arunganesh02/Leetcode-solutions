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
        ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
            ListNode * head;
            if (!list1 && !list2){
                return list1;
            }
            // if (list1 || list2){
            //     return list1 || list2;
            // }
            if (!list1 && list2){
                return list2;
            }
            if (list1 && !list2){
                return list1;
            }
            if (list1->val < list2->val){
                head = list1;
                list1 = list1->next;
            }
            else{
                head = list2;
                list2 = list2->next;
            }
            ListNode * temp = head;
            while (list1 && list2){
                if (list1->val < list2->val){
                    head->next = list1;
                    list1 = list1->next;
                    head = head->next;
                }
                else{
                    head->next = list2;
                    list2 = list2->next;
                    head = head->next;
                }
            }
            if(!list1 && list2){
                head->next = list2;
            }
            if ( !list2 &&  list1){
                head->next = list1;
            }
            return temp;
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0){
            return nullptr;
        }
        ListNode* dummy1 = nullptr;
        for (int i = 0 ; i<lists.size();i++){
            dummy1 = mergeTwoLists(dummy1,lists[i]);
        }
        return dummy1;
    }
};


