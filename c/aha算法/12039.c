/** 已知 n 个整数 x1,x2,…,xn，以及一个整数 k（k＜n）。从 n 个整数中任选 k 个整数相加，可分别得到一系列的和。例如当 n=4，k＝3，4 个整数分别为 3，7，12，19 时，可得全部的组合与它们的和为：
3＋7＋12=22　　3＋7＋19＝29　　7＋12＋19＝38　　3＋12＋19＝34。
现在，要求你计算出和为素数共有多少种。
例如上例，只有一种的和为素数：3＋7＋19＝29）。
 * */
#include <stdio.h>
#include <math.h>

int a[20];
int b[20];
int ret[1000];
int book[20];
int n, m;
int cnt = 0;

// 数素判断
int is_shusu(int a) {
    int i;
    int k;

    k = (int)sqrt((double)a);
    for (i=2; i<=k; i++) {
        if (a%i == 0) break;
    }

    if (i > k) return 1;
    return 0;
}

void dfs(int step) {

    int i, j;
    int sum;
    if (step == m) {

        // 判断是否是数素, 如果是就sum+1
        sum = 0;
        for (i = 0; i < m; i++) {
            sum += b[i];
        }

        if (is_shusu(sum) == 1) {
            for (j = 0; j < cnt; j++) {
                if (ret[j] == sum) {
                    return;
                }
            }
            
            for (i = 0; i < step; i++) {
                printf("%d+", b[i]);
            }
            printf("=%d\n", sum);

            ret[cnt] = sum;
            cnt+=1;
            for (i = 0; i < cnt; i++) {
                printf("%d ", ret[i]);
            }
            printf("\n");

        }
        return;
    }

    // 一共n个数
    for (i = 0; i < n; i++) {
        // 组合需要的数字为m个 
        if (book[i] == 0) {
            b[step] = a[i]; // 把数a[i]放入b[step]中
            book[i] = 1;    // 将第i个数标记为1
        
            dfs(step+1);    // 第step个数设置好了，走下一个step
            book[i] = 0;    // 把第i个数标记为0
        }
    }
}

int main() {

    int i;
    scanf("%d %d", &n, &m);

    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    dfs(0);
    printf("%d\n", cnt);
    return 0;
}
