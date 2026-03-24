from socket import socket as Socket
import socket
# 实现，客户端和服务器的即时聊天

# 创建一个UDP的socket对象
server_socket = Socket(socket.AF_INET, socket.SOCK_STREAM)

# IP:192.168.101.66，其他主机可以和当前服务器通信
# IP:127.0.0.1，其他的主机不可以和当前的服务器通信，除非客户端也在本地
# IP:''，该服务端绑定到所有的IP上
# server_socket.bind(('192.168.101.10', 6666))
server_socket.bind(('', 6666))
while True:
    print(server_socket)
    # 包括ip地址和端口号，msg是收到的数据，addr是源地址和端口号
    msg, addr = server_socket.recvfrom(1024)   # 最大一次接收数据量: 1KB

    if msg.decode('utf8') == 'quit':        # 表示终止聊天
        break

    # decode 函数可以把字节数据转换为字符串
    print(f'来自客户端IP:{addr[0]},端口号:{addr[1]}的消息：{msg.decode("utf8")}')

    # 服务端也可以发送数据到客户端
    send_msg = input('服务端>>')
    # sendto 发送的数据不能是字符串，只能是字节数据，字符串的encode函数
    server_socket.sendto(send_msg.encode('utf8'), addr)

server_socket.close()
