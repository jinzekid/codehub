#include <stdio.h>

struct note {
    int x;
    int y;
};

int n, m, max, mx, my;
char a[20][20];
int book[20][20] = {0};

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


void dfs(int x, int y){

    int i;
    int tx, ty;
    int sum = 0;

    if (x < 0 || x > n-1 || y < 0 || y > m-1){
        return;
    }

    tx = x;
    ty = y;

    for (i = 0; i <= 3; i++) {

        tx = tx + next[i][0];
        ty = ty + next[i][1];

        // 注意数组边界问题
        if (tx < 0 || tx > n - 1 || ty < 0 || ty > m - 1) 
            continue;

        if (a[tx][ty] == '.' &&  book[tx][ty] == 0) {
            book[tx][ty] = 1;

            sum = getnum(tx , ty);
            if (sum > max) {
                max = sum;
                mx = tx;
                my = ty;
            }

            dfs(tx, ty);
            book[tx][ty] = 0;
        }
    }
}

int main(){

    int startx, starty;
    int i;

    scanf("%d %d %d %d", &n, &m, &startx, &starty);
    
    for (i = 0; i < n; i++) {
        scanf("%s", a[i]);
    }

    dfs(startx, starty);

    printf("(%d, %d), %d\n", mx, my, max);
    return 0;
}
