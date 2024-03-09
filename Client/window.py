from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabBar, QApplication, QWidget, QMainWindow,QLabel,QLineEdit
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from request_handler import RequestHandler


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)
        self.reqHandler = RequestHandler()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            result = self.reqHandler.get_phonebook_data(self.text())
            pass
        else:
            super().keyPressEvent(event)

    

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.reqHandler = RequestHandler()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.setWindowTitle("Contacts App")
        phonebookIdLabel = QLabel(MainWindow)
        phonebookIdLabel.setText("Enter Phonebook ID")
        phonebookIdLabel.setGeometry(QtCore.QRect(10, 10, 100, 20))
      #subclass the QLineEdit
        self.phonebookIdTextEdit = LineEdit(MainWindow)
        self.phonebookIdTextEdit.setMaxLength(5)
        self.phonebookIdTextEdit.setGeometry(QtCore.QRect(110, 10, 20, 20))
        phoneLabel = QLabel(MainWindow)
        phoneLabel.setText("Phone Number")
        phoneLabel.setGeometry(QtCore.QRect(10, 170, 200, 20))
        phoneTextEdit = QLineEdit(MainWindow)
        phoneTextEdit.setGeometry(QtCore.QRect(220, 170, 200, 20))
        


app = QApplication(sys.argv)

window = MainWindow()
window.setupUi(window)
window.show()
app.exec()