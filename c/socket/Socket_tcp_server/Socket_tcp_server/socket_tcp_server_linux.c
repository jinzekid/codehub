//
//  socket_tcp_server_linux.c
//  Socket_tcp_server
//
//  Created by 陆杨 on 12/10/2017.
//  Copyright © 2017 陆杨. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define SERVER_PORT 5555

int main22(){
    
    //创建套接字
    int serv_sock;
    if ((serv_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP) < 0)) {
        perror("socket init error.");
        return 1;
    }
    
    //声明两个套接字sockaddr_in结构体变量，分别表示客户端和服务器
    struct sockaddr_in server_addr;
    struct sockaddr_in client_addr;
    
    // 初始化服务器的套接字
    memset(&server_addr, 0, sizeof(server_addr));
    //初始化服务器端的套接字，并用htons和htonl将端口和地址转成网络字节序
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    //ip可是是本服务器的ip，也可以用宏INADDR_ANY代替，代表0.0.0.0，表明所有地址
    server_addr.sin_addr.s_addr = inet_addr(INADDR_ANY);
    
    //对于bind，accept之类的函数，里面套接字参数都是需要强制转换成(struct sockaddr *)
    //bind三个参数：服务器端的套接字的文件描述符，
    //int    bind(int, const struct sockaddr *, socklen_t) __DARWIN_ALIAS(bind);
    if (bind(serv_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0){
        perror("connect error.");
        return 1;
    }
    
    //设置服务器上的socket为监听状态
    if (listen(serv_sock, 5) < 0){
        perror("listen error.");
        return 1;
    }
    
    
    socklen_t clent_addr_size = sizeof(client_addr);
    
    int client_sock = accept(serv_sock, (struct sockaddr *)&client_addr, (socklen_t *)&clent_addr_size);
    if (client_sock < 0) {
        perror("accept error.");
        return 1;
    }
    
    
    return 0;
}
