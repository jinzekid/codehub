#include <stdio.h>
int h[101];
int n;

void swap(int x, int y) {
    int t;
    t = h[x];
    h[x] = h[y];
    h[y]  =t;
}

void sift_down(int i){
    
    int t, flag = 0;
    while (i * 2 <= n && flag == 0) {
        if (h[i] > h[i * 2]) {
            t = i * 2;
        }
        else {
            t = i;
        }

        if (i * 2 + 1 <= n) {
            if (h[t] > h[i * 2 + 1]) {
                t = i * 2 + 1;
            }
        }


        if (t != i) {
            swap(t , i);
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

    while (i != 1 && flag == 0) {
        if (h[i] < h[i/2]){
            swap(i, i/2);
        }
        else {
            flag = 1;
        }

        i = i/2;
    }
}

int delete_max(){
    int t;
    t = h[1];
    h[1] = h[n];
    
    n--;
    sift_down(1);
    return t;
}

void heap_sort(){
    while (n > 1) {
        swap(1, n);
        n--;
        sift_down(1);
    }
}

void heap_sort_desc(){
    int i = 1;
    while (i < n) {
        swap(1, n);
        sift_up(i);

    }
}

void create() {
    int i;
    for (i = n/2; i >= 1; i--) {
        sift_down(i);
    }
}

int main() {

    int i, num;
    scanf("%d", &num);

    for (i = 1; i <= num; i++) {
        scanf("%d", &h[i]);
    }
    n = num;

    create();
    for (i = 1; i <= num; i++) {
        printf("%d ", h[i]);
    }
    printf("\n");


    heap_sort();
    for (i = 1; i <= num; i++) {
        printf("%d ", h[i]);
    }
    printf("\n");
    

    /*
    n = num;
    for (i = 1; i <= num; i++) {
        printf("%d ", delete_max());
    }
    printf("\n");
    */

    return 0;
}
