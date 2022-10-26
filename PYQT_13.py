# 시그널 & 슬롯 제작 ver2


import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Small', self)

        hbox = QHBoxLayout() # 가로로 버튼을 배열
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout() # 세로로 버튼을 배열
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)

        self.setLayout(vbox) # vbox를 창의 메인 레이아웃으로 설정(기준점)

        dial.valueChanged.connect(lcd.display) # dial.valueChanged 시그널을 lcd.display와 연결하여 하나의 슬롯(메서드)을 생성
        btn1.clicked.connect(self.resizeBig) # btn1.clicked 시그널을 resizeBig 메서드와 연결하여 슬롯 생성
        btn2.clicked.connect(self.resizeSmall) # btn2.clicked 시그널을 resizeSmall 메서드와 연결하여 슬롯 생성

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def resizeBig(self):
        self.resize(400, 500)

    def resizeSmall(self):
        self.resize(200, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())