/*
堆排序，去重复
*/
#include <stdio.h>

int h[101];
int n;
int stack[101];
int top = 1;

void swap(int a, int b) {

    int t;
    t = h[a];
    h[a] = h[b];
    h[b] = t;
}

// 向下调整
void sift_down(int i) {

    int t;
    int flag = 0;


    while (i <= n/2 && flag == 0) {

        // 判断左边
        if (h[i] > h[i*2]) {
            t = i*2;
        }
        else {
            t = i;
        }

        // 判断右边
        if ((i*2+1) <= n) {
            if (h[t] > h[i*2+1]) {
                t = i*2+1;
            }
        }

        if (t != i) {
            swap(t , i);
        } 
        else {
            flag = 1;
        }
        i = t;
    }

}

// 向上调整
void sift_up(int n) {

    int i;
    int flag = 0;

    if (i == 1) { return; }

    i = n;
    while (i != 1 && flag == 0){

        if (h[i] < h[i/2]) {
            swap(i, i/2);
        }
        else {
            flag = 1;
        }

        i = i/2;
    }
}

// 堆排序
void heap_sort(){
    
    int t, i;
    while (n > 0) {
        t = h[n];
        h[n] = h[1];
        h[1] = t;


        if (stack[top-1] != h[n]) {
            stack[top] = h[n];
            top++;
        }
        n--;

        sift_down(1);
    }
}


int main(){

    int m, i;
    scanf("%d", &m);

    n = 0;
    for (i = 1; i <= m; i++) {
        scanf("%d", &h[i]);
    }

    n = m;
    for (i = n/2; i >= 1; i--) {
        sift_down(i);
    }

    n = m;
    heap_sort();
    printf("%d\n", top-1);
    for (i = 1; i < top; i++) {
        printf("%d ", stack[i]);
    }
    printf("\n");



    return 0;
}
