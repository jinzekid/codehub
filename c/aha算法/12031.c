#include <stdio.h>

int a[10] = {0};
int book[10] = {0};
int n;

void dfs(int step) {

    int i;
    if (step == n + 1) {
        for (i = 1; i <= n; i++) {
            printf("%d", a[i]);
        }
        printf("\n");
        return;
    }


    for (i = 1; i <= n; i++) {
        if (book[i] == 0) {
            book[i] = 1;
            a[step] = i;

            dfs(step + 1);
            book[i] = 0;
        }
    }

}

int main(){

    int i;
    scanf("%d", &n);

    dfs(1);

    return 0;
}
