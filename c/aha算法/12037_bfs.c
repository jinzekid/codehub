#include <stdio.h>

struct node {
    int x;
    int y;
};
struct node que[10001];
int a[101][101];
int book[101][101];
int next[4][2] = {
    {1,0},
    {-1,0},
    {0,1},
    {0,-1}
};
int head, tail;
int n, m;
int sum, max;
int num = 0;

void bfs(int x, int y, int num){

    int i;
    int tx, ty;

    head = 1;
    tail = 1;
    que[tail].x = x;
    que[tail].y = y;
    tail++;

    while (head < tail) {

        for (i = 0; i < 4; i++) {
            tx = que[head].x + next[i][0];
            ty = que[head].y + next[i][1];

            if (tx < 1 || tx > n || ty < 1 || ty > m)
                continue;

            if (a[tx][ty] > 0 && book[tx][ty] == 0){
                book[tx][ty] = 1;
                a[tx][ty] = num;

                que[tail].x = tx;
                que[tail].y = ty;
                tail++;

                sum++;
            }
        }
        
        head++;
    }
}

int main(){

    int i, j;
    scanf("%d %d", &n, &m);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            
            if (a[i][j] > 0){
                num--;
                sum = 0;
                bfs(i, j, num);

                if (sum > max){
                    max = sum;
                }
            }
        }
    }

    printf("%d\n", max);


    for (i = 1; i <= n; i++) {
        for (j = 1; j<= m; j++) {
            printf("%2d", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
