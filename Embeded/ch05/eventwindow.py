#!/usr/bin/python3
import sys
from PySide2 import QtCore, QtGui, QtWidgets

class EventWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  # Python 3 스타일의 초기화
        self.setWindowTitle("Event Window")
        self.setGeometry(300, 300, 300, 300)
        self.points = []  # 클래스 변수 초기화 위치 수정

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mouseDoubleClickEvent(self, event):
        self.close()

    def mouseMoveEvent(self, event):
        print(f"x={event.x()}, y={event.y()}")  # Python 3 f-string 사용
        self.points.append((event.x(), event.y()))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)  # QPainter에 self (위젯) 전달
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 10, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))
        for p in self.points:
            painter.drawPoint(p[0], p[1])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ew = EventWindow()
    ew.show()
    sys.exit(app.exec_())

