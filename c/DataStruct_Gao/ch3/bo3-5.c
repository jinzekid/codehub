//链栈
typedef struct sNode {
    SElemType data;
    struct sNode* next;
}sNode;

typedef struct sLinkStack {
    struct sNode *pNode;
    struct sNode *head;
    int stackSize;
}sLinkStack;

status init_stack(sLinkStack *pLinkStack) {
    //sLinkStack *t = (sLinkStack *)malloc(sizeof(sLinkStack));
    //if (t == NULL) return ERROR;
    sLinkStack *t = pLinkStack;
    t->pNode = NULL;
    t->head  = NULL;
    t->stackSize = 0;

    printf("初始化链栈成功...\n");
}

status stack_empty(sLinkStack linkStack) {
    if (linkStack.stackSize == 0) return TRUE;
    return FALSE;
}

status get_top(sLinkStack *pLinkStack, SElemType *e) {
    
}

status pop(sLinkStack *pLinkStack) {

}

status push(sLinkStack *pLinkStack, SElemType e) {
    if (pLinkStack == NULL) return ERROR;

    struct sNode *newNode = (sNode *)malloc(sizeof(sNode));
    if (newNode == NULL) return ERROR;

    newNode->data = e;
    newNode->next = NULL;

    printf("newNode>data=%d\n", newNode->data);
    
    struct sNode *tmpNode = pLinkStack->head;
    if (tmpNode == NULL) {
        pLinkStack->head = newNode;
        pLinkStack->pNode = newNode;
    }
    else {
        while(tmpNode->next) {
            tmpNode = tmpNode->next;
        }

        tmpNode->next = newNode;
        pLinkStack->pNode = newNode;
    }
    pLinkStack->stackSize++;
    printf("stacksize:%d\n", pLinkStack->stackSize);
}

void stack_traverse(sLinkStack s, void(*visit)(SElemType)) {
    struct sNode* tmpNode = s.head;
    while (tmpNode) {
        printf("%d ", tmpNode->data);
        tmpNode = tmpNode->next;
    }
    printf("\n");
}
