#include <stdio.h>
#include <stdlib.h>

 // Definition for singly-linked list.
  struct ListNode {
      int val;
      struct ListNode *next;
  };
 

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* tmp1 = l1;
    struct ListNode* tmp2 = l2;
    struct ListNode* ret = NULL;
    struct ListNode* retTmp = NULL;
    struct ListNode* tmpNode = NULL;

    tmp1 = l1;
    tmp2 = l2;
    int s,t,jw = 0;

    while(tmp1 != NULL && tmp2 != NULL) {
        s = tmp1->val + tmp2->val + jw;
        t = s%10;
        jw = s/10;

        tmpNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmpNode->next = NULL;

        if (ret == NULL) {
            tmpNode->val = t;
            ret = tmpNode;
            retTmp = ret;
        }
        else {
            tmpNode->val = t;
            retTmp->next = tmpNode;

            retTmp = tmpNode;
        }

        tmp1 = tmp1->next;
        tmp2 = tmp2->next;
    }

    if (tmp1 != NULL) {
    while(tmp1 != NULL) {
        s = tmp1->val + jw;
        t = s%10;
        jw = s/10;

        tmpNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmpNode->next = NULL;

        tmpNode->val = t;
        retTmp->next = tmpNode;
        retTmp = tmpNode;
    }
    }

    if (tmp2 != NULL) {
    while(tmp2 != NULL) {
        s = tmp2->val + jw;
        t = s%10;
        jw = s/10;

        tmpNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmpNode->next = NULL;

        tmpNode->val = t;
        retTmp->next = tmpNode;
        retTmp = tmpNode;
    }
    }

    if (jw != 0) {
        tmpNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmpNode->next = NULL;

        tmpNode->val = jw;
        retTmp->next = tmpNode;
        retTmp = tmpNode;
    }

    return ret;

}

int main(){
    struct ListNode* ret;
    struct ListNode *node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = 0;
    node->next= NULL;

    struct ListNode *node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    node2->val = 1;

    struct ListNode *node3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    node3->val = 8;
    node3->next = NULL;

    node2->next = node3;

    ret = addTwoNumbers(node, node2);
    while(ret) {
        printf("%d ", ret->val);
        ret = ret->next;
    }

    return 0;
}
