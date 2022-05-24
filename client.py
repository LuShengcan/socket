from socket import *
from threading import Thread
from time import sleep
from utils import *
import tkinter as tk

heartBeatCount = 0  # 心跳包计数
dataBuf = bytes()   # 接收数据缓冲区
nicknameOrMsg = 0


# 心跳包发送
def sendHeartBeat(client:socket):
    global heartBeatCount
    while 1:
        client.send(packData(HEART_BEAT_PACKAGE, 'ping'))
        heartBeatCount += 1
        if heartBeatCount > 3:
            print('ERROR: heart beat error, start to reconnect')
        sleep(0.5)

# 消息接收
def msgReceive(dataBuf:bytes, client:socket):
    global heartBeatCount
    while 1:
        data = client.recv(1024)
        if data:
            dataBuf += data
        while len(dataBuf) > HEADSIZE:
            header = unpack('!3i', dataBuf[:HEADSIZE])
            versionNum = header[0]
            msgType = header[1]
            bodyLen = header[2]
            if len(dataBuf) < HEADSIZE + bodyLen:
                break

            if msgType == HEART_BEAT_PACKAGE:
                heartBeatCount -= 1
            elif msgType == MSG or msgType == LOG_IN:
                msg = dataBuf[HEADSIZE:bodyLen+HEADSIZE].decode('utf-8')
                print(msg)
            else:
                print('default')
            dataBuf = dataBuf[HEADSIZE+bodyLen:]

# 消息发送
def msgSend(client:socket):
    global nicknameOrMsg
    while 1:
        if nicknameOrMsg == 0:
            nickname = input()
            client.send(packData(LOG_IN, nickname))
            nicknameOrMsg = 1
        else:
            msg = input()
            client.send(packData(MSG, msg))

def connect(host, port):
    host = HOST
    port = PORT
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((host, port))

    Thread(target=sendHeartBeat, args=(client,)).start()
    Thread(target=msgReceive, args=(dataBuf, client)).start()
    Thread(target=msgSend, args=(client,)).start()

if __name__ == '__main__':

    rootWindow = tk.Tk()
    rootWindow.title("client")
    rootWindow.geometry('300x300')

    ip_label = tk.Label(rootWindow, text='服务器 ip 地址', width=1, height=1)
    ip_label.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)
    ip_entry = tk.Entry(rootWindow)
    ip_entry.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.1)

    port_label = tk.Label(rootWindow, text='端口号', width=1, height=1)
    port_label.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)
    port_entry = tk.Entry(rootWindow)
    port_entry.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.1)

    connect_bt = tk.Button(rootWindow, text='Connect', command = lambda: connect(ip_entry.get(), port_entry.get()))
    connect_bt.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

    rootWindow.mainloop()
