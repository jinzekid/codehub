#include "c1.h"
typedef int SElemType;
#include "c3-1.h"
#include "bo3-1.c"

void print(SElemType e) {
    printf("%d ", e);
}

int main() {

    int j;
    struct SqStack s;
    SElemType e;
    init_stack(&s);

    for (j = 1; j <= 12; j++) {
        push(&s, j);
    }

    printf("栈中元素依次为：");
    stack_traverse(s, print);

    pop(&s, &e);
    printf("弹出的栈顶元素e=%d\n", e);
    get_top(&s, &e);
    printf("栈顶元素e=%d 栈长度为：%d\n", e, stack_length(&s));
    destory_stack(&s);
    printf("销毁栈后，s.top=%u, s.base=%u, s.stackSize=%d\n", s.top, s.base, s.stackSize);

    return 0;
}
