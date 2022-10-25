# 시그널 & 슬롯
# 시그널은 특정 신호, 슬롯은 시그널에 어떻게 반응할지를 구현한 메서드를 뜻함.

import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__() 
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display) 
        # dial.valueChanged 와 lcd.display를 서로 연결한다. 
        # dial은(sender : 전송자), lcd는(receiver : 수신자)이다.

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())