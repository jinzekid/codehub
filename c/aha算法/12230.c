#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct sQue {
    int front;
    int rear;
    int a[11];
    int length;
};

char a[100][100];


void init_queue(struct sQue *q) {
    q->front = 0;
    q->rear = 0;
    q->length = 0;
}

void clear_queue(struct sQue *q) {
    q->front = 0;
    q->rear = 0;
}

void push(struct sQue *q, int e) {
    q->a[q->rear] = e;
    q->rear++;
    q->length++;
}

void pop(struct sQue *q, int *e) {
    if (q->front < q->rear) {
        *e = q->a[q->front];
        q->front++;
        q->length--;
    }
}

void print_que(struct sQue q) {
    struct sQue tmp_q;
    int i = 0;
    tmp_q = q;
    while (tmp_q.front < tmp_q.rear) {
        printf("%d", tmp_q.a[tmp_q.front]);
        tmp_q.front++;
        i++;

        if (i % 2 == 0) printf(" "); 
    }
}


int main() {

    struct sQue q;
    struct sQue q2;
    int i, j, k, w;
    int n, e;
    int len;
    scanf("%d", &n);

    init_queue(&q);
    init_queue(&q2);

    for (i = 0; i < n; i++) {
        for (j = 0; j < 9; j++)
            scanf(" %c", &a[i][j]);
    }

    for (i = 0; i < n; i++) {
        len = strlen(a[i]);

        for (j = 0; j < len; j++) {
            if (a[i][j] != ' ')
                push(&q, a[i][j]-'0');
        }
	 
	k = 0;
	while(q.length > 0) {
	    pop(&q, &e);
	    k++;
   	    if (k % 2 == 0) push(&q2, e);
	}

        // output
        print_que(q2);
        printf("\n");

        clear_queue(&q);
        clear_queue(&q2);
    }

    return 0;
}
