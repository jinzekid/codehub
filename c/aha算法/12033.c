#include <stdio.h>
#include <stdlib.h>




void search(char a[][50], int x, int y, int *ret_sum) {

    int sum = 0;
    int x1=x;
    int y1=y;

    // up search
    while(a[x1][y1] != '#'){
        if (a[x1][y1] == 'G') {
            sum++;
        }
        x1--;
    }

    // down serch 
    x1=x;y1=y;
    while(a[x1][y1] != '#'){
        if (a[x1][y1] == 'G') {
            sum++;
        }
        x1++;
    }

    // right search 
    x1=x;y1=y;
    while(a[x1][y1] != '#'){
        if (a[x1][y1] == 'G') {
            sum++;
        }
        y1++;
    }

    // left search
    x1=x;y1=y; 
    while(a[x1][y1] != '#'){
        if (a[x1][y1] == 'G') {
            sum++;
        }
        y1--;
    }

    *ret_sum = sum;
}

int main(){

    int n, m, n1, m1;
    int x, y;
    int sum = 0, max = 0;
    int i, j;
    char a[50][50] = {0};
    int book[50][50] = {0};

    scanf("%d %d %d %d", &n, &m, &n1, &m1);

    for (i = 0; i < n; i++) {
        scanf("%s", a[i]);
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {

    x = n1+i; y = m1+j;
    while(a[x][y] == '.') {
        //printf("%d %d\n", x, y);
        if (book[x][y] == 0) {
            search(a, x, y, &sum);
            book[x][y] = 1;
        }

        if (sum > max) {
            max = sum;
        }
        x++; 
    }

    x = n1+i; y = m1+j;
    while(a[x][y] == '.') {   
        //printf("%d %d\n", x, y);
        if (book[x][y] == 0) {
            search(a, x, y, &sum);
            book[x][y] = 1;
        }

        if (sum > max) {
            max = sum;
        }
        x--;
    }

    x = n1+i; y = m1+j;
    while(a[x][y] == '.') {
        //printf("%d %d\n", x, y);
        if (book[x][y] == 0) {
            search(a, x, y, &sum);
            book[x][y] = 1;
        }

        if (sum > max) {
            max = sum;
        }
        y++;

    }

    x = n1+i; y = m1+j;
    while(a[x][y] == '.') {
        //printf("%d %d\n", x, y);
        if (book[x][y] == 0) {
            search(a, x, y, &sum);
            book[x][y] = 1;
        }
        
        if (sum > max) {
            max = sum;
        }
        y--;
    }
        
        }
    }
    
    printf("%d\n", max);
    return 0;
}
