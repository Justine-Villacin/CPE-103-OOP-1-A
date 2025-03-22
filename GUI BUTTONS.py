import sys
from PyQt5.QtWidgets import QWidget,QApplication, QMainWindow, QPushButton,QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__() # initializes the main window like in the previous one
        # window = QMainWindow()
        self.title= "PyQt Button"
        self.x=200 # or left
        self.y=200 # or top
        self.width=300
        self.height=300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.button = QPushButton('Click me!', self)
        self.button. setToolTip("You've hovered over me!")
        self.button.move(110,70)

        # Text Box
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(260, 40)
        self.textbox.setText("Set this text value ")
        self.show()

# button.move(x,y)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())