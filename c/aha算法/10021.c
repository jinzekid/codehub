#include <stdio.h>
#include <string.h>
#include <math.h>

char ch[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z'};
int b[26] = {0}; // 对于26出现的字母进行统计
char a[100]; // 输入字符串，长度小于100


// 判断是否是质数
int is_prime(int m) {

    int k, i;
    
    // 1,0都不是质数
    if (m == 1 || m == 0)
        return 0;
    
    // 求平方根，注意sqrt()的参数为 double 类型，这里要强制转换m的类型
    k=(int)sqrt( (double)m );
    for(i=2;i<=k;i++)
        if(m%i==0)
            break;
    // 如果完成所有循环，那么m为素数
    // 注意最后一次循环，会执行i++，此时 i=k+1，所以有i>k
    if(i>k)
        return 1;
    
    return 0;
}


int main(){

    int i, j;
    int maxc, minc; // 统计最多出现的字母数量和最少出现的字母数量
    int ret;
    int isGetNumStatus;
    int aLen;// 输入字符串的长度
    
    // 输入长度小于100的单词
    scanf("%s", a);

    aLen = strlen(a);
//    printf("aLen=%d\n", aLen);
    for (i = 0; i < aLen; i++) {
        for (j = 0; j < 26; j++) {
            if (ch[j] == a[i]) {
                b[j] += 1;
            }
        }
//        printf("%c", a[i]);
    }

//    printf("\n");
    maxc = 0; minc = 0; isGetNumStatus = 0;
    for (i = 0; i < 26; i++) {
        if (isGetNumStatus == 0 && b[i] > 0) {
            isGetNumStatus = 1;
        }
        
        // 如果画遇到了第一个不为0的字母，就初始化maxc，minc
        if (isGetNumStatus == 1) {
            maxc = b[i];
            minc = b[i];
            isGetNumStatus = 2;
//            printf("i=%d, maxc=%d, minc=%d\n",i, maxc, minc);

        }
        else if (isGetNumStatus == 2){
            if (b[i] > maxc) {
                maxc = b[i];
            }
            if (b[i] < minc && b[i] > 0) { // 注意，这里需要b[i]>0才能赋值)
                minc = b[i];
            }
        }
    }

//    printf("maxc=%d, minc=%d\n", maxc, minc);
    ret = is_prime(maxc - minc);
    if (ret == 1) {
        printf("Lucky Word\n");
        printf("%d\n", maxc-minc);
    }
    else {
        printf("No Answer\n");
        printf("0\n");
    }

    return 0;
}
