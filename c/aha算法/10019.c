#include <stdio.h>
#include <stdlib.h>

//#define DEBUG 1

int a[100001];
int n;
int sum = 0;

void swap(int x, int y) {
    int t = a[x];
    a[x] = a[y];
    a[y] = t;
}
// 向下调整函数
void sift_down(int i) {

    int t, flag = 0;
    while (2*i <=n && flag ==0) {
        // 判断它和左儿子的关系, 并用t记录较小结点编号
        if (a[i] > a[i*2]) {
            t = i*2;
        }
        else {
            t = i;
        }

        // 如果有右儿子，再对右儿子进行比较
        if (i*2+1 <= n) {
            if (a[t] > a[i*2+1]) {
                t = i*2+1;
            }
        }

        // 如果发现最小的结点编号不是自己，说明结点中有比父结点更小的
        if (t != i) {
            swap(t, i);
            i = t;
        }
        else {
            flag = 1;
        }
    }
}

void sift_up(int i) {
    int flag = 0;
    if (i == 1) return;
    while(i != 1 && flag == 0) {
        if (a[i] < a[i/2]) {
            swap(i, i/2);
        }
        else {
            flag = 1;
        }
        i = i/2;
    }
}

void heap_sort(){
    while (n > 1) {
        swap(1, n);
        n--;
        sift_down(1);
    }
}

// 建立堆的函数
void create() {
    int i;
    for (i = n/2;i >=1; i--) {
        sift_down(i);
    }
}

int delete_max(){
    int t;
    t = a[1];
    a[1] = a[n];
    n--;
    sift_down(1); //向下调整
    return t;
}

int delete_top(){
    int t;
    t = a[1];
    a[1] = a[n];
    n--;
    sift_down(1);
    return t;
}

int main(){

    int min1, min2;
    int sum, newNum;
    int i, num;
    // 种类数
    scanf("%d", &n);

    //每个种类的果子数目
    for (i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }
    num = n;

    // 建堆
    create();
    /*
    printf("---建堆---\n");
    for (i=1;i<=num;i++) {
        printf("%d ", a[i]);
    }
    printf("------\n");
    */
    sum = 0;
    newNum = 0;
    while(n > 0) 
    { 
        min1 = delete_top();
        
        if (n > 1) {
            min2 = delete_top();
        }
        else {
            sum += min1+a[1];
            #ifdef DEBUG
            printf("end sum=%d\n", sum);
            #endif
            break;
        }

        newNum = (min1 + min2);
        #ifdef DEBUG
        printf("nextA=%d\n", newNum);
        #endif
        n++;
        a[n] = newNum;
        sum += newNum;
        sift_up(n);

        #ifdef DEBUG
        for (i=1;i<=n;i++) {
            printf("%d ", a[i]);
        }
        printf("\n");
        #endif

    }

    printf("%d\n", sum);
    return 0;
    /*
    // 堆排序(
    heap_sort();

    for (i=1;i<=num;i++) {
        printf("%d ", a[i]);
    }

    

    printf("\n");
    return 0;
    */
}
