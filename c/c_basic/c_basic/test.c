//
//  test.c
//  c_basic
//
//  Created by 陆杨 on 2018/10/25.
//  Copyright © 2018 陆杨. All rights reserved.
//

#include <stdio.h>

#define LEN 32
typedef struct letter {
    char c;
    int cnt;
}*pChar;
struct letter characters[LEN]= {{',',0},{' ',0},{'{',0},{'}',0},{'"', 0},{':',0},{'a',0},{'b',0},{'c',0},{'d',0},{'e',0},{'f',0},{'g',0},{'h',0},{'i',0},{'j',0},{'k',0},{'l',0},{'m',0},{'n',0},{'o',0},{'p',0},{'q',0},{'r',0},{'s',0},{'t',0},{'u',0},{'v',0},{'w',0},{'x',0},{'y',0},{'z',0}};

struct node {
    int weight;
    pChar left;
    pChar right;
};

/**
 * 打印数字的二进制形式
 */
void printBit(int i) {
    printf("\t二进制:\t");
    int r = i;
    int list[16];   //用来存储 & （and位）操作结果 不同的机器环境中 int 类型占 8bit 或 16bit、32bit
    int j;          //用来for循环计数 和 list 数组下标操作
    int mask = 1;   //用来 和 任意int进行 & bit操作，为什么要用 mask=1,而不是其他的数据
    // 因为1 的二级制是 00000000 00000001
    // 00000000 00000001 和 任意 二进制进行 & bit 操作时，只有低位为1时 结果为1 利用这一特点
    // 可以对任意 int 进行移位 操作使得 int 二进制中的所有位
    // 与 00000000 00000001 进行比较推算二进制 位的值 是0 还是1
    
    
    for (int j = 0; j < 16; j++) {
        if (i & mask == 1) {    //bit & 比较
            list[j] = 1;        //结果放到 list 数组中
        } else {
            list[j] = 0;        //结果放到 list 数组中
        }
        i=i>>1;                 // 右移bit 1次
    }
    
    //反向打印 数组
    //为什么要反向打印？
    //因为 我们进行 bit 比较的时候 第一次比较存储的结果是 最低位（最右边的bit）
    //最后一次比较存储的结果是 最高位（最左边的bit）
    //由于pirntf 打印函数是从左向右排列显示的 若果正向打印 会先打印最先存储的 最低位（最右边的bit）；显示到最 左边了 （说明:X86计算机 约定低位在最右边）
    //这和计算机实际的位是反向的 所以我们反向打印 就可把最低位排列到最右边了
    
    for (int j = 15; j >= 0; j--) {
        printf("%d", list[j]);
    }
    printf("\t 的十进制值：%d\t", r);
    //    printf("\n");
}


int main_test(int argc, const char * argv[]) {
    // insert code here...
    int i, size;
    char buf[1024];
    FILE *fp = NULL;
    
    int v = 5;
    char c = 'a';
    printBit(c);
    
    
    fp = fopen("/Users/jasonlu/Desktop/Dev/GitHub/codehub/c/c_basic/c_basic/txt.txt", "r");
    if (fp == NULL){
        printf("fp==null\n");
        return -1;
    }
    
    for (i = 0; i < LEN; i++) {
        printf("(%c, %d) ", characters[i].c, characters[i].cnt);
    }
    printf("\n");
    
    fgets(buf, 1024, fp);
    
    // 第一遍扫描字符串
    size = strlen(buf);
    char *tmp = NULL;
    tmp = buf;
    int k = 0;
    while (k <= size) {
        for (i = 0; i < LEN; i++) {
            if (*tmp == characters[i].c) {
                characters[i].cnt++;
                break;
            }
        }
        tmp++;
        k++;
    }

    for (i = 0; i < LEN; i++) {
        printf("(%c, %d) ", characters[i].c, characters[i].cnt);
    }
    printf("\n");
    
    printf("\nlength=%d\n", strlen(buf));
    
    
    
    fclose(fp);
    
    printf("Hello, World!\n");
    return 0;
}
