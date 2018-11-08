/******************************************************************/
/*
 * 链栈基本操作（链表方式）
 * 1.创建链表：create_stack
 * 2.初始化链栈：init_stack
 * 3.销毁链栈：destory_stack
 * 4.清空链栈：clear_stack
 * 5.获取链栈总长度：get_stack_length
 * 6.判断链栈是否为空：stack_empty
 * 7.获取链栈顶部元素：get_top_elem
 * 8.进栈：push
 * 9.出栈：pop
 * 10.链栈打印：stack_traverse
 *
 */
/******************************************************************/

//链栈
typedef int SElemType;

typedef struct sNode {
    SElemType data;
    struct sNode* next;
}sNode;

typedef struct sLinkStack {
    struct sNode *head;
    int stackSize;
}sLinkStack;


status create_stack(sLinkStack **pLinkStack) {
    sLinkStack *p = (sLinkStack *)malloc(sizeof(sLinkStack));
    if (p == NULL) {
	return ERROR;
    }

    *pLinkStack = p;
    return OK;
}


status init_stack(sLinkStack *pLinkStack) {
    sLinkStack *t = pLinkStack;
    t->head  = NULL;
    t->stackSize = 0;

    return OK;
}

status clear_stack(sLinkStack *pLinkStack) {

    if (stack_empty()) {
        return OK;
    }

    while (pLinkStack->stackSize > 0) {

        sNode *del_pSNode = pLinkStack->head;
        pLinkStack->head = del_pSNode->next;
        free(del_pSNode); 
        pLinkStack->stackSize--;
    }

    printf("栈已经清空\n");
    return OK;
}

status destory_stack(sLinkStack **pLinkStack) {
    sLinkStack *del_linkStack = NULL;
    del_linkStack = *pLinkStack;

    clear_stack(del_linkStack);
    del_linkStack->stackSize = 0;
    del_linkStack->head = NULL;

    free(del_linkStack);
    *pLinkStack = NULL;

    printf("栈已经销毁\n");
    return OK;
}

status stack_empty(sLinkStack *pLinkStack) {
    if (pLinkStack->stackSize == 0) return TRUE;
    return FALSE;
}

int get_stack_length(sLinkStack *pLinkStack) {
    return pLinkStack->stackSize;
}

status get_top(sLinkStack *pLinkStack, SElemType *e) {
    if (stack_empty(pLinkStack)) {
        printf("链栈为空\n");
        return ERROR;
    }

    sNode *pSNode = pLinkStack->head;
    *e = pSNode->data;
    return OK;
}

status pop(sLinkStack *pLinkStack, SElemType *e) {

    if (stack_empty(pLinkStack)) {
        printf("链栈为空\n");
        return ERROR;
    }

    sNode *pSNode = pLinkStack->head;
    pLinkStack->head = pLinkStack->head->next;
    pLinkStack->stackSize--;

    *e = pSNode->data;
    free(pSNode);
    printf("出栈成功\n");
}

status push(sLinkStack *pLinkStack, SElemType e) {
    if (pLinkStack == NULL) return ERROR;

    struct sNode *newNode = (sNode *)malloc(sizeof(sNode));
    if (newNode == NULL) return ERROR;

    newNode->data = e;
    newNode->next = NULL;

    struct sNode *tmpNode = pLinkStack->head;
    if (tmpNode == NULL) {
        pLinkStack->head = newNode;
    }
    else {
        /*
        while(tmpNode->next) {
            tmpNode = tmpNode->next;
        }

        tmpNode->next = newNode;
        pLinkStack->pNode = newNode;
        */
        newNode->next = pLinkStack->head;
        pLinkStack->head = newNode;
    }
    pLinkStack->stackSize++;

    return OK;
}

void stack_traverse(sLinkStack s, void(*visit)(SElemType)) {
    struct sNode* tmpNode = s.head;
    while (tmpNode) {
        printf("%d ", tmpNode->data);
        tmpNode = tmpNode->next;
    }
    printf("\n");
    printf("链栈中的数据数量为:%d\n", s.stackSize);
}
