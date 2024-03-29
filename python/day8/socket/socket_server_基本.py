# Author: Jason Lu

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        while True:
            # self.request is the TCP socket connected to the client
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)

                # 代表客户端断了,
                # 不用判断，直接用异常抓取
                # if not self.data:
                #     print("%s 断开了...." %(self.client_address[0]))
                #     break

                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print("e: %s" %(e))
                break

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
