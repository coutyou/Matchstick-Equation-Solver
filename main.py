import sys
from random import choice
from Solver import *
from Ui_main import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from NotificationWindow import *
from CircleLineWindow import *

class MyMainForm(QMainWindow, Ui_Form, CircleLineWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        
        self.Solver = Solver()
        self.generateDB()

        self.setSlot()
        self.show()

    # 设置槽函数
    def setSlot(self):
        self.solveInput_pushButton.clicked.connect(self.solvePressed)
        self.solveDB_pushButton.clicked.connect(self.solvePressed)
        self.about_pushButton.clicked.connect(self.aboutPressed)
        self.quit_pushButton.clicked.connect(self.close)
        self.regenerate_pushButton.clicked.connect(self.regenerateDB)
        self.hide_pushButton.clicked.connect(self.showMinimized)

    # about被按下时的槽函数
    def aboutPressed(self):
        NotificationWindow.info('About', "Developer:    自71 游晶")

    # 处理字符串
    def strProcessing(self, string):
        toBeReplaced = ["0" + str(num) for num in range(10)]
        for n in range(10):
            string = string.replace(toBeReplaced[n], str(n))
        return string

    # 产生等式库
    def generateDB(self):
        itemIndex = 0
        totalNum = 5
        while(itemIndex < totalNum):
            # 随机生成等式
            string = choice(numList) + choice(numList) + choice(operatorList) \
                + choice(numList) + choice(numList) + "=" \
                + choice(numList) + choice(numList)
            # 用第二根的算法解等式
            difficulty, res = self.Solver.solve(Equation(string), matchNum=2)
            # 如果该等式有解 添加至ComboBox
            if res != []:
                self.DB_comboBox.addItem("")
                self.DB_comboBox.setItemText(itemIndex, QCoreApplication.translate("Form", self.strProcessing(string)))
                itemIndex += 1
        itemIndex = 0
        while(itemIndex < totalNum):
            string = choice(numList) + choice(numList) + choice(operatorList) \
                + choice(numList) + choice(numList) + "=" \
                + choice(numList) + choice(numList)
            # 用第一根的算法解等式
            difficulty, res = self.Solver.solve(Equation(string), matchNum=1)
            if res != []:
                self.DB_comboBox.addItem("")
                self.DB_comboBox.setItemText(itemIndex + totalNum, QCoreApplication.translate("Form", self.strProcessing(string)))
                itemIndex += 1

    # 重新生成等式库
    def regenerateDB(self):
        itemIndex = 0
        totalNum = 5
        while(itemIndex < totalNum):
            # 随机生成等式
            string = choice(numList) + choice(numList) + choice(operatorList) \
                + choice(numList) + choice(numList) + "=" \
                + choice(numList) + choice(numList)
            # 用第二根的算法解等式
            difficulty, res = self.Solver.solve(Equation(string), matchNum=2)
            # 如果该等式有解 添加至ComboBox
            if res != []:
                self.DB_comboBox.setItemText(itemIndex, QCoreApplication.translate("Form", self.strProcessing(string)))
                itemIndex += 1
        itemIndex = 0
        while(itemIndex < totalNum):
            string = choice(numList) + choice(numList) + choice(operatorList) \
                + choice(numList) + choice(numList) + "=" \
                + choice(numList) + choice(numList)
            # 用第一根的算法解等式
            difficulty, res = self.Solver.solve(Equation(string), matchNum=1)
            if res != []:
                self.DB_comboBox.setItemText(itemIndex + totalNum, QCoreApplication.translate("Form", self.strProcessing(string)))
                itemIndex += 1

    # Solve键被按下时的槽函数
    def solvePressed(self):
        sender = self.sender()
        # set用于结果的去重
        res_set = set()
        # 判断是哪个Solve按钮被按下
        if sender is self.solveInput_pushButton:
            # 获得输入的字符串
            input_str = self.fst_10_comboBox.currentText() + self.fst_1_comboBox.currentText() + self.operator_comboBox.currentText() \
                + self.sec_10_comboBox.currentText() + self.sec_1_comboBox.currentText() + "=" \
                + self.trd_10_comboBox.currentText() + self.trd_1_comboBox.currentText()
            # 解等式
            difficulty, res = self.Solver.solve(Equation(input_str), matchNum=int(self.matchNum_comboBox.currentText()))
            # 显示结果
            self.difficulty_label.setText("Difficulty:  " + str(difficulty))
            # 如果等式本身是对的，也加入结果集中
            if Equation(input_str).checkRight():
                res.append(self.strProcessing(input_str))
            # 若结果不为空
            if res != []:
                res_str = ""
                for s in res:
                    # 若不在结果的set中，则添加
                    if s not in res_set:
                        res_set.add(s)
                for s in res_set:
                    res_str += s + "\n"
                NotificationWindow.success('Solution:', res_str)
            # 若结果为空
            else:
                res_str = "No Solution!"
                NotificationWindow.error('Error', res_str)
        elif sender is self.solveDB_pushButton:
            input_str = self.DB_comboBox.currentText()
            difficulty, res = self.Solver.solve(Equation(input_str), matchNum=int(self.matchNum_comboBox.currentText()))
            self.difficulty_label.setText("Difficulty:  " + str(difficulty))
            if Equation(input_str).checkRight():
                res.append(self.strProcessing(input_str))
            if res != []:
                res_str = ""
                for s in res:
                    if s not in res_set:
                        res_set.add(s)
                for s in res_set:
                    res_str += s + "\n"
                NotificationWindow.success('Solution:', res_str)
            else:
                res_str = "No Solution!"
                NotificationWindow.error('Error', res_str)
        else:
            # if more function added
            pass

    # 按下Esc退出
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

# 主函数
def main():
    app = QApplication(sys.argv)
    mf = MyMainForm()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()