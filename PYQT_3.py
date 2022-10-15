# 툴팁 생성

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QIcon


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      QToolTip.setFont(QFont('SanSerif', 10)) # 툴팁에 사용될 폰트와 폰트크기를 설정.
      self.setToolTip('This is a <b>QWidget</b> widget') # 위젯 전체(self)에 툴팁을 만들어 줌. 표시될 텍스트 입력


      btn = QPushButton('Quit', self)
      btn.setToolTip('This is a <b>Quit</b> widget')
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)

      
      btn2 = QPushButton('Button', self)
      btn2.setToolTip('This is a <b>Button</b> widget')
      btn2.move(150, 150)
      btn2.resize(btn.sizeHint())

      self.setWindowTitle('Quit Button')
      self.setWindowIcon(QIcon('instagram_logo.jfif'))
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())