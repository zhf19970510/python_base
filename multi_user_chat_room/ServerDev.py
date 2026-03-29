import time
from threading import Thread

import wx
from socket import *


class MyServerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, 100, 'zhf的服务器', wx.DefaultPosition, (515, 580))
        pl = wx.Panel(parent=self)

        # 创建一个可伸缩的网格布局器
        fg = wx.FlexGridSizer(wx.HORIZONTAL)
        # 创建3个按钮，并且把三个按钮按照水平的网格布局，看成一个整体
        start_server_button = wx.Button(pl, size=(170, 45), label='启动服务')
        save_log_button = wx.Button(pl, size=(170, 45), label='保存聊天记录')
        stop_server_button = wx.Button(pl, size=(170, 45), label='停止服务')
        fg.Add(start_server_button, 0, wx.ALL)
        fg.Add(save_log_button, 0, wx.ALL)
        fg.Add(stop_server_button, 0, wx.ALL)

        # 创建一个只读的文本框，显示聊天记录
        self.read_text = wx.TextCtrl(pl, size=(513, 535), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 创建一个box布局
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(fg, 1, wx.ALIGN_CENTER)  # 三个按钮居中对齐
        box.Add(self.read_text, 1, wx.ALIGN_CENTER)
        pl.SetSizer(box)

        # 给按钮添加鼠标点击事件：
        self.Bind(wx.EVT_BUTTON, source=start_server_button, handler=self.start_server)
        self.Bind(wx.EVT_BUTTON, source=save_log_button, handler=self.save_log_to_file)

        # 定义对象属性
        # 每一个客户端都有一个与之对应的线程
        self.client_dict = {}  # 聊天室中的所有客户端用户，把用户名作为key，把一个线程对象作为value

    def start_server(self, event):
        """点击启动按钮，开始启动Socket服务器"""
        self.server_socket = socket(AF_INET, SOCK_STREAM)  # 采用TCP协议
        self.server_socket.bind(('', 8080))
        self.server_socket.listen(5)

        # 创建一个子线程，让子线程调用accept, 子线程在阻塞等待客户端的连接
        self.server_thread = Thread(target=self.server_work)
        self.server_thread.daemon = True
        self.server_thread.start()

    def server_work(self):
        print('服务器开始启动，准备接收客户端的连接')
        """服务器已经启动，开始等待客户端（无限个）的连接：多人聊天室"""
        while True:
            # 当有一个客户端连接之后，返回session_socket
            # session_socket 负责和当前的客户端进行连接通信。每一个客户端都有一个与之对应的session_socket
            session_socket, client_addr = self.server_socket.accept()

            username = session_socket.recv(1024).decode('utf8')

            # 创建一个和客户端用户对应的线程
            t1 = SessionThread(username, session_socket, self)
            self.client_dict[username] = t1  # 把当前客户端用户的线程，存放到字典中
            t1.start()

            welcome_message = f'服务器通知：欢迎{username}进入聊天室！'
            self.show_message_and_send_message(welcome_message)

    def show_message_and_send_message(self, message):
        """
        专门负责，在服务器端，显示客户端的信息，并且发送信息给客户端
        第一步：把信息展示在服务器端的只读文本框中
        第二步：把信息发送给所有的客户端
        :param message:
        :return:
        """
        # 得到当前系统时间
        current_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
        full_message = f'{message}\n时间：{current_datetime}\n'
        self.read_text.AppendText(full_message)
        self.read_text.AppendText('-' * 60 + '\n')

        # 把信息发送给所有的客户端（用户）
        for client_thread in self.client_dict.values():
            if client_thread.isOn:  # 表示客户端用户还在聊天室
                # 发送通知信息到客户端
                client_thread.session_socket.send(full_message.encode('utf8'))

    def remove_client(self, username):
        """
        有一个客户端要离开聊天室，所以需要把它对应的线程从字典中删除
        :param username:
        :return:
        """
        if username in self.client_dict:
            self.client_dict.pop(username)

    def save_log_to_file(self, event):
        """
        保存所有的聊天记录到文件中，
        规则：每次保存的文件名是：log-当前时间.txt
        :param event:
        :return:
        """
        file_name = f'log-{time.strftime("%Y%m%d%H%M%S")}.txt'
        log_data = self.read_text.GetValue()
        with open(file_name, 'w', encoding='utf8') as f:
            f.writelines(log_data)


class SessionThread(Thread):
    """每一个客户端都有一个与之对应的线程"""

    def __init__(self, username, session_socket: socket, server_frame: MyServerFrame):
        super().__init__()
        self.session_socket = session_socket
        self.username = username
        self.isOn = True  # 客户端用户还在聊天室，可以控制线程的结束
        self.server_frame = server_frame

    def run(self):
        while self.isOn:
            # 接收该客户端用户 发送过来的聊天信息
            recv_message = self.session_socket.recv(1024).decode('utf8')
            if recv_message == 'zhf^leave^zhf':
                # 表示当前客户端要离开聊天室了
                self.isOn = False
                # 服务器给客户端发送了一条离开的确认消息
                self.session_socket.send('zhf^leave^zhf'.encode('utf8'))
                leave_message = f'服务器通知：{self.username} 离开聊天室！'
                self.server_frame.show_message_and_send_message(leave_message)
                # 还要把字典中存放当前客户端的数据删除
                self.server_frame.remove_client(self.username)
            else:
                self.server_frame.show_message_and_send_message(f'{self.username}: {recv_message}')

        self.session_socket.close()
        self.session_socket = None


if __name__ == '__main__':
    # wx库中所有的函数都是大写字母开头
    app = wx.App()
    # 创建一个窗口
    frame = MyServerFrame()  # 父窗口名称，窗口id，窗口标题
    frame.Show(True)  # 默认值是True
    app.MainLoop()
