# 사용자 정의 시그널 생성 + btn과 시그널 연결

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Signal(QObject):

    closeApp = pyqtSignal()

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Signal()
        self.c.closeApp.connect(self.close)

        btn1 = QPushButton('EXIT', self)
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)

        btn1.clicked.connect(self.c.closeApp)

        self.setLayout(vbox)
        self.setWindowTitle('Personal Emitting Signal')      
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# ------------ 원문은 아래에


import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):

    closeApp = pyqtSignal() # pyqtSignal()을 활용하여 새로운 closeApp 시그널을 생성. 본 시그널은 마우스 클릭시 발생하며, QMainWindow의 close() 슬롯에 연결되어 프로그램을 종료.

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self):
        self.c.closeApp()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())