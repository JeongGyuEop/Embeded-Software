import sys
from PySide2 import QtCore, QtWidgets, QtUiTools

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # QApplication 인스턴스 생성
    loader = QtUiTools.QUiLoader()  # QUiLoader 인스턴스 생성
    ui = loader.load('./hello.ui')  # UI 파일 로드
    ui.show()  # 로드된 UI 보이기
    sys.exit(app.exec_())  # 애플리케이션 실행 및 종료 이벤트 처리

