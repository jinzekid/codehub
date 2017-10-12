//
//  socket_tcp.c
//  CProject
//
//  Created by 陆杨 on 25/09/2017.
//  Copyright © 2017 陆杨. All rights reserved.
//

//socket tcp服务器
#include <fcntl.h>
#include <errno.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define SERVER_PORT 5556


int main(){
    
    int code;
    //调用socket函数返回的文件描述符
    int serverSocket = 0; // 服务器端
    int clientSocket = 0; // 客户端

    //声明两个套接字sockaddr_in结构体变量，分别表示客户端和服务器
    struct sockaddr_in server_addr;
    struct sockaddr_in clientAddr;
    
    int addr_len = sizeof(clientAddr);
    char buffer[200];
    ssize_t iDataNum;
    
    
    //int socket(int domain, int type, int protocol);
    //第一个参数表示使用的地址类型，一般都是ipv4，AF_INET
    //第二个参数表示套接字类型：tcp：面向连接的稳定数据传输SOCK_STREAM
    //第三个参数设置为0
    if ((serverSocket = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        code = 1;
        goto ENDSOCKET;
    }
    
    bzero(&server_addr, sizeof(server_addr));
    //初始化服务器端的套接字，并用htons和htonl将端口和地址转成网络字节序
    server_addr.sin_family = AF_INET;
    server_addr.sin_port   = htons(SERVER_PORT);
    
    //ip可是是本服务器的ip，也可以用宏INADDR_ANY代替，代表0.0.0.0，表明所有地址
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    
    //对于bind，accept之类的函数，里面套接字参数都是需要强制转换成(struct sockaddr *)
    //bind三个参数：服务器端的套接字的文件描述符，
    //int	bind(int, const struct sockaddr *, socklen_t) __DARWIN_ALIAS(bind);
    if (bind(serverSocket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0){
        code = 2;
        goto ENDSOCKET;
    }
    
    //设置服务器上的socket为监听状态
    if (listen(serverSocket, 5) < 0){
        code = 3;
        goto ENDSOCKET;
    }
    
    while (1) {
        
        printf("Listening on port: %d\n", SERVER_PORT);
        //调用accept函数后，会进入阻塞状态
        //accept返回一个套接字的文件描述符，这样服务器端便有两个套接字的文件描述符，
        //serverSocket和client。
        //serverSocket仍然继续在监听状态，client则负责接收和发送数据
        //clientAddr是一个传出参数，accept返回时，传出客户端的地址和端口号
        //addr_len是一个传入-传出参数，传入的是调用者提供的缓冲区的clientAddr的长度，以避免缓冲区溢出。
        //传出的是客户端地址结构体的实际长度。
        //出错返回-1
        
        clientSocket = accept(serverSocket, (struct sockaddr *)&clientAddr, (socklen_t *)&addr_len);
        if (clientSocket < 0) {
            code = 4;
            goto ENDSOCKET;
        }
        
        
        //向客户端发送数据
        //char str[] = "Hello World!";
        //send(clientSocket, str, sizeof(str) , 0);
        
        printf("\nrecv client data...n");
        //inet_ntoa   ip地址转换函数，将网络字节序IP转换为点分十进制IP
        //表达式：char *inet_ntoa (struct in_addr);
        printf("IP is %s\n", inet_ntoa(clientAddr.sin_addr));
        printf("Port is %d\n", htons(clientAddr.sin_port));
        
        int isClose = 0;
        //char sendbuf[200];

        while (1) {
            
            iDataNum = recv(clientSocket, buffer, 1024, 0);
            if (iDataNum < 0) {
                perror("recv error.");
                continue;
            }
            printf("buffer=%s,iDataNum=%d\n", buffer , iDataNum);

            buffer[iDataNum] = '\0';
            printf("222 buffer=%s\n", buffer);

            if (strcmp(buffer, "quit") == 0) {
                isClose = -1;
                break;
            }
            
            printf("%ld recv data is %s\n", iDataNum, buffer);
            
            
            
            
            send(clientSocket, buffer, iDataNum, 0);
            
            
//            printf("Input your to client:>");
//            scanf("%s", sendbuf);
//            printf("\n");
//            send(clientSocket, sendbuf, strlen(sendbuf), 0);
        }
    }
    
    
ENDSOCKET:
    if (code == 1) {
        perror("socket init error.");
    }
    else if (code == 2) {
        perror("connect error.");
    }
    else if (code == 3) {
        perror("listen error.");
    }
    else if (code == 4) {
        perror("accept error.");
    }

    // 关闭套接字
    close(serverSocket);
    close(clientSocket);
    
    return code;
}
