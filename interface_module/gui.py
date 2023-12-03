from PyQt5 import QtCore, QtGui, QtWidgets
from info_module.information import *
from icon_module.decode_img_temp import decode_b64
from info_module.area import area_hh, area_trudvsem


class UiMainWindow(object):
    def setup_ui(self, main_window) -> None:
        main_window.setObjectName("main_window")
        main_window.resize(1101, 900)
        # main_window.showMaximized()
        main_window.setMinimumSize(QtCore.QSize(1101, 900))
        main_window.setMaximumSize(QtCore.QSize(1101, 900))
        main_window.setStyleSheet("background-color: rgb(170, 255, 127);")
        img = decode_b64()
        main_window.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(img[0])))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("central_widget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1101, 900))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        # self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('search.png')))
        self.pushButton.setGeometry(QtCore.QRect(490, 125, 100, 35))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        font = QtGui.QFont()
        font.setPixelSize(24)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 255);\n"
                                      "background-color: rgb(255, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(335, 15, 490, 30))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.icon = QtWidgets.QLabel(self.tab)
        self.icon.setGeometry(QtCore.QRect(300, 15, 30, 30))
        self.pix = QtGui.QPixmap(img[0]).scaled(30, 30)
        self.icon.setPixmap(self.pix)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(45, 45, 65, 20))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.pushButton_2.setStyleSheet(
            "color: rgb(255, 255, 255);\nbackground-color: rgb(0, 0, 0);\n"
            "border-style: outset; border-radius: 7px;border-color: green; "
            "border-width: 2px;"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setToolTip(definition_readDB)
        font.setPixelSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(685, 140, 15, 15))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.pushButton_5.setStyleSheet(
            "color: rgb(255, 255, 255);\nbackground-color: rgb(0, 0, 0);\n"
            "border-style: outset; border-radius: 7px;border-color: red; "
            "border-width: 2px;"
        )
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setToolTip('обновление списка online')
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(177, 125, 190, 30))
        font.setPixelSize(19)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(720, 95, 130, 30))
        font.setPixelSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(935, 95, 265, 30))
        font.setPixelSize(19)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(770, 10, 265, 30))
        font.setPixelSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(880, 50, 170, 30))
        font.setPixelSize(19)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(110, 82, 265, 30))
        font.setPixelSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(270, 85, 80, 20))
        font.setPixelSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(250, 60, 120, 30))
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(125, 52, 120, 13))
        font.setPixelSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(153, 35, 70, 15))
        font.setPixelSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(720, 52, 100, 40))
        font.setPixelSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(235, 105, 120, 20))
        font.setPixelSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 123, 130, 37))
        font.setPixelSize(32)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 233, 206);")
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(395, 70, 305, 40))
        font = QtGui.QFont()
        font.setPixelSize(28)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('инженер')
        self.lineEdit.setToolTip(definition_search)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(1020, 95, 45, 30))
        font = QtGui.QFont()
        font.setPixelSize(14)
        font.setBold(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('113')
        self.lineEdit_2.setValidator(QtGui.QIntValidator(0, 10000, main_window))
        self.lineEdit_2.setToolTip(region)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(870, 95, 45, 30))
        font.setPixelSize(14)
        font.setBold(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText('')
        self.lineEdit_3.setValidator(QtGui.QIntValidator(0, 1000, main_window))
        self.lineEdit_3.setToolTip(categories)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(1020, 10, 45, 30))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText('100')
        self.lineEdit_4.setValidator(QtGui.QIntValidator(0, 100, main_window))
        self.lineEdit_4.setToolTip(definition_field)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(1020, 52, 45, 30))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText('30')
        self.lineEdit_5.setValidator(QtGui.QIntValidator(0, 30, main_window))
        self.lineEdit_5.setToolTip(definition_days)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(815, 55, 45, 30))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText('')
        self.lineEdit_6.setValidator(QtGui.QIntValidator(0, 1000, main_window))
        self.lineEdit_6.setToolTip(industry)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(40, 73, 60, 40))
        font.setPixelSize(16)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.spinBox.setValue(0)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(340, 85, 20, 20))
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.radioButton.setChecked(False)
        self.radioButton.setToolTip(additional_information)
        self.checkbox = QtWidgets.QCheckBox(self.tab)
        self.checkbox.setGeometry(QtCore.QRect(365, 85, 20, 20))
        self.checkbox.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox.setChecked(False)
        self.checkbox.setToolTip(count_vacancies)
        self.checkbox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_2.setGeometry(QtCore.QRect(365, 65, 20, 20))
        self.checkbox_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_2.setChecked(True)
        self.checkbox_2.setToolTip(sort_date)
        self.checkbox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_3.setGeometry(QtCore.QRect(125, 65, 20, 20))
        self.checkbox_3.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_3.setChecked(False)
        self.checkbox_3.setToolTip(definition_txt)
        self.checkbox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_4.setGeometry(QtCore.QRect(150, 65, 20, 20))
        self.checkbox_4.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_4.setChecked(False)
        self.checkbox_4.setToolTip(definition_db)
        self.checkbox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_5.setGeometry(QtCore.QRect(175, 65, 20, 20))
        self.checkbox_5.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_5.setChecked(False)
        self.checkbox_5.setToolTip(definition_pdf)
        self.checkbox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_6.setGeometry(QtCore.QRect(120, 15, 20, 20))
        self.checkbox_6.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_6.setChecked(True)
        self.checkbox_6.setToolTip(definition_fullDay)
        self.checkbox_7 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_7.setGeometry(QtCore.QRect(100, 15, 20, 20))
        self.checkbox_7.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_7.setChecked(True)
        self.checkbox_7.setToolTip(definition_remote)
        self.checkbox_8 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_8.setGeometry(QtCore.QRect(80, 15, 20, 20))
        self.checkbox_8.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_8.setChecked(True)
        self.checkbox_8.setToolTip(definition_flyInFlyOut)
        self.checkbox_9 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_9.setGeometry(QtCore.QRect(60, 15, 20, 20))
        self.checkbox_9.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_9.setChecked(True)
        self.checkbox_9.setToolTip(definition_shift)
        self.checkbox_10 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_10.setGeometry(QtCore.QRect(40, 15, 20, 20))
        self.checkbox_10.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_10.setChecked(True)
        self.checkbox_10.setToolTip(definition_flexible)
        self.checkbox_11 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_11.setGeometry(QtCore.QRect(200, 65, 20, 20))
        self.checkbox_11.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_11.setChecked(False)
        self.checkbox_11.setToolTip(definition_csv)
        self.checkbox_12 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_12.setGeometry(QtCore.QRect(225, 65, 20, 20))
        self.checkbox_12.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_12.setChecked(False)
        self.checkbox_12.setToolTip(definition_xls)
        self.checkbox_13 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_13.setGeometry(QtCore.QRect(365, 105, 20, 20))
        self.checkbox_13.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_13.setChecked(True)
        self.checkbox_13.setToolTip(center)
        self.comboButton = QtWidgets.QComboBox(self.tab)
        self.comboButton.setGeometry(QtCore.QRect(700, 140, 370, 25))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboButton.setFont(font)
        self.comboButton.setStyleSheet("background-color: rgb(224, 254, 254);")
        self.comboButton.setObjectName("comboButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 170, 1101, 730))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboButton_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboButton_2.setGeometry(QtCore.QRect(700, 140, 370, 25))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboButton_2.setFont(font)
        self.comboButton_2.setStyleSheet(
            "background-color: rgb(224, 254, 254);")
        self.comboButton_2.setObjectName("comboButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 170, 1101, 730))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setOpenLinks(False)
        self.textBrowser_2.setStyleSheet("background-color: rgb(224, 224, "
                                         "255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_2, "trudvsem.ru")
        self.tabWidget.addTab(self.tab, "hh.ru")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 125, 100, 35))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        font = QtGui.QFont()
        font.setPixelSize(24)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 0, 255);\n"
                                        "background-color: rgb(255, 255, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(335, 15, 490, 30))
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.icon_2 = QtWidgets.QLabel(self.tab_2)
        self.icon_2.setGeometry(QtCore.QRect(300, 15, 30, 30))
        self.pix_2 = QtGui.QPixmap(img[1]).scaled(30, 30)
        self.icon_2.setPixmap(self.pix_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(45, 45, 65, 20))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(0, 0, 0);\n"
                                        "border-style: outset; "
                                        "border-radius: 7px;"
                                        "border-color: green; "
                                        "border-width: 2px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setToolTip(definition_readDB)
        font.setPixelSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(685, 140, 15, 15))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.pushButton_6.setStyleSheet(
            "color: rgb(255, 255, 255);\nbackground-color: rgb(0, 0, 0);\n"
            "border-style: outset; border-radius: 7px;border-color: red; "
            "border-width: 2px;"
        )
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setToolTip('обновление списка online')
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(177, 125, 190, 30))
        font.setPixelSize(19)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(935, 95, 265, 30))
        font.setPixelSize(19)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(770, 10, 265, 30))
        font.setPixelSize(15)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(880, 50, 170, 30))
        font.setPixelSize(19)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(110, 82, 265, 30))
        font.setPixelSize(18)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(150, 40, 120, 25))
        font.setPixelSize(11)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(20, 5, 250, 30))
        font.setPixelSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(235, 80, 120, 20))
        font.setPixelSize(13)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(40, 123, 130, 37))
        font.setPixelSize(32)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(255, 233, 206);")
        self.lcdNumber_2.setDigitCount(7)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.checkbox_24 = QtWidgets.QCheckBox(self.tab_2)
        self.checkbox_24.setGeometry(QtCore.QRect(150, 65, 20, 20))
        self.checkbox_24.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_24.setChecked(False)
        self.checkbox_24.setToolTip(definition_db[1:-1])
        self.checkbox_25 = QtWidgets.QCheckBox(self.tab_2)
        self.checkbox_25.setGeometry(QtCore.QRect(175, 65, 20, 20))
        self.checkbox_25.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_25.setChecked(False)
        self.checkbox_25.setToolTip(definition_pdf[1:-1])
        self.checkbox_26 = QtWidgets.QCheckBox(self.tab_2)
        self.checkbox_26.setGeometry(QtCore.QRect(200, 65, 20, 20))
        self.checkbox_26.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_26.setChecked(False)
        self.checkbox_26.setToolTip(definition_xls[1:-1])
        self.checkbox_27 = QtWidgets.QCheckBox(self.tab_2)
        self.checkbox_27.setGeometry(QtCore.QRect(365, 80, 20, 20))
        self.checkbox_27.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.checkbox_27.setChecked(True)
        self.checkbox_27.setToolTip(center[1:-1])
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(395, 70, 305, 40))
        font = QtGui.QFont()
        font.setPixelSize(28)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_20.setText('инженер')
        self.lineEdit_20.setToolTip(definition_search[1:49])
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(1020, 95, 45, 30))
        font = QtGui.QFont()
        font.setPixelSize(14)
        font.setBold(True)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_21.setText('')
        self.lineEdit_21.setValidator(QtGui.QIntValidator(0, 10000,
                                                          main_window))
        self.lineEdit_21.setToolTip(str(area_trudvsem))
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(1020, 10, 45, 30))
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_22.setText('100')
        self.lineEdit_22.setValidator(QtGui.QIntValidator(0, 100, main_window))
        self.lineEdit_22.setToolTip(definition_field[1:-1])
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(1020, 52, 45, 30))
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_23.setText('30')
        self.lineEdit_23.setValidator(QtGui.QIntValidator(0, 10, main_window))
        self.lineEdit_23.setToolTip(definition_days[1:-3] + '99')
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setGeometry(QtCore.QRect(40, 73, 60, 40))
        font.setPixelSize(16)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.spinBox_2.setValue(0)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox")
        main_window.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(main_window)
        # self.statusbar.setObjectName("status_bar")
        # main_window.setStatusBar(self.statusbar)
        self.text_ui(main_window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def text_ui(self, main_window) -> None:
        main_window.setWindowTitle("Поисковик вакансий на hh.ru и trudvsem.ru")
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
        self.label_10.setText("txt  db   pdf   csv   xls")
        self.label_11.setText("сохранить")
        self.label_12.setText("Индустрия\n компании")
        self.label_13.setText("центровка текста")
        id_areas = ['выбор региона'] + area_hh
        # self.comboButton.addItem('Россия: 113')
        self.comboButton.addItems(id_areas)
        self.label_20.setText("Введите профессию для поиска")
        self.label_21.setText("Найдено вакансий")
        self.pushButton_3.setText("поиск")
        self.pushButton_4.setText("read db")
        # self.comboButton_2.addItem('Хабаровский край: 27')
        self.comboButton_2.addItems(['выбор региона'] + area_trudvsem)
        self.label_24.setText("Регион")
        self.label_25.setText("Число вакансий в поле вывода")
        self.label_26.setText("Период дней")
        self.label_27.setText("Страница")
        self.label_28.setText(" сохранить\ndb   pdf   xls")
        self.label_29.setText("Федеральная государственная\n   "
                              "информационная система")
        self.label_30.setText("центровка текста")