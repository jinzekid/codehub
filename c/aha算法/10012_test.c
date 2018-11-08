#include <stdio.h>
#include <stdlib.h>

typedef struct Stack{
    int data[5];
    int head;
    int tail;
    int size;
}Stack;

void clear_stack(Stack *pStack) {
    pStack->head = 0;
    pStack->tail = 0;
    pStack->size = 0;
}

void print_stack(Stack *pStack) {
    int i;
    for (i = 0; i < pStack->size; i++) {
        printf("%d ", pStack->data[i]);
    }
    printf("\n");
}

void push_stack(Stack *pStack, int num, int *sum) {

    int yu, cnt = 0;
    int tmp = num;
    if (pStack == NULL)
        return;

    clear_stack(pStack);

    while (tmp) {

        yu = tmp % 10;
        pStack->data[pStack->tail] = yu;
        pStack->tail++;
        pStack->size++;

        if (yu == 2) {
            cnt += 1;
        }

        tmp = tmp / 10;
    }

    *sum += cnt;
}

int main(){

    int i;
    int n, m;
    int sum;
    Stack *pStack = NULL;
    pStack = (Stack *)malloc(sizeof(Stack));

    scanf("%d %d", &n, &m);
    
    sum = 0;
    for (i = n; i <= m; i++) {
        push_stack(pStack, i, &sum);
    }

    printf("%d\n", sum);
    //print_stack(pStack);

    return 0;
}
