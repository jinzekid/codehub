#include "c1.h"
typedef int SElemType;
#include "bo3-5.c"

void print(SElemType e) {
    printf("%d", e);
}

int main() {

    int j;
    sLinkStack linkStack;
    init_stack(&linkStack);

    for (j = 1; j <= 12; j++) {
        push(&linkStack, j);
    }

    printf("栈中元素从栈底到栈顶依次为：\n");
    stack_traverse(linkStack, print);

    return 0;
}
