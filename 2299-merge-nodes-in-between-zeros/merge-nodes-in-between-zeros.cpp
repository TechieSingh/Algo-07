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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* curr = head->next; // Skip the first zero node
        ListNode* result = new ListNode(0); // Dummy node for results
        ListNode* temp = result; // Pointer to add nodes to result
        int sum = 0;

        while (curr != NULL) {
            if (curr->val != 0) {
                sum += curr->val;
            } else {
                temp->next = new ListNode(sum);
                temp = temp->next;
                sum = 0; // Reset the sum for the next segment
            }
            curr = curr->next;
        }

        return result->next; // Skip the dummy node
    }
};
