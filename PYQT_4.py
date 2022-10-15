# 상태바(statusBar) + 메뉴바(menuBar) 생성

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QAction, qApp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    # 메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar, QWidget 영역으로 나뉨.
    def initUI(self):
        QToolTip.setFont(QFont('SanSerif', 10))
        self.setToolTip('<b>QWidget</b>') 

        self.statusBar()
        self.statusBar().setToolTip('<b>QStatusBar</b>')

        btn = QPushButton('Quit', self)
        btn.setToolTip('<b>Quit</b>')
        btn.move(200, 200)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        btn2 = QPushButton('Button', self)
        btn2.setToolTip('<b>Button</b>')
        btn2.move(400, 200)
        btn2.resize(btn.sizeHint())
        btn2.clicked.connect(QCoreApplication.instance().quit)

        exitAction = QAction(QIcon('image\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q') # 본 기능의 단축키를 설정 가능.
        exitAction.setStatusTip('<b>Exit application</b>')
        exitAction.triggered.connect(qApp.quit) # exitAction을 눌렀을 때 생성되는 triggered 시그널이 quit() 메서드에 연결되어, 어플리케이션을 종료.

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) # menubar.setNativeMenuBar(False)를 추가함으로써 macOS에서도 Windows 환경과 동일한 결과를 얻을 수 있다.
        filemenu = menubar.addMenu('&File') # 메뉴 이름 앞에 앰퍼샌드(&)를 더하면, (Alt + 앰퍼샌드 뒤에 있는 알파벳)을 단축키로 활용 가능.
        filemenu.addAction(exitAction)
        filemenu2 = menubar.addMenu('&Modify') # 이와 같은 방식으로 여러가지 메뉴를 생성 가능.
        filemenu2.addAction(exitAction)

        self.setWindowTitle('Statusbar')
        self.setWindowIcon(QIcon('image\instagram_logo.jfif'))
        self.setGeometry(1200, 1000, 700, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())