#include <stdio.h>

struct note {
    int x;
    int y;
};

int a[51][51] = {0};
int book[51][51] = {0};

int next[4][2] = {
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}
};
int sum;
int n, m;

void dfs_bdtx(int x, int y, int color) {

    int i;
    int tx, ty;

    for (i = 0; i < 4; i++) {
        tx = x + next[i][0];
        ty = y + next[i][1];

        if (tx < 0 || tx > n -1 || ty < 0 || ty >m -1)
            continue;

        if (a[tx][ty] != 0 && book[tx][ty] == 0) {
            book[tx][ty] = 1;
            a[tx][ty] = color;
            sum++;
            dfs_bdtx(tx, ty, color);
        }
    }

    return;
}

int main(){

    int i, j;
    int startx, starty;
    scanf("%d %d %d %d", &n, &m, &startx, &starty);

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    sum = 0;
    dfs_bdtx(startx, starty, -1);

    //printf("%d\n", sum);

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            printf("%3d", a[i][j]);
        }

        printf("\n");
    }
    return 0;
}
