import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont


class App(QWidget):

    def __init__(self):
        # Set Title
        super().__init__()
        self.title = "Account Registration System"
        self.x = 760
        self.y = 340
        self.width = 550
        self.height = 480
        self.initUI()

    # Clear Button / Function
    def clear(self):
        self.textbox1.clear()
        self.textbox2.clear()
        self.textbox3.clear()
        self.textbox4.clear()
        self.textbox5.clear()
        self.textbox6.clear()
    def submit(self):
        print("Form Submitted")

        # Set Window
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonicon.ico'))

        # Label
        self.textlbl1 = QLabel("Registration Form", self)
        self.textlbl1.move(179,15)
        self.textlbl1.setFont(QFont("Consolas", 15, QFont.Bold))

        self.textlbl2 = QLabel("First Name:", self)
        self.textlbl2.move(40, 70)
        self.textlbl2.setFont(QFont("Arial", 11, QFont.Bold))

        self.textlbl3 = QLabel("Last Name:", self)
        self.textlbl3.move(40, 125)
        self.textlbl3.setFont(QFont("Arial", 11, QFont.Bold))

        self.textlbl3 = QLabel("Username:", self)
        self.textlbl3.move(40, 180)
        self.textlbl3.setFont(QFont("Arial", 11, QFont.Bold))

        self.textlbl4 = QLabel("Password:", self)
        self.textlbl4.move(40, 235)
        self.textlbl4.setFont(QFont("Arial", 11, QFont.Bold))

        self.textlbl5 = QLabel("Email Address:", self)
        self.textlbl5.move(40, 290)
        self.textlbl5.setFont(QFont("Arial", 11, QFont.Bold))

        self.textlbl6 = QLabel("Contact Number:", self)
        self.textlbl6.move(40, 345)
        self.textlbl6.setFont(QFont("Arial", 11, QFont.Bold))

        # Text Box
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(190, 63)
        self.textbox1.resize(320,30)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(190, 119)
        self.textbox2.resize(320, 30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(190, 173)
        self.textbox3.resize(320, 30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(190, 225)
        self.textbox4.resize(320, 30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(190, 280)
        self.textbox5.resize(320, 30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(190, 338)
        self.textbox6.resize(320, 30)

        # Buttons
        self.button1 = QPushButton('Submit', self)
        self.button1.move(40, 400)
        self.button1.setGeometry(125, 400, 100, 50)
        self.button1.clicked.connect(self.submit)

        self.button2 = QPushButton('Clear', self)
        self.button2.move(40, 400)
        self.button2.setGeometry(325, 400, 100, 50)
        self.button2.clicked.connect(self.clear)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())