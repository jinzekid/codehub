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
