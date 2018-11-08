#include <stdio.h>

struct node {
    int x;
    int s;
};

struct node que[100001];
int inf = 999999;
int e[1001][1001];
int n, m, start, end;
int book[1001];
int head;
int tail;

void bfs(int x) {

    int flag;
    int i, tx;
    head = 1;
    tail = 1;
    que[tail].x = x;
    que[tail].s = 0;
    tail++;

    flag = 0;
    while(head < tail) {

        tx = que[head].x;
        for (i = 1; i <= n; i++){
            if (e[tx][i] != inf  && book[i] == 0) {
                book[i] = 1;

                que[tail].x = i;
                que[tail].s = que[head].s + 1;
                tail++;


                if (i == end) {
                    flag = 1;
                    break;
                }
            }
        }

        if (flag == 1) {
            break;
        }

        head++;
    }

    
    printf("%d\n", que[tail-1].s);
}

int main() {

    int i, j;
    int x, y;
    scanf("%d %d %d %d", &n, &m, &start,  &end);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <=n; j++) {
            if (i == j) e[i][j] = 0;
            else e[i][j] = inf;
        }
    }

    for (i = 1; i <= m; i++) {
        scanf("%d %d", &x, &y);
        e[x][y] = 1;
        e[y][x] = 1;
    }


    bfs(start);

    return 0;
}
