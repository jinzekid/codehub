/******************************************************************/
/*
 * 顺序栈基本操作（以链表方式）
 * 1.初始化链栈：init_stack
 * 2.销毁链栈：destory_stack
 * 3.清空链栈：clear_stack
 * 4.获取链栈总长度：get_stack_length
 * 5.判断链栈是否为空：stack_empty
 * 6.获取链栈顶部元素：get_top_elem
 * 7.进栈：push
 * 8.出栈：pop
 * 9.链栈打印：stack_traverse
 *
 */
/******************************************************************/

#define STACK_INIT_SIZE 10
#define STACK_INCREMENT_SIZE 5

//typedef int SElemType;

// 这里使用链表形式，也可以使用数组
typedef struct SeqStack {
    SElemType *top;
    SElemType *base;
    int length;
    int stackSize;
}SeqStack;

int init_stack(struct SeqStack *s) {
    SElemType *t_base = (SElemType *)malloc(STACK_INIT_SIZE*sizeof(SElemType));
    if (t_base == NULL){
        return ERROR;
    }

    s->top = t_base;
    s->base = t_base;
    s->stackSize = STACK_INIT_SIZE;
    s->length = 0;

    return OK;
}

status destory_stack(struct SeqStack *s) {
    free(s->base);
    s->base = NULL;
    s->top = NULL;
    s->stackSize = 0;
    s->length = 0;
    
    return OK;
}

status clear_stack(struct SeqStack *s) {
    s->top = s->base;
    s->length = 0;
    return OK;
}

int get_stack_length(struct SeqStack *s) {
    return s->length;
}

status stack_empty(struct SeqStack *s) {
    if (s->length == 0) {
        return TRUE;
    }
    return FALSE;
}

status get_top_elem(struct SeqStack *s, SElemType *e) {
    if (stack_empty(s)) {
        printf("栈已空\n");
        return ERROR;
    }

    *e = *(s->top-1);
    return OK;
}

status push(struct SeqStack *s, SElemType e) {
    if (s->length >= s->stackSize) {
        s->base = (SElemType *)realloc(s->base, (s->stackSize + STACK_INCREMENT_SIZE) * sizeof(SElemType));
        if (s->base == NULL)
            return ERROR;
        
        s->top = s->base+s->stackSize;
        s->stackSize += STACK_INIT_SIZE;
    }

    *s->top = e;
    s->top++;
    s->length++;
    return OK;
}

status pop(struct SeqStack *s, SElemType *e) {
    if (s->length == 0) {
        printf("栈已空\n");
        return ERROR;
    }
    
    *e = *(--s->top);
    s->length--;
    return OK;
}

void stack_traverse(struct SeqStack s, void(*visit)(SElemType)) {
    struct SeqStack tmpStack;
    tmpStack = s;

    while (tmpStack.top > tmpStack.base) {
        visit(*tmpStack.base++);
    }

    printf("\n");

} 





