#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

void main(){
    time_t t1, t2;
    struct timeval tv1, tv2;
    long t;
    double x, sum = 1, sum1 = 1;
    int i, j, n;
    printf("Please input x, n:");
    scanf("%lf%d", &x, &n);

    gettimeofday(&tv1, NULL);
    for (i=1;i<=n;i++){
        sum1 *= -1.0/x;
        sum += sum1;
    }

    gettimeofday(&tv2, NULL);
    t = (tv2.tv_sec-tv1.tv_sec) * 1000 + (tv2.tv_usec-tv1.tv_usec)/1000;
    printf("sum=%1f use easpled: %ld ms\n", sum, t);

    getchar();
}
