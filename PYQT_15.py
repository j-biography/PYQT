# 이벤트 핸들러 챕터 2.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 0
        y = 0

        self.text = 'x value:{0}, y value:{1}'.format(x, y) # format(x,y)에서 첫번째 항목을 {0}으로 불러오고, 두번째 항목을 {1}로 불러옴.
        self.label = QLabel(self.text, self)
        self.label.move(30, 30)

        self.setMouseTracking(True) # setMouseTracking을 켜지않으면, 마우스 버튼을 클릭했다가 뗄 때만 mouseEvent가 발생. (Default)

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mouseMoveEvent(self, A):
        x = A.x() # 현재 마우스 커서 위치(A)의 x값
        y = A.y() # 현재 마우스 커서 위치(A)의 y값

        text = 'x value:{0}, y value:{1}'.format(x, y)
        self.label.setText(text)
        self.label.adjustSize() # 라벨의 크기를 자동으로 조절하게 함.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())