//
//  main.c
//  C_TypeWordGame
//
//  Created by 陆杨 on 09/11/2017.
//  Copyright © 2017 陆杨. All rights reserved.
//

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


/***************初始化***************/
//设计字母，子弹

//游戏角色初始化
void do_initGame();


/***************功能函数***************/
//定位到屏幕的某个位置
void do_gotoxy(int x, int y) {
}


//获取随机数
//获取0_1之间的随机数
void do_getRandom_0_1(){
    int i;
    srand( (unsigned)time( NULL ) );
    for( i = 0; i < 10;i++ ) {
        printf( " %5.2f\n", rand()*1.0f/(INT32_MAX));
    }
    //INT32_MAX: -214748364~2147483647
}

//获取1_100之间的随机数
void do_getRandom_1_100(){
    int i;
    srand( (unsigned)time( NULL ) );
    for( i = 0; i < 10;i++ ) {
        printf( " %d\n", (rand()%100) + 1);
    }
}

//获取n_m之间的随机数
void do_getRandom_n_m(int n, int m){
    int i;
    srand( (unsigned)time( NULL ) );
    for( i = 0; i < 10; i++ ) {
        printf( " %d\n", (rand()%(m-n+1)) + n);
    }
}

//end 获取随机数


int main(int argc, const char * argv[]) {
    
//    int i_random = do_getRandom();
//    printf("random:%d\n", i_random);
    
//    for (int i = 0; i < 10; i++)
//    {
//        int i_random = do_getRandom();
//        sleep(0.5);
//        printf("random:%d\n", i_random);
//    }
    unsigned int max_int = 0-1;
    
    printf("The max value of unsigned int on 32 machine: %u\n", max_int);
    printf("The max value of unsigned int on 32 machine: %d\n", INT32_MAX);
    printf("The max value of unsigned int on 32 machine: %lld\n", INT64_MAX);
    printf("The max value of unsigned int on 32 machine: %d\n", INT16_MAX);
    

    do_getRandom_0_1();
    do_getRandom_1_100();
    do_getRandom_n_m(100,200);
    
    system("pause");
    // insert code here...
    printf("Hello, World!\n");
    return 0;
}



