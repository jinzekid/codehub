#include <stdio.h>

int e[101][101];
int book[101] = {0};
int que[10001], head, tail;
int n, m;

void bfs(int cur){

    int i;
    head = 1;
    tail = 1;

    que[tail] = cur;
    tail++;
    book[1] = cur;

    while(head < tail) {
        cur = que[head];
        for (i = 1; i <= n; i++) {
            if (e[cur][i] == 1 && book[i] == 0) {
                book[i] = 1;
                que[tail] = i;
                tail++;
            }

            if (tail > n) {
                break;
            }
        }

        head++;
    }


    for (i = 1; i < tail; i++) {
        printf("%2d", que[i]);
    }
    printf("\n");
}

int main(){

    int i, j, a, b;
    scanf("%d %d", &n, &m);

    for (i = 1; i <=n ; i++) {
        for (j = 1; j <= m; j++) {
            if (i == j) e[i][j] = 0;
            else e[i][j] = 999999;
        }
    }

    for (i = 1; i <= m; i++) {
        scanf("%d %d", &a, &b);
        e[a][b] = 1;
        e[b][a] = 1;
    }

    bfs(1);

    return 0;
}
