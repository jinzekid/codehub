#include <stdio.h>

#define N 10
#define T 3
#define MAX_SIZE 20

typedef int InfoType;
typedef int KeyType;

struct RedType {
    KeyType key;
    InfoType otherInfo;
};

struct SqList {
    struct RedType r[MAX_SIZE+1];
    int length;
};

void print_lk(struct SqList l) {
    int i;
    for (i = 1; i <= l.length; i++) {
        printf("%d ", l.r[i].key);
    }
    printf("\n");
}

void printl(struct SqList l) {
    int i;
    for (i = 1; i <= l.length; i++) {
        printf("(%d, %d)", l.r[i].key, l.r[i].otherInfo);
    }
    printf("\n");
}

// 对顺序表作一趟希尔插入排序
// 1.前后记录位置的增量为dk，而不是1
// 2.r0只是暂存单元，当j 《= 0 时，插入位置已经找到
void shell_insert(struct SqList *L, int dk) {
    int i,j;
    for (i = dk+1; i <= L->length; i++) {
        if (L->r[i].key > L->r[i-dk].key) {
            L->r[0] = L->r[i];
            for (j = i-dk; j>0 && L->r[0].key > L->r[j].key; j-=dk){
                L->r[j+dk] = L->r[j];
            }
            L->r[j+dk] = L->r[0];
        }
    }
}

void shell_sort(struct SqList *L, int dlta[], int t){
    int k;
    struct SqList tmp = *L;
    for (k = 0; k < t; k++) {
        shell_insert(L, dlta[k]); // 一趟增量为dltal【k】的插入排序
        printf("after %d sorted:", k+1);
        print_lk(tmp);
    }
}


int main(){

    int i;

    struct RedType d[N] = {{49,1}, {38,2}, {65,3}, {97,4}, {76,5},{13,6},{27,7},{49,8}, {55,9},{4,10}};
    struct SqList l;
    int dt[T] = {5,3,1};
    for(i = 0; i<N; i++) 
        l.r[i+1] = d[i];

    l.length = N;
    printf("before sort:\n");
    print_lk(l);
    shell_sort(&l, dt, T);
    printf("after sort:\n");
    printl(l);



    return 0;
}


