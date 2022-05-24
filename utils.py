from socket import socket
from struct import *

LOG_IN = 0   # 客户端与服务器之间的登录包
HEART_BEAT_PACKAGE = 1    # 客户端心跳包
MSG = 2     # 客户端发送信息
BROADCAST = 3 # 服务端广播包

HOST = '127.0.0.1'
PORT = 10086

VERSION_NUM = 0   # 版本号
HEADSIZE = 12


def packData(msgType:int, msg:str = ''):
    bodyLen = len(msg.encode('utf-8'))
    header = [VERSION_NUM, msgType, bodyLen]
    headPack = pack('!3i', *header) # ！代表网络字节序，3i代表传入三个int，*header功能是将列表的每个元素作为一个单独的参数传入函数
    return headPack + msg.encode('utf-8')

def sendData(to:socket, package:bytes):
    to.send(package)

def unpackData(pack):
    pass