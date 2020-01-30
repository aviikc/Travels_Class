from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from passanger_dialog import Ui_Dialog
import sys


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(["apple","pear","banana","coconut"])
        self.ui.pushButton_2.clicked.connect(self.on_cancel)
        self.ui.pushButton.clicked.connect(self.on_accept)
    
    def on_accept(self):
        v = self.ui.lineEdit.text()
        if v.strip() != "":
            print (v)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Value Error")
            msg.setInformativeText("Put some Name")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
    def on_cancel(self):
        sys.exit()
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()