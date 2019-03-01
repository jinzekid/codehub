#include <stdio.h>

int main(){

    int i, j;
    int temp, yuShu;
    int cnt;
    unsigned int a;
    int b;
    scanf("%u %d", &a, &b); // 整数 a、b,范围是1<=n<=a(a <= 10000000), b是在 a之间出现的数字

    // 如果输入有误就直接跳出程序
    if (b <0 || b > 9 || a < 1 || a > 10000000) {
        printf("Input Error");
        return 0;
    } 

    cnt = 0; // 计数清零
    for (i = 1; i <= a; i++) {
        temp = i;
        while (temp) {
            if (temp/10  == 0) break; // 如果数小于10就直接跳出循环
            yuShu = temp % 10; // 获取余数
            if (yuShu == b)    // 余数和b进行比较
                cnt += 1;      // 如果相等就cnt加1

            temp /= 10;        // 获取剩余数
        }
        
        if (temp == b) {       // 对最后一位数进行比较
            cnt += 1;
        }
    }

    printf("%d\n", cnt);
    return 0;
}
