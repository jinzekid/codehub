#include <stdio.h>

int book[10001];    // 一共长度为10001的数组表示长度为L的路段
int start[100];     // 开始路段
int end[100];       // 结束路段

int main(){

    int i, j;
    int cnt = 0;
    int L, M;
    scanf("%d %d",&L, &M); // 输入总长度L, 路段数目M

    // 对输入进行总长度和路段数进行判断
    if (L < 1 || L > 10000 || M <1 || M > 100) {
        printf("Error input\n");
        return 0;
    }

    // 输入路段的间隔起始和结束距离
    for (i = 0; i < M; i++) {
        scanf("%d %d", &start[i], &end[i]);
    }
    

    for (i = 0; i < M; i++) {
        // 对起始路段到结束路段的book数组内的值进行判断，如果是0就置为1，表示需要移除
        for (j = start[i]; j <= end[i]; j++) {
            if (book[j] == 0)  {
                book[j] = 1;
            }
        }
    }

    // 对所有路段中需要种树进行统计，如果是0就表示需要种树，并进行cnt+1
    for (i = 0; i <= L; i++) {
        if (book[i] == 0) {
            cnt += 1;
        }
    }

    printf("%d\n", cnt);
    return 0;
}
