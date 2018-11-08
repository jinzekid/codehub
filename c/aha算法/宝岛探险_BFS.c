#include <stdio.h>

struct note {
    int x;
    int y;
};
int a[51][51];
struct note que[2501];
int book[51][51] = {0};
int head;
int tail;

int next[4][2] = {
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}
};

void bfs_bdtx(int n, int m, int x, int y){


    int sum, i;
    int tx, ty;

    tx = x;
    ty = y;

    head = 1;
    tail = 1;
    que[tail].x = tx;
    que[tail].y = ty;
    book[tx][ty] = 1;
    sum = 1;
    tail++;
    while (head < tail) {

        for (i = 0; i < 4; i++) {
            tx = que[head].x + next[i][0];
            ty = que[head].y + next[i][1];

            if (tx < 0 || tx > n-1 || ty < 0 || ty > m-1) 
                continue;
            
            if (a[tx][ty] != 0 && book[tx][ty] == 0) {
                book[tx][ty] = 1;
                que[tail].x = tx;
                que[tail].y = ty;
                tail++;
                sum++;
            }
        }

        head++;
    }

    printf("%d\n", sum);
}

int main(){

    int n, m;
    int i, j;
    int startx, starty;

    scanf("%d %d %d %d", &n, &m, &startx, &starty);

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            scanf("%d", &a[i][j]);
        }
    }


    bfs_bdtx(n, m, startx, starty);

    return 0;

}
