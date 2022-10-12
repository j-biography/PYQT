
import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500,500)
        self.center() # center() 메서드를 통해 창이 화면의 가운데에 위치하게 함.
        self.show()

    def center(self): # center() 메서드 생성
        qr = self.frameGeometry() # frameGeometry() 메서드를 통해 self(어플리케이션 창)의 위치와 크기 정보를 가져옴.
        cp = QDesktopWidget().availableGeometry().center() # QDesktopWidget().availableGeometry().center() 메서드를 통해 내 모니터의 가운데 위치를 파악.
        qr.moveCenter(cp) # qr(어플리케이션 창의 좌표)의 직사각형 위치를 cp(내 모니터) 중심으로 이동.
        self.move(qr.topLeft()) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())    

    