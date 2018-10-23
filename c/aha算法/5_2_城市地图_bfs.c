#include <stdio.h>

#define INF 999999

struct node {
    int x;
    int s;
};

int e[101][101];
int book[101][101];
struct node que[101];
int stack[101];
int top;
int head;
int tail;
int n, m;
int dis;
int min = INF;

void bfs(int cur){

    int i;
    int j, sum;
    head = 1;
    tail = 1;
    top = 1;
    que[tail].x = cur;
    que[tail].s = 0;
    tail++;
    stack[top] = cur;
    top++;
    book[cur][1] = 1;
    sum = 0;
    dis = 0;

    while (head < tail) {

        cur = que[head].x; // 从第一个点开始

        if (cur == n) { // 如果等于目的地就判断距离大小
            if (min > que[head].s) {
                min = que[head].s;
                printf("top==%d\n", top);
                for (i = 0; i < top; i++) {
                    printf("%3d", stack[i]);
                }
                printf("\n");
            }
        }

        for (j = 1; j <= n; j++) {
            // 对没有搜索过的点进行入队操作
            if (cur != j && e[cur][j] != INF && book[cur][j] == 0) {

                book[cur][j] = 1;
                que[tail].s = que[head].s +  e[cur][j];
                que[tail].x = j;
                tail++;

                stack[top] = cur;
                top++;
                //bootk[j] = 0;
            }
        }

        head++;
    }
}

int main() {

    int i, j;
    int a, b, v;
    scanf("%d %d", &n, &m);

    //初始化数组
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            if (i == j) e[i][j] = 0;
            else e[i][j] = INF;
        }
    }

    for (i = 1; i<= m; i++) {
        scanf("%d %d %d", &a, &b, &v);
        e[a][b] = v;
    }


    bfs(1);
    printf("%d\n", min);

    return 0;
}
