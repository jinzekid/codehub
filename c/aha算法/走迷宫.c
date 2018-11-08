/***********************************************
 * 走迷宫
 * 利用广度搜索法进行遍历
 * 设置边界为50x50
 *
 * 注意点：
 * 1.搜索的边界比较
 * 2.搜索的tx，ty的值
 * 3.结束条件
 * 4.book[tx][ty] = 0，需要回溯
 *
 * *********************************************/
#include <stdio.h>
#include <stdlib.h>

int n, m, p, q, min = 99999999;
int a[51][51], book[51][51];
int next[4][2] = {
    {0, 1},
    {1, 0},
    {0, -1},
    {-1, 0}
};

void dfs(int x, int y, int step){

    int tx, ty, i;
    if (x == p && y == q){
        if (step < min) {
            min = step;
        }
        return;
    }

    for (i = 0; i <= 3; i++) {
        tx = x + next[i][0];
        ty = y + next[i][1];

        if (tx < 1 || tx > n || ty <1 || ty > m) {
            continue;
        }

        if (a[tx][ty] == 0 && book[tx][ty] == 0) {
            book[tx][ty] = 1;
            dfs(tx, ty, step+1);
            book[tx][ty] = 0;
        }
    }
}

int main(){

    int i, j, startx, starty;
    scanf("%d %d", &n, &m);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    scanf("%d %d %d %d", &startx, &starty, &p, &q);
    book[startx][starty] = 1;
    dfs(startx, starty, 0);

    printf("%d\n", min);

    return 0;
}
