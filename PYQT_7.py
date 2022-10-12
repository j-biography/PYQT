
import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

# now = QDate.currentDate() # currentDate() 메서드는 현재 날짜를 리턴한다.
# print(now.toString()) # toString() 메서드는 리턴 값을 문자열로 변환하여 출력한다.

# print(now.toString('dd.MM.yyyy'))
# print(now.toString('ddd.MMMM.yyyy'))
# print(now.toString(Qt.ISODate))
# print(now.toString(Qt.DefaultLocaleLongDate))
# print(now.toString(Qt.DefaultLocaleShortDate))

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(1000, 1000, 1000, 1000)
        self.show()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())