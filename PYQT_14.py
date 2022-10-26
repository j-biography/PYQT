# 이벤트 핸들러 = 슬롯(시그널을 받아서 이벤트를 발생시키는 메서드)
# 이미 정의되어 있는 이벤트 핸들러를 사용해 보는 챕터.


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, A):
        if A.key() == Qt.Key_Backspace: # 백스페이스 키를 입력하면 close 명령이 실행.
            self.close()
        elif A.key() == Qt.Key_F: # F 키를 입력하면 창 최대화 명령이 실행.
            self.showFullScreen()
        elif A.key() == Qt.Key_N: # N 키를 입력하면 창 원상태화 명령이 실행.
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

