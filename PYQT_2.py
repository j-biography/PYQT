
import sys # 인터프리터를 동작시키는 모듈
import os # 실제로는 os 모듈 내에 sys 모듈도 포함되어 있음. # 따라서 os.sys.argv 등으로 모듈을 불러내는 것도 가능. # print(dir(sys)) # sys 모듈 내에 있는 모듈 확인이 가능.
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget): # Myapp 클래스를 생성하는데, QWidget 클래스를 상속받는다.

    def __init__(self):
        super().__init__() # super() 메소드는 자식클래스에서 부모클래스의 메소드를 실행시킬 때 활용. (메소드는 클래스 내에 종속되어 있는 함수를 의미)
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(100,100)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Test')
        self.setWindowIcon(QIcon('instagram_logo.jfif'))
        self.setGeometry(500, 500, 500, 500)
        self.show() # 위젯을 스크린에 보여줌.

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())