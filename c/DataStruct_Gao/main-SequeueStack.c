#include "commonHeader.h"
#include "SequenceStack.c"

void print(SElemType e) {
    printf("%d", e);
}

int main() {

    int n, t;
    int j;
    SElemType e;
    struct SeqStack seqStack;
    init_stack(&seqStack);

    printf("请输入个数：");
    scanf("%d",&n);

    for (j = 1; j <= n; j++) {
        scanf("%d", &t);
        push(&seqStack, t);
    }

    printf("栈中元素从栈底到栈顶依次为：\n");
    stack_traverse(seqStack, print);

    pop(&seqStack, &e);
    printf("弹出的栈顶元素为：%d\n", e);

    get_top_elem(&seqStack, &e);
    printf("当前栈顶元素为：%d, 栈的长度为：%d\n", e, get_stack_length(&seqStack));

    clear_stack(&seqStack);
    printf("当前栈长度为：%d\n", get_stack_length(&seqStack));

    destory_stack(&seqStack);

    return 0;
}
