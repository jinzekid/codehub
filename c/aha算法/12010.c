#include <stdio.h>

int main() {

    int t;
    int n;
    int i;
    int a[200001];
    int que[100001];
    int top;
    int head;
    int tail;

    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }

    head = 1;
    tail = n+1;
    top = 1;

    while(head < tail) {
        que[top] = a[head];
        top++;
        head++;

        a[tail] = a[head];
        tail++;

        head++;
    }

    for (i = 1; i < top; i++) {
        printf("%d ", que[i]);
    }
    printf("\n");

    return 0;
}
