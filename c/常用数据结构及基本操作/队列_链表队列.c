#include "commonHeader.h"

typedef int ElemType;

typedef struct Node{
    ElemType data;
    struct Node *next;
}Node;


typedef struct LinkQueue {
    Node *head;
    Node *tail;
    int size;
}LinkQueue, *pLinkQueue;






