#include <stdio.h>

struct note {
    int x;
    int y;
};
struct note que[401];
int book[20][20] = {0};
char a[20][20];
int head, tail;

int next[4][2] = {
    {0, 1},
    {0, -1},
    {1, 0},
    {-1, 0}
};

int getnum(int i, int j) {
    int sum, x, y;
    sum = 0;

    x = i;
    y = j;
    while (a[x][y] != '#'){
        if (a[x][y] == 'G') {
            sum++;
        }
        x--;
    }

    x = i;
    y = j;
    while(a[x][y] != '#') {
        if (a[x][y] == 'G') {
            sum++;
        }
        x++;
    }

    x = i;
    y = j;
    while(a[x][y] != '#'){
        if (a[x][y] == 'G'){
            sum++;
        }
        y--;
    }

    x = i;
    y = j;
    while(a[x][y] != '#'){
        if (a[x][y] == 'G'){
            sum++;
        }
        y++;
    }

    return sum;
}

void bfs(int n, int m, int startx, int starty){

    int i, sum, max;
    int mx, my;
    int tx, ty;
    head = 1;
    tail = 1;

    que[tail].x = startx;
    que[tail].y = starty;
    tail++;

    book[startx][starty] = 1;
    max = getnum(startx, starty);
    mx = startx;
    my = starty;

    while(head < tail) {

        for (i = 0; i <= 3; i++) {
            tx = que[head].x + next[i][0];
            ty = que[head].y + next[i][1];
            
            if (tx < 0 || tx > n-1 || ty < 0 || ty > m-1) {
                continue;
            }

            // 判断是否为平地且没有走过的
            if (a[tx][ty] == '.'  && book[tx][ty] == 0) {
                book[tx][ty] = 1;
                que[tail].x = tx;
                que[tail].y = ty;
                tail++;

                sum = getnum(tx, ty);
                if (sum > max) {
                    max = sum;
                    mx = tx;
                    my = ty;
                }
            }
        }

        head++;
    }


    printf("(%d, %d), %d\n", mx, my, max);
    return;
}

int main(){

    int i;
    int n, m, startx, starty;
    scanf("%d %d %d %d", &n, &m, &startx, &starty);

    for (i = 0; i <= n - 1; i++){
        scanf("%s", a[i]);
    }


    bfs(n, m, startx, starty);
    return 0;
}
