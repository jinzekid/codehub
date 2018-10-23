#include <stdio.h>

int main(){

    int inf = 999999;
    int e[10][10], dis[10];
    int book[10] = {0};
    int i, j, k, min;
    int n, m;
    int t1, t2, t3;
    int u, v;

    scanf("%d %d", &n, &m);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            if (i == j) e[i][j] = 0;
            else e[i][j] = inf;
        }
    }

    for (i = 1; i <= m; i++) {
        scanf("%d %d %d", &t1, &t2, &t3);
        e[t1][t2] = t3;
    }

    for (i = 1; i <= n; i++) {
        dis[i] = e[1][i];
    }

    
    book[1] = 1;

    // Dijkstra 
    for (i = 1; i <= n; i++) {
        min = inf;

        for (j = 1; j <= n; j++) {
            if (min > dis[j] && book[j] == 0) {
                u = j;
                min = dis[j];
            }
        }

        book[u] = 1;

        for (v = 1; v <= n; v++) {
            if (e[u][v] < inf) {
                if (dis[v] > dis[u] + e[u][v]) {
                    dis[v] = dis[u] + e[u][v];
                 }
            }
        }
    }

    for (i = 1; i <= n; i++) {
        printf("%d ", dis[i]);
    }

    return 0;
}
