#include "commonHeader.h"
#include "LinkStack.c"

void print(SElemType e) {
    printf("%d", e);
}

void print_menu() {
    printf("\n*******************************\n");
    printf("1.创建链栈");
    printf("2.初始化链栈");
    printf("");
    printf("");
    printf("\n*******************************\n");
}

int main() {

    int n, t;
    int j;
    SElemType e;
    sLinkStack *pLinkStack = NULL;
    create_stack(&pLinkStack);
    init_stack(pLinkStack);

    printf("请输入个数：");
    scanf("%d",&n);

    for (j = 1; j <= n; j++) {
        scanf("%d", &t);
        push(pLinkStack, t);
    }

    printf("栈中元素从栈底到栈顶依次为：\n");
    stack_traverse(*pLinkStack, print);

    pop(pLinkStack, &e);
    printf("弹出的栈顶元素为：%d\n", e);

    get_top(pLinkStack, &e);
    printf("当前栈顶元素为：%d, 栈的长度为：%d\n", e, get_stack_length(pLinkStack));

    clear_stack(pLinkStack);
    printf("当前栈长度为：%d\n", get_stack_length(pLinkStack));

    destory_stack(&pLinkStack);
    printf("pLinkStack=%d\n", pLinkStack);

    return 0;
}
