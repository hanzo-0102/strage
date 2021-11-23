import sys
from random import randint as rd
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QPointF


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paintEvent())

    def initUI(self):
        self.setGeometry(600, 600, 400, 400)
        self.setWindowTitle('Cringe')

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(rd(0, 255), rd(0, 255), rd(0, 255)))
        a = rd(10, self.width() - 10)
        self.qp.drawEllipse(a // 2, a // 2, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
