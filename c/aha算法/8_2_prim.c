#include <stdio.h>

int e[7][7],  dis[7], book[7] = {0};
int inf = 999999;
int count = 0, sum = 0;
int min = 0;

int main(){

    int u, v, k;
    int i, j;
    int n, m;
    scanf("%d %d", &n, &m);

    // 初始化邻接矩阵
    for (i = 1; i <=n ; i++) {
        for (j = 1; j <= n; j++) {
            if (i == j) e[i][j] = 0;
            else e[i][j] = inf;
        }
    }

    // 输入矩阵值
    for (i = 1;  i<= m; i++) {
        scanf("%d %d %d", &u, &v, &k);
        e[u][v] = k;
        e[v][u] = k;
    }

    for (i = 1;  i <= n; i++) {
        dis[i] = e[1][i];
    }

    // prime算法核心
    book[1] = 1;
    count++;
    while (count < n) {

	// 寻找数组中最小距离的j点
        min = inf;
        for (i =1; i <= n; i++) {
            if (book[i] == 0 && dis[i] < min) {
                min = dis[i] ; j = i;
            }
        }


        book[j] = 1;count++; sum += dis[j];
	// 扫描以j点出发的所有边，更新生成树到每个非树顶点的距离
        for (k = 1; k <= n; k++) {
            if (book[k] == 0 && dis[k] > e[j][k]){
                dis[k] = e[j][k];
            }
        }
    } 


    printf("%d\n", sum);

    return 0;
}
