#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    char a[20][21];
    int i, j, sum, map=0, p, q, x, y, n, m;
    // 读入n和m，n表示多少行字符，m表示每行有多少列
    scanf("%d %d", &n, &m);

    // 读入n行
    for(i = 0; i <= n-1; i++) {
        scanf("%s", a[i]);
    }
    printf("%c\n", a[0][0]);

    // 用两重循环每句地图中的每一个点
    for (i = 0; i <= n-1; i++) {
        for (j = 0; j <= m -1; j++) {
            if (a[i][j] == '.') {
                sum = 0;

                x = i; y = j;
                // 向上统计可以小妹的敌人数量
                while(a[x][y] != '#') {
                    if (a[x][y] == 'G'){
                        sum++;
                    }
                    x--;
                }

                x = i; y = j;
                //  向下统计
                while(a[x][y] != '#') {
                    if (a[x][y] == 'G') {
                        sum++;
                    }
                    x++;
                }

                x = i; y = j;
                while(a[x][y] != '#'){
                    if (a[x][y] == 'G'){
                        sum++;
                    }
                    y--;
                }

                x = i; y = j;
                while(a[x][y] != '#') {
                    if (a[x][y] == 'G') {
                        sum++;
                    }
                    y++;
                }


                // 更新map
                if (sum > map) {
                    map = sum;
                    p = i;
                    q = j;
                }
            }
        }
    }

    
    printf("将炸弹防止在（%d, %d）, 最多可以消灭%d个敌人\n", p, q, map);
    getchar();
    return 0;
}
