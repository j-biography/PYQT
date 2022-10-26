# 박스 레이아웃

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        # 2개의 버튼 생성

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1) # 수평박스(QHBoxLayout)를 생성하고, 2개의 버튼과 빈 공간(addStretch)을 추가한다.

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1) # 수직박스(QVBoxLayout)를 생성하고, 수평박스(QHBoxLayout = hbox)를 넣어준다.

        self.setLayout(vbox) # 수직박스를 창의 메인 레이아웃으로 설정.

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
        
        