#include <stdio.h>

char a[51][51];

int main() {
    int n, m, i, j;
    int x, y;
    int p, q;
    int sum = 0;
    int max = 0;
    scanf("%d %d", &n, &m);

    for (i = 0; i < n; i++) {
        scanf("%s", a[i]);
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (a[i][j] == '.') {
                sum = 0;
                
                x = i; y = j;
                // search up
                while(a[x][y] != '#') {
                    if (a[x][y] == 'G') sum++;
                    x--;
                }

                // search down 
                x = i; y = j;
                while(a[x][y] != '#') {
                    if (a[x][y] == 'G') sum++;
                    x++;
                }

                // search left 
                x = i; y = j;
                while (a[x][y] != '#'){
                    if (a[x][y] == 'G') sum++;
                    y--;
                }

                // search right 
                x = i; y = j;
                while(a[x][y] != '#'){
                    if (a[x][y] == 'G') sum++;
                    y++;
                }

                if (sum > max) {
                    max = sum;
                    p = i;
                    q = j;
                }
            }
        }
    }

    printf("x:%d, y:%d\n", p, q);
    printf("%d\n", max);

    return 0;
}
