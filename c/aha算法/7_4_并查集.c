#include <stdio.h>
int f[1000] = {0}, n , m;

void init() {
    int i;
    for (i = 1; i <= n; i++) {
        f[i] = i;
    }
}

int getf(int v){

    if (f[v] == v) {
        return v;
    }
    else {
        f[v] = getf(f[v]);//路径压缩，每次返回函数时候，顺带把路上敌人编号改为祖宗编号
        return f[v];
    }
}

void merge(int v, int u) {

    int t1, t2;
    t1 = getf(v);
    t2 = getf(u);

    if (t1 != t2) {
        f[t2] = t1;//靠左原则，左边变成右边的boss，把右边的集和，作为左边集和的子集和
    }
}


int main() {

    int i, x, y;
    int sum = 0;
    scanf("%d %d", &n, &m);

    init();

    for (i = 1; i <= m; i++) {
        scanf("%d %d", &x, &y);
        merge(x, y);
    }

    for (i = 1; i <= n; i++) {
        if (f[i] == i) {
            sum++;
        }
    }

    printf("%d\n", sum);
}
