#include <stdio.h>

int a[101][101] = {0};
int book[101][101] = {0};
int n, m;
int sum, max = 0;

int next[4][2] = {
    {1,0},
    {0,1},
    {-1,0},
    {0,-1}
};

void dfs(int x, int y, int num){

    int i;
    int tx,ty;

    for (i = 0; i < 4; i++) {
        tx = x + next[i][0];
        ty = y + next[i][1];

        if (tx < 1 || tx > n || ty < 1 || ty > m) {
            continue;
        }

        if (a[tx][ty] > 0 && book[tx][ty] == 0) {
            book[tx][ty] = 1;
            a[tx][ty] = num;

            sum++;
            dfs(tx, ty, num);
        }
    }
    
    return;
}

int main(){

    int i, j;
    int startx, starty;
    int num = 0;
    scanf("%d %d", &n, &m);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    for (i = 1; i <= n; i++) {
        for (j = 1; j<= m; j++) {
            
            if (a[i][j] > 0) {
                num--;
                dfs(i, j, num);

                if (sum > max) {
                    max = sum;
                }
                sum = 0;
            }
        }
    }

    printf("max=%d\n", max);
    return 0;
}
