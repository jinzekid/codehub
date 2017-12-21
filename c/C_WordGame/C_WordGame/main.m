//
//  main.m
//  C_WordGame
//
//  Created by 陆杨 on 09/11/2017.
//  Copyright © 2017 陆杨. All rights reserved.
//

#import <Cocoa/Cocoa.h>

#include <stdio.h>
#include <stdlib.h>

/***************初始化***************/
//设计字母，子弹

//游戏角色初始化
void do_initGame();

/***************功能函数***************/
//定位到屏幕的某个位置
void do_gotoxy(int x, int y) {
    
    
}

int main(int argc, const char * argv[]) {
    
    int* p = 4;
    printf("sizeof p: %d\n", sizeof(int *));
    
    system("pause");

    // insert code here...
    printf("Hello, World!\n");
    return NSApplicationMain(argc, argv);
}
