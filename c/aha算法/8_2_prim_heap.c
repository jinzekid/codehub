#include <stdio.h>

int count = 0, sum = 0;
int inf = 999999;
int n, m;
int size;

int dis[7],book[7] = {0};
int h[7], pos[7];

void swap(int i, int j) {
    int t;

    t = h[i];
    h[i] = h[j];
    h[j] = t;
}

void sift_down(int i) {

    int flag = 0;
    int k;
    while (i <= size/2 && flag == 0)  {
        
        if (h[i] > h[i*2]) {
            k = i*2;
        }
        else {
            k = i;
        }

        if (i*2+1 <= size) {
            if (h[k] > h[i*2+1]){
                k = i*2+1;
            }
        }


        if (k != i) {
            swap(k, i);
            i = k;
        }
        else {
            flag = 1;
        }
    }
}

void sift_up(int i) {
   
    int flag = 0;
    if (i == 1) return; 

    while ( i > 1 && flag == 0) {
        if (h[i] < h[i/2]){
            k = i/2;
        }
        else {
            k = i;
        }

        if (k != i) {
            swap(k, i);
            i = k;
        }
        else {
            flag = 1;
        }
    }
}

int pop(){

    int t;
    t = h[1];
    pos[t] = 0;
    h[1] = h[size];
    pos[h[1]] = 1;
    size--;
    sift_down(1);
    return t;

}

int main() {

    scanf("%d %d", &n, &m);


    return 0;
}
