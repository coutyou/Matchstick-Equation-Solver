from Tables import *

class Equation(object):
    def __init__(self, string):
        # 处理字符串，并获取各个IndexList
        self.str = self.strProcessing(string)
        self.plusTwoIndexList = self.getPlusTwoIndex()
        self.plusIndexList = self.getPlusIndex()
        self.metaTwoIndexList = self.getMetaTwoIndex()
        self.metaIndexList = self.getMetaIndex()
        self.minusTwoIndexList = self.getMinusTwoIndex()
        self.minusIndexList = self.getMinusIndex()
        self.metaPlusIndexList = self.getMetaPlusIndex()
        self.metaMinusIndexList = self.getMetaMinusIndex()
        self.space2OneIndexList = self.getSpace2OneIndex()
        # if DEBUG_MODE:
        #     print("self.str:  ", self.str)
        #     print("self.plusIndexList:  ")
        #     for char in self.plusIndexList:
        #         print(char)
        #     print("self.metaIndexList:  ")
        #     for char in self.metaIndexList:
        #         print(char)
        #     print("self.minusIndexList:  ")
        #     for char in self.minusIndexList:
        #         print(char)

    # 字符串处理
    def strProcessing(self, string):
        # 将形如01的地方改成1
        toBeReplaced = ["0" + str(num) for num in range(10)]
        for i in range(10):
            string = string.replace(toBeReplaced[i], str(i))
        return string

    def getSpace2OneIndex(self):
        space2OneIndexList = []
        if self.checkEquator() and self.checkOperator():
            # 如果第二位为操作符
            if self.str[1] in operatorList:
                space2OneIndexList.append(0)
            # 如果倒数第二位为等号
            if self.str[-2] == "=":
                space2OneIndexList.append(-1)
            # 如果等号前两位为操作符
            if self.str[self.str.find("=") - 2] in operatorList:
                space2OneIndexList.append(self.str.find("=") - 1)
        return space2OneIndexList

    def getPlusTwoIndex(self):
        plusTwoIndexList=[]
        for index in range(len(self.str)):
            # 对每一位进行检查，如果可以PlusTwo就加入List里
            if isPlusTwoAble(self.str[index]):
                plusTwoIndexList.append(index)
        return plusTwoIndexList

    def getPlusIndex(self):
        plusIndexList=[]
        for index in range(len(self.str)):
            if isPlusAble(self.str[index]):
                plusIndexList.append(index)
        return plusIndexList

    def getMetaTwoIndex(self):
        metaTwoIndexList=[]
        for index in range(len(self.str)):
            if isMetaTwoAble(self.str[index]):
                metaTwoIndexList.append(index)
        return metaTwoIndexList

    def getMetaIndex(self):
        metaIndexList=[]
        for index in range(len(self.str)):
            if isMetaAble(self.str[index]):
                metaIndexList.append(index)
        return metaIndexList

    def getMinusTwoIndex(self):
        minusTwoIndexList=[]
        for index in range(len(self.str)):
            if isMinusTwoAble(self.str[index]):
                minusTwoIndexList.append(index)
        return minusTwoIndexList

    def getMinusIndex(self):
        minusIndexList=[]
        for index in range(len(self.str)):
            if isMinusAble(self.str[index]):
                minusIndexList.append(index)
        return minusIndexList

    def getMetaPlusIndex(self):
        metaPlusIndexList=[]
        for index in range(len(self.str)):
            if isMetaPlusAble(self.str[index]):
                metaPlusIndexList.append(index)
        return metaPlusIndexList
    
    def getMetaMinusIndex(self):
        metaMinusIndexList=[]
        for index in range(len(self.str)):
            if isMetaMinusAble(self.str[index]):
                metaMinusIndexList.append(index)
        return metaMinusIndexList

    # 检查等号
    def checkEquator(self):
        return self.str.count("=") == 1

    # 检查符号
    def checkOperator(self):
        operators = [self.str.count("+"), self.str.count("-"), self.str.count("×")]
        if operators in operatorCheckList:
            return True
        else:
            return False

    # 检查等式的正确性
    def checkRight(self):
        if self.checkEquator() and self.checkOperator():
            try:
                return eval(self.str.replace("=", "==").replace("×", "*"))
            except Exception as e:
                if DEBUG_MODE:
                    print(e)
                return False
        else:
            return False