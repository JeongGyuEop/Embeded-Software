#!/usr/bin/env python3
import sys
import signal
import random
from PySide2 import QtCore, QtNetwork

class Server(QtNetwork.QTcpServer):
    def __init__(self, parent=None):
        super(Server, self).__init__(parent)
        self.newConnection.connect(self.newClient)
        self.clients = {}

    def newClient(self):
        socket = self.nextPendingConnection()
        socket.readyRead.connect(self.readData)
        socket.disconnected.connect(self.disconnectClient)
        self.clients[socket] = {}
        self.clients[socket]["name"] = "손님-%d" % random.randint(1, 100)

    def disconnectClient(self):
        socket = self.sender()
        self.sendAll("<em>%s 님이 나가셨습니다.</em>" % self.clients[socket]["name"])
        self.clients.pop(socket)

    def readData(self):
        socket = self.sender()
        line = socket.readLine().data().decode("utf-8").strip()
        cmd, value = line.split(" ", 1)
        if cmd == "login":
            if self.Exist(value):
                name = self.clients[socket]["name"]
                self.send(socket, "<em>이름이 이미 존재합니다. 자동으로 설정합니다...</em>")
            else:
                name = value
                self.clients[socket]["name"] = name
                self.sendAll("<em>%s 님이 들어왔습니다.</em>" % name)
        elif cmd == "msg":
            message = "<%s> : %s" % (self.clients[socket]["name"], value)
            self.sendAll(message)

    def send(self, socket, message):
        socket.write(message.encode("utf-8"))

    def sendAll(self, message):
        for c in self.clients:
            self.send(c, message)

    def Exist(self, name):
        for c in self.clients.values():
            if name == c["name"]:
                return True
        return False

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtCore.QCoreApplication(sys.argv)
    serv = Server()
    port = 8080
    if not serv.listen(QtNetwork.QHostAddress.Any, port):
        print("Failed to start server")
        sys.exit(-1)
    print("The server is running with port %d" % port)
    sys.exit(app.exec_())

