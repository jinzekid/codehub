#include <stdio.h>

struct note {
    int x;
    int y;
    int f;
    int s;
};

struct note que[2501];
int head, tail;
int a[51][51] = {0};
int book[51][51] = {0};
int head = 1;
int tail = 1;
int flag;

int next[4][2] = {
    {0, 1},
    {1, 0},
    {0, -1},
    {-1, 0}
};


void bfs(int n, int m, int startx, int starty, int p, int q) {

    int i, x, y;
    int tx, ty;
    
    // init queue
    head = 1;
    tail = 1;

    // insert (x, y) to queue
    que[tail].x = startx;
    que[tail].y = starty;
    que[tail].f = 0;
    que[tail].s = 0;
    tail++;
    book[startx][starty] = 1;

    flag = 0;
    printf("n=%d, m=%d\n", n, m);

    while (head < tail) {
        for (i = 0; i < 4; i++) {
            tx = que[head].x + next[i][0];
            ty = que[head].y + next[i][1];
            if (tx < 1 || tx > n || ty < 1 || ty > m) {
                continue;
            }

            if (a[tx][ty] == 0 && book[tx][ty] == 0) {
                book[tx][ty] = 1;
                que[tail].x = tx;
                que[tail].y = ty;
                que[tail].f = head;
                que[tail].s = que[head].s+1;
                tail++;
            }

            if (tx == p && ty == q) {
                flag = 1;
                break;
            }
        }

        if (flag == 1) {
            break;
        }

        head++;
    }

    printf("%d\n", que[tail-1].s);
}


int main(){

    int n, m, i, j;
    int startx, starty, p, q;

    scanf("%d %d", &n, &m);
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }
    scanf("%d %d %d %d", &startx, &starty, &p, &q);

    bfs(n, m, startx, starty, p, q);
    return 0;
}
