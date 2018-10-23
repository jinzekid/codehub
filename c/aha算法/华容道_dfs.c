/*
 * 华容道：
 * 3 4 1
 * 5 6 0
 * 8 2 7
 *
 * */
#include <stdio.h>

int a[51][51];
int book[51][51];
int next[4][2] = {
    {1, 0},
    {-1,0},
    {0,1},
    {0,-1}
};
int n, m;
int flag;

void dfs(int x, int y) {

    int tx, ty;
    int i, j;

    flag = 1;
    for (i = 1; i <= 3; i++) {
        for (j = 1; j <= 3; j++) {
            if (a[i][j] != (i-1)*3 + j){
                flag = 0;
                return;;
            }
        }
    }

    for (i = 0; i < 4; i++) {
        tx = x + next[i][0];
        ty = y + next[i][1];

        if (tx < 1 || tx > n || ty < 1 || ty > m) {
            continue;
        }

        if (a[tx][ty] == 0 && book[tx][ty] == 0) {
            book[tx][ty] = 1;

            dfs(tx, ty);
            book[tx][ty] = 0;
        }
    }

    return ;
}

int main(){

    int i, j;
    int startx, starty;
    scanf("%d %d %d %d", &n, &m, &startx, &starty);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    dfs(startx, starty);

    if (flag == 1) {
        printf("has answer\n");
    }
    else {
        printf("no answer\n");
    }
    return 0;
}
