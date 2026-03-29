from threading import Thread

import wx
from socket import *


class MyClientFrame(wx.Frame):
    def __init__(self, username):
        super().__init__(None, 100, f'{username}的客户端', wx.DefaultPosition, (400, 520))
        pl = wx.Panel(parent=self)

        # 创建一个可伸缩的网格布局器
        fg = wx.FlexGridSizer(wx.HORIZONTAL)
        # 创建2个按钮，并且把三2按钮按照水平的网格布局，看成一个整体
        connect_button = wx.Button(pl, size=(200, 40), label='进入聊天室')
        leave_button = wx.Button(pl, size=(200, 40), label='离开聊天室')
        fg.Add(connect_button, 0, wx.ALL)
        fg.Add(leave_button, 0, wx.ALL)

        # 创建一个只读的文本框，显示聊天记录
        self.log_text = wx.TextCtrl(pl, size=(400, 260), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 创建一个可以输入内容的文本框，显示聊天记录
        self.input_text = wx.TextCtrl(pl, size=(400, 140), style=wx.TE_MULTILINE)

        # 创建一个可伸缩的网格布局器
        fg2 = wx.FlexGridSizer(wx.HORIZONTAL)
        # 创建2个按钮，并且把三2按钮按照水平的网格布局，看成一个整体
        clear_button = wx.Button(pl, size=(200, 40), label='重置')
        send_button = wx.Button(pl, size=(200, 40), label='发送')
        fg2.Add(clear_button, 0, wx.ALL)
        fg2.Add(send_button, 0, wx.ALL)

        # 创建一个box布局
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(fg, 1, wx.ALIGN_CENTER)  # 三个按钮居中对齐
        box.Add(self.log_text, 1, wx.ALIGN_CENTER)
        box.Add(self.input_text, 1, wx.ALIGN_CENTER)
        box.Add(fg2, 1, wx.ALIGN_CENTER)
        pl.SetSizer(box)

        # 给按钮添加鼠标点击事件：
        self.Bind(wx.EVT_BUTTON, source=connect_button, handler=self.connect_server)
        self.Bind(wx.EVT_BUTTON, source=send_button, handler=self.send_message)
        self.Bind(wx.EVT_BUTTON, source=leave_button, handler=self.leave)

        # 给当前对象的属性赋值
        self.username = username
        self.is_on = None

    def connect_server(self, event):
        """客户端连接服务器，并且把自己的用户名发送给服务端"""
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 8080))
        # 连接成功之后，马上把自己的用户发送给服务器端
        self.client_socket.send(self.username.encode('utf8'))
        self.is_on = True  # 表示客户端用户在聊天室

        t = Thread(target=self.recv_data)
        t.daemon = True
        t.start()

    def recv_data(self):
        """
        专门负责：在客户端接收消息的函数
        第一步：接收到服务器的消息
        第二步：把消息展示到客户端的只读文本框中
        """
        while self.is_on:
            message = self.client_socket.recv(1024).decode('utf8')
            if message == 'zhf^leave^zhf':
                self.is_on = False
            else:
                self.log_text.AppendText(message)
                self.log_text.AppendText('-' * 50 + '\n')

        self.client_socket.close()
        self.client_socket = None

    def send_message(self, event):
        """
        负责发送聊天信息到聊天室
        :param event:
        :return:
        """
        if self.is_on:
            message = self.input_text.GetValue()    # 获取输入文本框中的内容，并且去掉首尾空格
            if message:
                self.client_socket.send(message.encode('utf8'))
                self.input_text.SetValue('')

    def leave(self, event):
        """
        客户端离开聊天室
        规定： 1. 当客户端发送 zhf^leave^zhf ~ 就代表客户端马上要离开了 2. 服务器也要发送同样的消息，客户端收到之后确认离开（为了不让recv函数阻塞住）
        1. 客户端窗口不关闭
        2. 客户端的线程要结束，socket要关闭
        :param event:
        :return:
        """
        # self.is_on = False
        self.client_socket.send('zhf^leave^zhf'.encode('utf8'))
        pass

if __name__ == '__main__':
    username = input('请输入用户名:')
    # wx库中所有的函数都是大写字母开头
    app = wx.App()
    # 创建一个窗口
    frame = MyClientFrame(username)  # 父窗口名称，窗口id，窗口标题
    frame.Show(True)  # 默认值是True
    app.MainLoop()
