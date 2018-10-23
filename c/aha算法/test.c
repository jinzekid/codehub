#include <stdio.h>

struct node {
    int x;
    int y;
};
struct node que[10001];
int head, tail;
int n, m;
int a[101][101] = {0};
int book[101][101] = {0};
int sum = 0;

int next[4][2] = {
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}
};

void bfs(int x, int y) {

    int tx, ty;
    int i;

    head = 1;
    tail = 1;

    que[tail].x = x;
    que[tail].y = y;
    tail++;

    while (head < tail) {

        for (i = 0; i < 4; i++) {
            tx = que[head].x + next[i][0];
            ty = que[head].y + next[i][1];

            if (tx < 1 || tx > n || ty < 1 || ty > m) {
                continue;
            }

            if (a[tx][ty] > 0 && book[tx][ty] == 0) {
                book[tx][ty] = 1;
                sum++;

                que[tail].x = tx;
                que[tail].y = ty;
                tail++;
            }
        }
        head++;
    } 

}

int main(){
    
    int i, j;
    int startx, starty;
    scanf("%d %d %d %d", &n, &m, &startx, &starty);

    for (i = 1; i <= n; i++) {
        for(j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    bfs(startx, starty);

    printf("%d\n", sum);
    return 0;
}
