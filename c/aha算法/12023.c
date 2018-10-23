#include <stdio.h>

struct node {
    int x;
    int y;
    int s;
};

struct node stack[101];
int top = 1;
int book[101][101];

int a[11][11];
int n, m;
int flag = 0;

void dfs(int sx, int sy, int dir) {

    int i, j;
    int tx, ty, ts;
    tx = sx;
    ty = sy;

    if (tx == n && ty == m+1) {
        flag = 1;
        for (i = 1; i < top; i++) {
            printf("(%d,%d)", stack[i].x, stack[i].y);
        }
        printf("\n");
        return;
    }

    if (flag == 1) return;

    //for (i = 0; i < 4; i++) 
    {
        //tx = sx + next[i][0];
        //ty = sy + next[i][1];

        if (tx < 1 || tx > n || ty < 1 || ty > m)
            return;

	if (book[tx][ty] == 1) return;

        //if (book[tx][ty] == 0 && a[tx][ty] != 0) 
	{

            //printf("(%d,%d)\n", tx, ty);
            stack[top].x = tx;
            stack[top].y = ty;
            top++;
            book[tx][ty] = 1;
            ts = a[tx][ty];
            if (ts == 5 || ts == 6) {
                // 直管
                if (dir == 4) {
                    dfs(tx, ty+1, 4);
                }
                else if (dir == 2) {
                    dfs(tx, ty-1, 2);
                }
                else if (dir == 1) {
                    dfs(tx+1, ty, 1);
                }
                else if (dir == 3) {
                    dfs(tx-1, ty, 3);
                }
            }
            else if (ts == 3 || ts == 4 || ts == 1 || ts == 2) {
                // 弯管
                if (dir == 1) {
                    dfs(tx, ty+1, 4);
                    dfs(tx, ty-1, 2);
                }
                else if (dir = 2) {
                    dfs(tx-1, ty, 3);
                    dfs(tx+1, ty, 1);
                }
                else if (dir == 3) {
                    dfs(tx, ty-1, 2);
                    dfs(tx, ty+1, 4);
                }
                else if (dir == 4) {
                    dfs(tx+1, ty, 1);
                    dfs(tx-1, ty, 3);
                }
            }
        }

        book[tx][ty] = 0;
        top--;
    }
}

void bfs(int sx, int sy) {

    /*
    int tx, ty, ts;
    int flag = 0;
    head = 1;
    tail = 1;
    que[1].x = sx;
    que[1].y = sy;
    que[1].s = a[sx][sy];
    book[sx][sy] = 1;
    tail++;

    while(head < tail) {


        ts = que[head].s;



        if (que[tail].x == n+1 && que[tail].y = m) {
            // found
            flag = 1;
            break;
        }


        if (flag == 1) {
            break;
        }

        head++;
    }

    if (flag == 1) {
        ;
    }
    else {
        printf("impossible\n");
    }
    */

}

int main() {

    int i, j;
    scanf("%d %d", &n, &m);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    //bfs(1, 1, 4);
    dfs(1,1,4);

    if (flag == 0) {
        printf("impossible\n");
    }

    return 0;
}
