#include <stdio.h>

#define MAX 100000

struct Queue {
    int a[MAX];
    int front;
    int rear;
};

int is_full(struct Queue *que) {
    if (que->front-que->rear >= MAX) {
        return 1;
    }

    return 0;
}

int is_empty(struct Queue *que) {
    if (que->rear == que->front) {
        return 1;
    }
    return 0;
}

void enqueue(struct Queue *que,  int e) {
    
    if (is_full(que)) {
        return;
    }

    que->a[que->front] = e;
    que->front++;
}

void dequeue(struct Queue *que) {
    if (is_empty(que)) {
        return;
    }

    que->a[que->rear] = 
    que->rear++;
}

void print_queue(struct Queue *que) {
    int tmpFront = que->front;
    int tmpRear = que->rear;

    while (tmpRear < tmpFront) {
        printf("%d ", que->a[tmpRear]);
        tmpRear++;
    }
    printf("\n");
}

int main() {

    struct Queue que;
    int n, i, t;
    char c;
    scanf("%d", &n);

    que.front = 0;
    que.rear = 0;

    for (i = 1; i <= n; i++) {
        scanf(" %c", &c);

        if (c == 'I') {
            scanf("%d", &t);
            enqueue(&que, t);
        }
        else if (c == 'O') {
            dequeue(&que);
        }
    }

    print_queue(&que);

    return 0;
}
