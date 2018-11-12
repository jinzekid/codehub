//
//  commonHeader.h
//  c_basic
//
//  Created by 陆杨 on 2018/9/16.
//  Copyright © 2018 陆杨. All rights reserved.
//

#ifndef commonHeader_h
#define commonHeader_h

typedef int status;
typedef int boolean;

#define TRUE    1
#define FALSE   0
#define OK      1
#define ERROR   0
#define INFEASIBLE -1

// 普通操作
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <string.h>
#include <strings.h>
#include <time.h>
#include <errno.h>
#include <ctype.h>
#include <math.h>

// 文件与目录操作
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <dirent.h>

// 进程间通信
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include <sys/msg.h>
#include <sys/wait.h>
#include <semaphore.h>
#include <signal.h>

// 线程
#include <pthread.h>

// 网络
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>

#endif /* commonHeader_h */

// 常用宏定义
#define MAX(x, y) (((x) > (y)) ? (x):(y))
#define MIN(x, y) (((x) < (y)) ? (x):(y))

#define DECCHK(c) ((c) >= '0' && (c) <= '9')
#define UPCASE(x) (((c) >= 'a' && (c) <= 'z') ? ((c) - 0x20) : (c))
#define LOWCASE(x) (((c) >= 'A' && (c) <= 'Z') ? ((c)|0x20) : (c))

#define ARR_SIZE(x) (sizeof((a))/sizeof((a[0])))

// 定义是否需要输出打印信息
#ifdef DEBUG
#define OneArgument(a); printf(a);printf("%d%d",__LINE__,__FILE__); 
#define TwoArguments(a, b); printf(a, b);printf("%d%d",__LINE__,__FILE__);
#else
#define OneArgument(a) ;
#define TwoArguments(a, b) ;
#endif
 
#define GetMacro(_1, _2, NAME, ...) NAME
#define PRINT(...) GetMacro(__VA_ARGS__, TwoArguments, OneArgument, ...)(__VA_ARGS__)



