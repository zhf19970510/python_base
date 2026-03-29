from socket import socket as Socket
import socket


# 创建一个UDP的socket对象
client_socket = Socket(socket.AF_INET, socket.SOCK_DGRAM)

# 客户端的socket是不需要bind。所以由操作系统分配一个随机的端口号

while True:
    # 发送数据给服务端
    send_msg = input('客户端>>')

    if send_msg == 'quit':  # 如果客户端输入quit表示退出聊天
        # quit发给服务器，然后客户端退出循环
        client_socket.sendto(send_msg.encode('utf8'), ('192.168.101.10', 6666))
        break

    client_socket.sendto(send_msg.encode('utf8'), ('192.168.101.10', 6666))

    msg, addr = client_socket.recvfrom(1024)

    print(f'来自服务端IP:{addr[0]},端口号:{addr[1]}的消息：{msg}')

# 关闭
client_socket.close()