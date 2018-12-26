#include <stdio.h>
#include <stdlib.h>

int a[100001];
int n;
int sum = 0;
//堆排序
void sift_down(int a[], int n) {
    
    int t = 1;
    int t2 = t;

    while (t <= n/2) {
        if (a[t] > a[2*t]) {
            t2 = 2*t;
        }

        if (2*t+1 <= n) {
            if (a[t] > a[2*t+1]) {
                t2 = 2*t + 1;
            }
        }

        if (t != t2) {
            t = t2;
            swap(a , a[t], a[t2]);
        }
    }

}

void sift_up(int a[], int n) {

}

void heap_sort(){

}

int main(){

    int i;
    // 种类数
    scanf("%d", &n);

    //每个种类的果子数目
    for (i = 1; i <= 100000; i++) {
        scanf("%d", &a[i]);
    }





    return 0;
}
