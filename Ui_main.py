# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\CINYOU\Desktop\pys\AI_SUPER1\MatchstickEquationSolver\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(907, 538)
        font = QtGui.QFont()
        font.setFamily("张海山锐谐体")
        Form.setFont(font)
        self.DB_label = QtWidgets.QLabel(Form)
        self.DB_label.setGeometry(QtCore.QRect(237, 278, 132, 16))
        font = QtGui.QFont()
        font.setFamily("张海山锐谐体")
        font.setPointSize(12)
        self.DB_label.setFont(font)
        self.DB_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.DB_label.setObjectName("DB_label")
        self.DB_comboBox = QtWidgets.QComboBox(Form)
        self.DB_comboBox.setGeometry(QtCore.QRect(420, 279, 191, 27))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.DB_comboBox.setFont(font)
        self.DB_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.DB_comboBox.setObjectName("DB_comboBox")
        self.solveInput_pushButton = QtWidgets.QPushButton(Form)
        self.solveInput_pushButton.setGeometry(QtCore.QRect(447, 220, 75, 23))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.solveInput_pushButton.setFont(font)
        self.solveInput_pushButton.setStyleSheet("font: 25 12pt \"3ds Light\";color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 1px solid rgb(255, 255, 255);")
        self.solveInput_pushButton.setObjectName("solveInput_pushButton")
        self.solveDB_pushButton = QtWidgets.QPushButton(Form)
        self.solveDB_pushButton.setGeometry(QtCore.QRect(447, 337, 75, 23))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.solveDB_pushButton.setFont(font)
        self.solveDB_pushButton.setStyleSheet("font: 25 12pt \"3ds Light\";color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 1px solid rgb(255, 255, 255);")
        self.solveDB_pushButton.setObjectName("solveDB_pushButton")
        self.difficulty_label = QtWidgets.QLabel(Form)
        self.difficulty_label.setGeometry(QtCore.QRect(377, 397, 171, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.difficulty_label.setFont(font)
        self.difficulty_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.difficulty_label.setScaledContents(False)
        self.difficulty_label.setObjectName("difficulty_label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(317, 87, 306, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.matchNum_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("张海山锐谐体")
        font.setPointSize(14)
        self.matchNum_label.setFont(font)
        self.matchNum_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.matchNum_label.setObjectName("matchNum_label")
        self.horizontalLayout_2.addWidget(self.matchNum_label)
        self.matchNum_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.matchNum_comboBox.setFont(font)
        self.matchNum_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.matchNum_comboBox.setObjectName("matchNum_comboBox")
        self.matchNum_comboBox.addItem("")
        self.matchNum_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.matchNum_comboBox)
        self.input_label = QtWidgets.QLabel(Form)
        self.input_label.setGeometry(QtCore.QRect(230, 170, 176, 18))
        font = QtGui.QFont()
        font.setFamily("张海山锐谐体")
        font.setPointSize(12)
        self.input_label.setFont(font)
        self.input_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.input_label.setObjectName("input_label")
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(420, 170, 341, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fst_10_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.fst_10_comboBox.setFont(font)
        self.fst_10_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.fst_10_comboBox.setObjectName("fst_10_comboBox")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.setItemText(0, "")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.addItem("")
        self.fst_10_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.fst_10_comboBox)
        self.fst_1_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.fst_1_comboBox.setFont(font)
        self.fst_1_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.fst_1_comboBox.setObjectName("fst_1_comboBox")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.fst_1_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.fst_1_comboBox)
        self.operator_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.operator_comboBox.setFont(font)
        self.operator_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.operator_comboBox.setObjectName("operator_comboBox")
        self.operator_comboBox.addItem("")
        self.operator_comboBox.addItem("")
        self.operator_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.operator_comboBox)
        self.sec_10_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.sec_10_comboBox.setFont(font)
        self.sec_10_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.sec_10_comboBox.setObjectName("sec_10_comboBox")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.setItemText(0, "")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.addItem("")
        self.sec_10_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.sec_10_comboBox)
        self.sec_1_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.sec_1_comboBox.setFont(font)
        self.sec_1_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.sec_1_comboBox.setObjectName("sec_1_comboBox")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.sec_1_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.sec_1_comboBox)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.trd_10_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.trd_10_comboBox.setFont(font)
        self.trd_10_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.trd_10_comboBox.setObjectName("trd_10_comboBox")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.setItemText(0, "")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.addItem("")
        self.trd_10_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.trd_10_comboBox)
        self.trd_1_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(10)
        self.trd_1_comboBox.setFont(font)
        self.trd_1_comboBox.setStyleSheet("QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(255, 255, 255);\n"
"        background: transparent;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}")
        self.trd_1_comboBox.setObjectName("trd_1_comboBox")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.trd_1_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.trd_1_comboBox)
        self.quit_pushButton = QtWidgets.QPushButton(Form)
        self.quit_pushButton.setGeometry(QtCore.QRect(300, 460, 75, 23))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.quit_pushButton.setFont(font)
        self.quit_pushButton.setStyleSheet("font: 25 12pt \"3ds Light\";color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 1px solid rgb(255, 255, 255);")
        self.quit_pushButton.setObjectName("quit_pushButton")
        self.about_pushButton = QtWidgets.QPushButton(Form)
        self.about_pushButton.setGeometry(QtCore.QRect(590, 460, 75, 23))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.about_pushButton.setFont(font)
        self.about_pushButton.setStyleSheet("font: 25 12pt \"3ds Light\";color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 1px solid rgb(255, 255, 255);")
        self.about_pushButton.setObjectName("about_pushButton")
        self.regenerate_pushButton = QtWidgets.QPushButton(Form)
        self.regenerate_pushButton.setGeometry(QtCore.QRect(650, 281, 101, 23))
        self.regenerate_pushButton.setStyleSheet("font: 25 12pt \"3ds Light\";color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 1px solid rgb(255, 255, 255);")
        self.regenerate_pushButton.setObjectName("regenerate_pushButton")
        self.hide_pushButton = QtWidgets.QPushButton(Form)
        self.hide_pushButton.setGeometry(QtCore.QRect(450, 460, 75, 23))
        self.hide_pushButton.setStyleSheet("font: 25 12pt \"3ds Light\";color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 1px solid rgb(255, 255, 255);")
        self.hide_pushButton.setObjectName("hide_pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MatchstickEquationSolver"))
        self.DB_label.setText(_translate("Form", "或选择右边的等式之一："))
        self.solveInput_pushButton.setText(_translate("Form", "Solve"))
        self.solveDB_pushButton.setText(_translate("Form", "Solve"))
        self.difficulty_label.setText(_translate("Form", "Difficulty："))
        self.matchNum_label.setText(_translate("Form", "请选择可以移动的火柴棍数目："))
        self.matchNum_comboBox.setItemText(0, _translate("Form", "2"))
        self.matchNum_comboBox.setItemText(1, _translate("Form", "1"))
        self.input_label.setText(_translate("Form", "请输入需要求解的等式："))
        self.fst_10_comboBox.setItemText(1, _translate("Form", "1"))
        self.fst_10_comboBox.setItemText(2, _translate("Form", "2"))
        self.fst_10_comboBox.setItemText(3, _translate("Form", "3"))
        self.fst_10_comboBox.setItemText(4, _translate("Form", "4"))
        self.fst_10_comboBox.setItemText(5, _translate("Form", "5"))
        self.fst_10_comboBox.setItemText(6, _translate("Form", "6"))
        self.fst_10_comboBox.setItemText(7, _translate("Form", "7"))
        self.fst_10_comboBox.setItemText(8, _translate("Form", "8"))
        self.fst_10_comboBox.setItemText(9, _translate("Form", "9"))
        self.fst_1_comboBox.setItemText(0, _translate("Form", "0"))
        self.fst_1_comboBox.setItemText(1, _translate("Form", "1"))
        self.fst_1_comboBox.setItemText(2, _translate("Form", "2"))
        self.fst_1_comboBox.setItemText(3, _translate("Form", "3"))
        self.fst_1_comboBox.setItemText(4, _translate("Form", "4"))
        self.fst_1_comboBox.setItemText(5, _translate("Form", "5"))
        self.fst_1_comboBox.setItemText(6, _translate("Form", "6"))
        self.fst_1_comboBox.setItemText(7, _translate("Form", "7"))
        self.fst_1_comboBox.setItemText(8, _translate("Form", "8"))
        self.fst_1_comboBox.setItemText(9, _translate("Form", "9"))
        self.operator_comboBox.setItemText(0, _translate("Form", "+"))
        self.operator_comboBox.setItemText(1, _translate("Form", "-"))
        self.operator_comboBox.setItemText(2, _translate("Form", "×"))
        self.sec_10_comboBox.setItemText(1, _translate("Form", "1"))
        self.sec_10_comboBox.setItemText(2, _translate("Form", "2"))
        self.sec_10_comboBox.setItemText(3, _translate("Form", "3"))
        self.sec_10_comboBox.setItemText(4, _translate("Form", "4"))
        self.sec_10_comboBox.setItemText(5, _translate("Form", "5"))
        self.sec_10_comboBox.setItemText(6, _translate("Form", "6"))
        self.sec_10_comboBox.setItemText(7, _translate("Form", "7"))
        self.sec_10_comboBox.setItemText(8, _translate("Form", "8"))
        self.sec_10_comboBox.setItemText(9, _translate("Form", "9"))
        self.sec_1_comboBox.setItemText(0, _translate("Form", "0"))
        self.sec_1_comboBox.setItemText(1, _translate("Form", "1"))
        self.sec_1_comboBox.setItemText(2, _translate("Form", "2"))
        self.sec_1_comboBox.setItemText(3, _translate("Form", "3"))
        self.sec_1_comboBox.setItemText(4, _translate("Form", "4"))
        self.sec_1_comboBox.setItemText(5, _translate("Form", "5"))
        self.sec_1_comboBox.setItemText(6, _translate("Form", "6"))
        self.sec_1_comboBox.setItemText(7, _translate("Form", "7"))
        self.sec_1_comboBox.setItemText(8, _translate("Form", "8"))
        self.sec_1_comboBox.setItemText(9, _translate("Form", "9"))
        self.label.setText(_translate("Form", "   ="))
        self.trd_10_comboBox.setItemText(1, _translate("Form", "1"))
        self.trd_10_comboBox.setItemText(2, _translate("Form", "2"))
        self.trd_10_comboBox.setItemText(3, _translate("Form", "3"))
        self.trd_10_comboBox.setItemText(4, _translate("Form", "4"))
        self.trd_10_comboBox.setItemText(5, _translate("Form", "5"))
        self.trd_10_comboBox.setItemText(6, _translate("Form", "6"))
        self.trd_10_comboBox.setItemText(7, _translate("Form", "7"))
        self.trd_10_comboBox.setItemText(8, _translate("Form", "8"))
        self.trd_10_comboBox.setItemText(9, _translate("Form", "9"))
        self.trd_1_comboBox.setItemText(0, _translate("Form", "0"))
        self.trd_1_comboBox.setItemText(1, _translate("Form", "1"))
        self.trd_1_comboBox.setItemText(2, _translate("Form", "2"))
        self.trd_1_comboBox.setItemText(3, _translate("Form", "3"))
        self.trd_1_comboBox.setItemText(4, _translate("Form", "4"))
        self.trd_1_comboBox.setItemText(5, _translate("Form", "5"))
        self.trd_1_comboBox.setItemText(6, _translate("Form", "6"))
        self.trd_1_comboBox.setItemText(7, _translate("Form", "7"))
        self.trd_1_comboBox.setItemText(8, _translate("Form", "8"))
        self.trd_1_comboBox.setItemText(9, _translate("Form", "9"))
        self.quit_pushButton.setText(_translate("Form", "Quit"))
        self.about_pushButton.setText(_translate("Form", "About"))
        self.regenerate_pushButton.setText(_translate("Form", "Regenerate"))
        self.hide_pushButton.setText(_translate("Form", "Hide"))
