import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QLabel, QLCDNumber


class Foc(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 320, 60)
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton(self)
        self.btn.setText("->")
        self.btn.setGeometry(140, 20, 30, 30)
        self.btn.clicked.connect(self.word)
        self.right = QLineEdit(self)
        self.right.setGeometry(175, 20, 125, 30)

        self.left = QLineEdit(self)

        self.left.setGeometry(10, 20, 125, 30)

    def word(self):
        if self.btn.text() == '->':
            self.btn.setText('<-')
            self.right.setText(self.left.text())
            self.left.setText(' ')

        else:
            self.btn.setText('->')
            self.left.setText(self.right.text())
            self.right.setText(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Foc()
    ex.show()
    sys.exit(app.exec())
