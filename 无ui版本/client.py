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

if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('192.168.1.104', PORT))
    Thread(target=sendHeartBeat, args=(client,)).start()
    Thread(target=msgReceive, args=(dataBuf, client)).start()
    Thread(target=msgSend, args=(client,)).start()
