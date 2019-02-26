#include <stdio.h>

int ren[10000]; // 表示每个人需要节水的量以及排队顺序
int bookRen[10000] = {0}; // 记录人是否已经接过水 1:接过 2:没有接过
int bookWater[100] = {0}; // 记录水龙头的状态 1:被占用 0:空闲

int a[100]; // 接水数组

int main(){

    int i, k, j;
    int renCnt = 0;
    int timeCnt = 0;
    int stop = 0;
    int flag = 0;
    int min = 99999;
    int n, m; // n表示接水的人数, m表示龙头个数
    scanf("%d %d", &n, &m);

    // 初始化每个人需要接水的量以及排队的顺序
    for (i = 0; i < n; i++) {
        scanf("%d", &ren[i]);
    }

    while (1) {
        for (k = 0; k < m; k++) {
            if (bookWater[k] == 0) { // 判断第k位置水龙头是否空闲
                bookWater[k] = 1; // 标记第k位置水龙头被占用
                for (j = 0; j < n; j++) {
                    if (bookRen[j] == 0) { // 判断是否已经第j人是否已经接过水了
                        bookRen[j] = 1; // 标记第j人已经加过水了

                        a[k] = ren[j]; // 记录需要接水的水量
                        renCnt += 1; // 需要节水的人数加1
                        break;
                    }
                }
            }
        }

        // 寻找数组中的最少值
        min = 99999;
        for (i = 0; i < m; i++) {
            if (a[i] > 0 && min > a[i]) {
                min = a[i];
            }
        }

        /*
        printf("\n\n");
        printf("开始计算接水时间...\n");
        printf("最少节水量:%d\n", min);
        printf("------------------------\n");
        for (i = 0; i < m; i++) {
            printf("第%d人还需节水%d\n", i, a[i]);
        }
        printf("------------------------\n");
        */
        // 开始计算接水时间
        // 因为已经找到最小值了，就可以直接减去最小值，就是用掉的时间
        
        timeCnt += min; // 数组中最少接水所需用的时间
        //printf("需要换人接水拉!当前用时:%d\n", timeCnt);

        for (i = 0; i < m; i++) {
            if (a[i] > 0) {
                a[i] -= min;
                if (a[i] == 0) 
                    bookWater[i] = 0; // 已经接满的水龙头置空闲
            }
            //printf("第%d人还需节水%d\n", i, a[i]);
        }

        // 如果水龙上接水的人数是0；就表示所有人都已经接满水了
        flag = 1;
        for (i = 0; i < m; i++) {
            if (a[i] > 0) {
                flag = 0;
                break;
            }
        }
        
        // 判断水龙头是否有接水的人，同时需要判断所有人是否都记录过
        if (flag == 1 && renCnt == n) {
            break;
        }
    }

    printf("%d\n", timeCnt);
    return 0;
}
