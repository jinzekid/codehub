#include <stdio.h>
struct node {
    int x;
    int y;
    int s;
};
struct node que[10001];
int n, m; // <= 100
int a[101][101];
int book[101][101];

int head;
int tail;
int next[4][2] = {
    {1,0},
    {-1,0},
    {0,1},
    {0,-1}
};

int main(){

    int i, j, k;
    int startx, starty;
    int endx, endy;
    int tx, ty;
    int flag;
    
    scanf("%d %d", &n, &m);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }


    scanf("%d %d %d %d", &startx, &starty, &endx, &endy);

    flag = 0;
    head = 1;
    tail = 1;
    que[tail].x = startx;
    que[tail].y = starty;
    que[tail].s = 0;
    tail++;


    while(head < tail){

        for (k = 0; k < 4; k++) {
            tx = que[head].x + next[k][0];
            ty = que[head].y + next[k][1];

            if (tx < 1 || tx > n || ty < 1 || ty > m)
                continue;

            
            if (a[tx][ty] == 0 && book[tx][ty] == 0){
                book[tx][ty] = 1;
                que[tail].x = tx;
                que[tail].y = ty;
                que[tail].s = que[head].s + 1;
                tail++;
            }
            
            if (tx == endx && ty == endy) {
                flag = 1;
                break;
            }

        }

        if (flag == 1) {
            break;
        }

        head++;
    }

    if (flag == 1) {
        printf("%d\n", que[tail-1].s);
    }
    else {
        printf("No Way!");
    }


    return 0;
}
