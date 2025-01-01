/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
// O(n) time O(n) space
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;
        Node *curr = head;
        std::map<Node *, Node *> built;
        Node *dummy = new Node(0);
        Node *it = dummy;
        while (curr) {
            if (!built.count(curr)) {
                it->next = new Node(curr->val);
                built[curr] = it->next;
            } else {
                it->next = built[curr];
            }
            it = it->next;
            if (curr->random && !built.count(curr->random)) {
                it->random = new Node(curr->random->val);
                built[curr->random] = it->random;
            } else if (curr->random) {
                it->random = built[curr->random];
            } else {
                it->random = nullptr;
            }
            curr = curr->next;
        }
        it->next = nullptr;
        Node *res = dummy->next;
        delete dummy;
        return res;
    }
};