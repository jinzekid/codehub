// 12026
// 为什么是1111，因为是这个是等式，
// 如果是11111 + 11111 = x，x就没有火柴表示了，因为正好用光24根火柴
// 所以两个最大的数的等式为1111 + 1111 = x
#include <stdio.h>

int func(int x) {

    int m = 0;
    int a[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    while (x/10 != 0) {
        m += a[x%10];
        x = x/10;
    }
    m += a[x];
    return m;
}

int main(){

    int n, c;
    int sum = 0;
    int i, j;
    scanf("%d", &n);

    for (i = 0; i <= 1111; i++) {
        for (j = 0; j <= 1111; j++) {
            c = i+j;
            if (func(i) + func(j) + func(c) == n - 4) {
                printf("%d + %d = %d\n", i, j , (i+j));
                sum++;
            }
        }
        //printf("i===%d\n",i);
    }

    printf("%d\n",sum);
    return 0;
}
