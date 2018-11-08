#include <stdio.h>

struct node {
    int c;
    int m;
    int e;
    int sum;
    int id;
};
struct node h[301];
int n;

struct node stack[11];
int top;

void swap(int a, int b) {
    struct node tmp;
    tmp = h[b];
    h[b] = h[a];
    h[a] = tmp;
}

void sift_down(int i) {

    int flag = 0;
    int t;

    while(i <= n/2 && flag == 0) {

        if (h[i].sum < h[2*i].sum) {
            t = 2*i;
        }
        else if (h[i].sum == h[2*i].sum) {
            if (h[i].c < h[2*i].c) {
                t = 2*i;
            }
            else if (h[i].c == h[2*i].c) {
                if (h[i].id > h[2*i].id) {
                    t = 2*i;
                }
            }
            else {
                t = i;
            }
        }
        else {
            t = i;
        }

        if (i*2+1 <= n) {
            if (h[t].sum < h[2*i+1].sum) {
                t = 2*i+1;
            }
            else if (h[t].sum == h[2*i+1].sum) {
                if (h[t].c < h[2*i+1].c) {
                    t = 2*i+1;
                }
                else if (h[t].c == h[2*i+1].c) {
                    if (h[t].id > h[2*i+1].id){
                        t = 2*i+1;
                    }
                }
            }
        }

        if (t != i) {
            swap(t, i);
            i = t;
        }
        else {
            flag = 1;
        }
    }
}

void heap_sort(){

    int t;
    top = 1;

    while(n > 0) {
        struct node tmp;
        tmp = h[1];
        h[1] = h[n];
        h[n] = tmp;
        n--;
        sift_down(1);

        stack[top++] = tmp;
        //printf("%d  %d", tmp.id, tmp.sum);
        //printf("\n");
    }

}

int main(){

    int i, m;
    scanf("%d", &m);

    n = 0;
    for (i = 1; i <= m; i++) {
        scanf("%d   %d   %d", &h[i].c, &h[i].m, &h[i].e);
        h[i].id = i;
        h[i].sum = h[i].c+h[i].m+h[i].e;
    }

    n = m;
    for (i = n/2; i >= 1; i--) {
        sift_down(i);
    }
    
    n = m;
    heap_sort();

    for (i = 1; i <= 5; i++) {
        printf("%d  %d", stack[i].id, stack[i].sum);
        printf("\n");
    }

    return 0;
}
