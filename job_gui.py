from PyQt5 import QtCore, QtGui, QtWidgets
from information import *


class UiMainWindow(object):
    def setup_ui(self, main_window) -> None:
        main_window.setObjectName("main_window")
        main_window.resize(1101, 867)
        # main_window.showMaximized()
        main_window.setMinimumSize(QtCore.QSize(1101, 867))
        main_window.setMaximumSize(QtCore.QSize(1101, 867))
        main_window.setStyleSheet("background-color: rgb(170, 255, 127);")
        main_window.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('favicon.ico')))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("central_widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('search.png')))
        self.pushButton.setGeometry(QtCore.QRect(470, 125, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        # font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 255);\n"
                                      "background-color: rgb(255, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(315, 20, 470, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 125, 190, 30))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(95, 33, 190, 30))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(920, 25, 190, 30))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(720, 120, 265, 30))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(855, 77, 265, 30))
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 77, 265, 30))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 90, 80, 30))
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 60, 120, 30))
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 70, 85, 40))
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 120, 90, 40))
        font.setPointSize(24)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 233, 206);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 70, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('DevOps')
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1000, 30, 45, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('113')
        self.lineEdit_2.setToolTip(region)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 35, 45, 30))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText('')
        self.lineEdit_3.setToolTip(categories)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1000, 120, 45, 30))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText('100')
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1000, 75, 45, 30))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText('30')
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(795, 75, 45, 30))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText('')
        self.lineEdit_6.setToolTip(industry)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(40, 73, 60, 40))
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.spinBox.setValue(0)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(320, 85, 30, 40))
        self.radioButton.setChecked(False)
        self.checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox.setGeometry(QtCore.QRect(345, 95, 20, 20))
        self.checkbox.setChecked(False)
        self.checkbox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_2.setGeometry(QtCore.QRect(345, 65, 20, 20))
        self.checkbox_2.setChecked(False)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 170, 1101, 691))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(224, 254, 255);")
        self.textBrowser.setObjectName("textBrowser")
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("status_bar")
        main_window.setStatusBar(self.statusbar)
        self.text_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def text_ui(self, main_window) -> None:
        main_window.setWindowTitle("?????????????????? ???????????????? ???? hh.ru")
        self.pushButton.setText("??????????")
        self.label.setText("?????????????? ?????????????????? ?????? ????????????")
        self.label_2.setText("?????????????? ????????????????")
        self.label_3.setText("??????????????????????????")
        self.label_4.setText("????????????")
        self.label_5.setText("?????????? ???????????????? ?? ???????? ????????????")
        self.label_6.setText("???????????? ????????")
        self.label_7.setText("????????????????")
        self.label_8.setText("??????.????????")
        self.label_9.setText("????????-???? ???? ????????")
        self.label_10.setText("??????????????????\n ????????????????")
