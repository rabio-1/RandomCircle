import sys
from random import randint, choice

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # сформировать графический интерфейс
        self.yellowbtn.clicked.connect(self.run)
        self.flag = False
        self.color = ['red', 'blue', 'yellow', 'green', 'orange', 'pink']

    def paintEvent(self, e):
        if not self.flag:
            return
        qp = QPainter(self)
        qp.begin(self)  # начать изменение
        for _ in range(randint(1, 10)):
            x = randint(0, 300)
            y = randint(0, 300)
            r = randint(10, 100)  # радиус
            col = choice(self.color)
            qp.setPen(QColor(col))  # цвет карандаша
            qp.setBrush(QColor(col))  # цвет кисти для закраски
            qp.drawEllipse(x, y, r, r)
        qp.end()  # конец изменений

    def run(self):
        self.flag = True
        self.repaint()  # перерисовать содержимое формы


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
