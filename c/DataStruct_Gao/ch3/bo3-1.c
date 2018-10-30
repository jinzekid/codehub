int init_stack(struct SqStack *s) {
    SElemType *t_base = (SElemType *)malloc(STACK_INIT_SIZE*sizeof(SElemType));
    if (t_base == NULL){
        return FALSE;
    }

    s->base = t_base;
    s->top = t_base;
    s->stackSize = STACK_INIT_SIZE;

    return OK;
}

int destory_stack(struct SqStack *s) {
    free(s->base);
    s->base = NULL;
    s->top = NULL;
    s->stackSize = 0;
}

void clear_stack(struct SqStack *s) {
    s->top = s->base;
}

status stack_empty(struct SqStack *s) {
    if (s->top == s->base) {
        return TRUE;
    }
    
    return FALSE;
}

int stack_length(struct SqStack *s) {
    return s->top - s->base;
}

status get_top(struct SqStack *s, SElemType *e) {
    if (s->top > s->base) {
        *e = *(s->top-1);
        return OK;
    }

    return ERROR;
}

status push(struct SqStack *s, SElemType e) {
    if (s->top-s->base >= s->stackSize) {
        s->base = (SElemType *)realloc(s->base, (s->stackSize + STACK_INIT_SIZE) * sizeof(SElemType));

        if (s->base == NULL)
            return ERROR;
        
        s->top = s->base+s->stackSize;
        s->stackSize += STACK_INIT_SIZE;
    }

    *s->top = e;
    s->top++;
    return OK;
}

status pop(struct SqStack *s, SElemType *e) {
    if (s->top == s->base) {
        return -1;
    }
    
    *e = *(--s->top);
    return OK;
}

void stack_traverse(struct SqStack s, void(*visit)(SElemType)) {
    struct SqStack tmpStack;
    tmpStack = s;

    while (tmpStack.top > tmpStack.base) {
        visit(*tmpStack.base++);
    }

    printf("\n");

} 





