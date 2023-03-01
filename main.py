from sys import argv, exit
from PyQt5 import QtWidgets
from parser import MyWin


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = MyWin()
    myapp.show()
    exit(app.exec_())
