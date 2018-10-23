#include <stdio.h>

struct edge {
    int u;
    int v;
    int w;
};

struct edge e[10];
int n, m;
int f[7] = {0}, sum = 0, count = 0;

// 对边的权值进行快速排序
void quick_sort(int left, int right) {

    int i, j;
    struct edge t;

    if (left > right) return;

    i = left;
    j = right;
    while (i != j) {
        while(e[j].w >= e[left].w && i < j) {
            j--;
        }

        while (e[i].w >= e[right].w && i < j) {
            i++;
        }

        // exchange
        if (i < j) {
            t = e[i];
            e[i] = e[j];
            e[j] = t;
        }
    }

    t = e[left];
    e[left] = e[i];
    e[i] = t;

    quick_sort(left, i-1);
    quick_sort(i+1, right);
}

// 并查集，查找祖先
int getf(int v) {
    if (f[v] == v) 
        return v;
    else {
        f[v] = getf(f[v]);
        return f[v];
    }
}

// 合并集和
int merge(int v, int u) {

    int t1, t2;

    t1 = getf(v);
    t2 = getf(u);

    if (t1 != t2) {
        f[t2] = t1;
        return 1;
    }

    return 0;
}


int main(){
    int i;
    scanf("%d %d", &n, &m);

    for (i = 1; i <= m; i++) {
        scanf("%d %d %d", &e[i].u, &e[i].v, &e[i].w);
    }

    quick_sort(1, m);

    for (i = 1; i <= n; i++) {
        f[i] = i;
    }

    for (i = 1; i <= m; i++) {
        if (merge(e[i].u, e[i].v)) {
            count++;
            sum = sum + e[i].w;
        }
        
        if (count == n -1) {
            break;
        }
    }

    printf("%d\n", sum);
}


