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
        # self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('search.png')))
        self.pushButton.setGeometry(QtCore.QRect(470, 125, 100, 35))
        font = QtGui.QFont()
        font.setPixelSize(24)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 255);\n"
                                      "background-color: rgb(255, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(315, 20, 470, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(45, 45, 65, 20))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(0, 0, 0);\n"
                                        "border-style: outset; border-radius: 7px;"
                                        "border-color: green; border-width: 2px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setToolTip(definition_readDB)
        font.setPixelSize(14)
        self.pushButton_2.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(177, 125, 190, 30))
        font.setPixelSize(19)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(740, 35, 190, 30))
        font.setPixelSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(940, 30, 150, 30))
        font.setPixelSize(19)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(740, 120, 265, 30))
        font.setPixelSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(875, 77, 265, 30))
        font.setPixelSize(19)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 82, 265, 30))
        font.setPixelSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 90, 80, 30))
        font.setPixelSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 60, 120, 30))
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(130, 32, 90, 35))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_11")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(705, 70, 85, 40))
        font.setPixelSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_10")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 123, 130, 37))
        font.setPixelSize(32)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 233, 206);")
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 70, 305, 40))
        font = QtGui.QFont()
        font.setPixelSize(28)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('DevOps')
        self.lineEdit.setToolTip(definition_search)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1020, 30, 45, 30))
        font = QtGui.QFont()
        font.setPixelSize(14)
        font.setBold(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('113')
        self.lineEdit_2.setToolTip(region)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(880, 35, 45, 30))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText('')
        self.lineEdit_3.setToolTip(categories)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1020, 120, 45, 30))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText('100')
        self.lineEdit_4.setToolTip(definition_field)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1020, 75, 45, 30))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText('30')
        self.lineEdit_5.setToolTip(definition_days)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(800, 75, 45, 30))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText('')
        self.lineEdit_6.setToolTip(industry)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(40, 73, 60, 40))
        font.setPixelSize(16)
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
        self.checkbox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_3.setGeometry(QtCore.QRect(135, 65, 20, 20))
        self.checkbox_3.setChecked(False)
        self.checkbox_3.setToolTip(definition_txt)
        self.checkbox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_4.setGeometry(QtCore.QRect(165, 65, 20, 20))
        self.checkbox_4.setChecked(False)
        self.checkbox_4.setToolTip(definition_db)
        self.checkbox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_5.setGeometry(QtCore.QRect(195, 65, 20, 20))
        self.checkbox_5.setChecked(False)
        self.checkbox_5.setToolTip(definition_pdf)
        self.checkbox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_6.setGeometry(QtCore.QRect(120, 15, 20, 20))
        self.checkbox_6.setChecked(True)
        self.checkbox_6.setToolTip(definition_fullDay)
        self.checkbox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_7.setGeometry(QtCore.QRect(100, 15, 20, 20))
        self.checkbox_7.setChecked(True)
        self.checkbox_7.setToolTip(definition_remote)
        self.checkbox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_8.setGeometry(QtCore.QRect(80, 15, 20, 20))
        self.checkbox_8.setChecked(True)
        self.checkbox_8.setToolTip(definition_flyInFlyOut)
        self.checkbox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_9.setGeometry(QtCore.QRect(60, 15, 20, 20))
        self.checkbox_9.setChecked(True)
        self.checkbox_9.setToolTip(definition_shift)
        self.checkbox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_10.setGeometry(QtCore.QRect(40, 15, 20, 20))
        self.checkbox_10.setChecked(True)
        self.checkbox_10.setToolTip(definition_flexible)
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
        main_window.setWindowTitle("Поисковик вакансий на hh.ru")
        self.pushButton.setText("поиск")
        self.pushButton_2.setText("read db")
        self.label.setText("Введите профессию для поиска")
        self.label_2.setText("Найдено вакансий")
        self.label_3.setText("Специализация")
        self.label_4.setText("Регион")
        self.label_5.setText("Число вакансий в поле вывода")
        self.label_6.setText("Период дней")
        self.label_7.setText("Страница")
        self.label_8.setText("доп.инфо")
        self.label_9.setText("сорт-ка по дате")
        self.label_10.setText(" сохранить\ntxt   db   pdf")
        self.label_11.setText("Индустрия\n компании")
