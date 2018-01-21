# Author: Jason Lu
# 支持多用户连接的一个socket server
import socketserver

# 保存用户列表
list_users = []
def do_initUsers():
    with open("user", "r", encoding="utf-8") as f_users:
        for data_user in f_users:
            data = data_user
            list_users.append(eval(data))
            print(list_users)


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        self.request.sendall(self.data.upper())

    def setup(self):
        # 如果有新连接出来就发送提示消息
        print("有新request:", self.request)
        data_msg = '欢迎登陆服务器,请输入用户名和密码:'
        self.request.sendall(data_msg.encode("utf-8"))



    # 使用发射


if __name__ == '__main__':
    # do_initUsers()


    HOST, POST = "localhost", 6969
    print("开始启动socket server...")
    server = socketserver.ThreadingTCPServer((HOST, POST), MyTCPHandler)
    server.serve_forever()
