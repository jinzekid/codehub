//顺序队列
#include "commonHeader.h"

#define TRUE    1
#define FALSE   0
#define ERROR   0
#define OK      1
#define OVERFLOW 0
#define INF     0
#define MAX     10000

typedef int Status;
typedef int Boolean;
typedef int ElemType;

// 数组形式
typedef struct linearQueue {
    ElemType    data[MAX];
    int         head;
    int         tail;
}Queue, *pQueue;


Status init_queue(Queue **q){
    Queue *pq = (Queue *)malloc(sizeof(Queue));

    if (pq == NULL) {
        return ERROR;
    }

    *q = pq;
    return OK;
}

Status is_full(pQueue q) {
    
    if ((q->tail+1) % MAX == q->head){
        return TRUE;
    }

    return FALSE;
}

Status is_empty(pQueue q) {

    if (q->head == q->tail) {
        return TRUE;
    }

    return FALSE;
}

int queue_len(pQueue q) {
    return (q->tail - q->head);
}

Status destory_queue(pQueue *q) {

    pQueue tmp = *q;
    if (tmp) {
        free(tmp);
    }

    *q = NULL;
    printf(">>:destory queue...:)\n");
    return OK;
}

Status enqueue(pQueue q, ElemType e) {

    if (is_full(q)){
        return OVERFLOW;
    }
   
    q->data[q->tail] = e;
    q->tail++;
}

Status dequeue(pQueue q, ElemType *e) {

    if (is_empty(q)){
        return INF;
    }

    *e = q->data[q->head];
    q->head++;
}


int main(int argc, const char* argv[]){

    int i, n, m;
    Queue *q = NULL;
    init_queue(&q);

    printf(">>:Please input n:");
    scanf("%d", &n);

    for (i = 0; i< n; i++) {
        scanf("%d", &m);
        enqueue(q, m);
    }

    printf("queue length: %d\n", queue_len(q));

    while(!is_empty(q)){
        ElemType e;
        dequeue(q, &e);
        printf("%d ", e);
    }
    printf("\n");

    destory_queue(&q);

    getchar();
    return 0;
}




