#include <stdio.h>

int e[101][101];
int book[101];
int min = 999999;
int n, m;
int stack[101];
int top;

void dfs(int cur, int dis){
    
    int j, i;

    if (cur == n) {
        
        for (i = 1; i < top; i++) {
            printf("%2d", stack[i]);
        }   
        printf("\n");

        if (dis < min) {
            min = dis;
        }
        return;
    }
    
    if (dis > min) return;


    for (j = 1; j <= n; j++) {
        if (e[cur][j] != 999999 && book[j] == 0) {
            book[j] = 1;
            stack[top++] = j;

            dfs(j , dis+e[cur][j]);
            book[j] = 0;
            top--;
        }
    }

    return;
}

int main(){

    int i, j;
    int a, b, c;

    scanf("%d %d", &n, &m);

    for (i = 1; i <= n; i++) {
        for (j = 1; j <=n; j++) {
            if (i == j) e[i][j] = 0;
            else e[i][j] = 999999;
        }
    }

    for (i = 1; i <= m; i++) {
        scanf("%d %d %d", &a, &b, &c);
        e[a][b] = c;
    }


    book[1] = 1;
    top = 1;

    stack[top++] = 1;
    dfs(1, 0);

    
    printf("%d\n", min);
    return 0;
}
