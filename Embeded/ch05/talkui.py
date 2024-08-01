#!/usr/bin/env python3
import sys
from PySide2 import QtCore, QtWidgets, QtNetwork
from talk import Ui_TalkWindow
from connect import Ui_Dialog

class ConnectWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class TalkMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TalkMainWindow, self).__init__(parent)
        self.ui = Ui_TalkWindow()
        self.ui.setupUi(self)
        self.ui.connectButton.clicked.connect(self.connect)
        self.socket = QtNetwork.QTcpSocket(self)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)
        self.connectState = False

    def connect(self):
        if not self.connectState:
            cw = ConnectWindow()
            if cw.exec_() == QtWidgets.QDialog.Accepted:
                self.socket.connectToHost(cw.ui.server.text(), int(cw.ui.port.text()))
                if self.socket.waitForConnected(1000):
                    self.name = cw.ui.name.text()
                    self.send(f"login {self.name}")
                    self.ui.sendButton.clicked.connect(self.sendClick)
                    self.ui.messageEdit.returnPressed.connect(self.sendClick)
                    self.ui.messageEdit.setFocus()
                    self.ui.connectButton.setText("Disconnect")
                    self.connectState = True
        else:
            self.socket.disconnectFromHost()
            self.ui.connectButton.setText("Connect")
            self.connectState = False

    # 아래는 예시로 추가한 메서드들입니다. 실제 구현에 필요한 기능에 맞게 수정해주세요.
    def readData(self):
        # 서버로부터 데이터를 읽고 처리하는 로직 구현
        pass

    def displayError(self, socketError):
        # 연결 오류를 처리하는 로직 구현
        pass

    def sendClick(self):
        # 메시지 전송 버튼 클릭 시 처리하는 로직 구현
        pass

    def send(self, message):
        # 서버로 메시지를 전송하는 로직 구현
        pass

# 메인 이벤트 루프를 시작하는 부분
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = TalkMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

