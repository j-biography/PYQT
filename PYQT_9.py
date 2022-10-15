# 절대적 배치

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(30,27)

        label2 = QLabel('Label2', self)
        label2.move(30,67)

        btn1 = QPushButton('Button1', self)
        btn1.move(100,20)

        btn2 = QPushButton('Button2', self)
        btn2.move(100,60)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
