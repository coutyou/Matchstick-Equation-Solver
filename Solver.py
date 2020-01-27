from Equation import *

class Solver(object):
    # 字符串替换函数
    def replace_char(self, string, char, index):
        str_list = list(string)
        str_list[index] = char
        return ''.join(str_list)

    # 字符串插入函数
    def insert_char(self, string, char, index):
        str_list = list(string)
        str_list.insert(index, char)
        return ''.join(str_list)

    def plusAndMinus(self, equation):
        resultPlusAndMinus = []
        difficultyPlusAndMinus = 0
        if equation.plusIndexList != []:
            # 找到所有可以进行Plus操作的Char的Index
            for index in equation.plusIndexList:
                for plusChar in plusTable[equation.str[index]]:
                    # 对每个可以进行Plus操作的Char，用其所有可以变成的Char进行替换，生成新的Equation
                    newPlusEquation = Equation(self.replace_char(equation.str, plusChar, index))
                    if newPlusEquation.minusIndexList != []:
                        # 在新的等式中，找到所有可以进行Minus操作的Char的Index
                        for newIndex in newPlusEquation.minusIndexList:
                            # 为减少重复，要求这里的Index与之前不同
                            if newIndex != index:
                                # 对每个可以进行Minus操作的Char，用其所有可以变成的Char进行替换，生成新的Equation
                                for minusChar in minusTable[newPlusEquation.str[newIndex]]:
                                    newEquation = Equation(self.replace_char(newPlusEquation.str, minusChar, newIndex))
                                    if DEBUG_MODE:
                                        print("plusAndMinus:  ", newEquation.str, end="")
                                        if newEquation.checkRight():
                                            print(" Save!")
                                        else:
                                            print(" Drop")
                                    # 如果正确，加入结果List
                                    if newEquation.checkRight():
                                        resultPlusAndMinus.append(newEquation)
                                    difficultyPlusAndMinus += 1
        return difficultyPlusAndMinus, resultPlusAndMinus

    def meta(self, equation):
        resultMeta = []
        difficultyMeta = 0
        if equation.metaIndexList != []:
            for index in equation.metaIndexList:
                for metaChar in metaTable[equation.str[index]]:
                    newEquation = Equation(self.replace_char(equation.str, metaChar, index))
                    if DEBUG_MODE:
                        print("meta:  ", newEquation.str, end="")
                        if newEquation.checkRight():
                            print(" Save!")
                        else:
                            print(" Drop")
                    if newEquation.checkRight():
                        resultMeta.append(newEquation)
                    difficultyMeta += 1
        return difficultyMeta, resultMeta

    # 一根火柴的解法
    def extern(self, equation):
        # 拿到所有可能情况的结果和难度，并进行汇总
        result = []
        difficultyMeta, resultMeta = self.meta(equation)
        difficultyPlusAndMinus, resultPlusAndMinus = self.plusAndMinus(equation)
        result.extend(resultMeta)
        result.extend(resultPlusAndMinus)
        difficulty = difficultyMeta + difficultyPlusAndMinus
        if DEBUG_MODE:
            print("Result of extern:")
            for e in result:
                print(e.str)
        return difficulty, result

    def metaTwo(self, equation):
        resultMetaTwo = []
        difficultyMetaTwo = 0
        if equation.metaTwoIndexList != []:
            for index in equation.metaTwoIndexList:
                for metaTwoChar in metaTwoTable[equation.str[index]]:
                    newEquation = Equation(self.replace_char(equation.str, metaTwoChar, index))
                    if DEBUG_MODE:
                        print("metaTwo:  ", newEquation.str, end="")
                        if newEquation.checkRight():
                            print(" Save!")
                        else:
                            print(" Drop")
                    if newEquation.checkRight():
                        resultMetaTwo.append(newEquation)
                    difficultyMetaTwo += 1
        return difficultyMetaTwo, resultMetaTwo

    def metaAndMeta(self, equation):
        resultMetaAndMeta = []
        difficultyMetaAndMeta = 0
        if equation.metaIndexList != []:
            for index in equation.metaIndexList:
                for metaChar in metaTable[equation.str[index]]:
                    newMetaEquation = Equation(self.replace_char(equation.str, metaChar, index))
                    if newMetaEquation.metaIndexList != []:
                        for newMetaIndex in newMetaEquation.metaIndexList:
                            if newMetaIndex != index:
                                for newMetaChar in metaTable[newMetaEquation.str[newMetaIndex]]:
                                    newEquation = Equation(self.replace_char(newMetaEquation.str, newMetaChar, newMetaIndex))
                                    if DEBUG_MODE:
                                        print("metaAndMeta:  ", newEquation.str, end="")
                                        if newEquation.checkRight():
                                            print(" Save!")
                                        else:
                                            print(" Drop")
                                    if newEquation.checkRight():
                                        resultMetaAndMeta.append(newEquation)
                                    difficultyMetaAndMeta += 1
        return difficultyMetaAndMeta, resultMetaAndMeta

    def plusTwoAndMinusAndMinus(self, equation):
        resultPlusTwoAndMinusAndMinus = []
        difficultyPlusTwoAndMinusAndMinus = 0
        if equation.plusTwoIndexList != []:
            for index in equation.plusTwoIndexList:
                for plusTwoChar in plusTwoTable[equation.str[index]]:
                    newPlusTwoEquation = Equation(self.replace_char(equation.str, plusTwoChar, index))
                    if newPlusTwoEquation.minusIndexList != []:
                        for newIndex in newPlusTwoEquation.minusIndexList:
                            if newIndex != index:
                                for minusChar in minusTable[newPlusTwoEquation.str[newIndex]]:
                                    newPlusTwoAndMinusEquation = Equation(self.replace_char(newPlusTwoEquation.str, minusChar, newIndex))
                                    if newPlusTwoAndMinusEquation.minusIndexList != []:
                                        for newNewIndex in newPlusTwoAndMinusEquation.minusIndexList:
                                            if newNewIndex != newIndex and newNewIndex != index:
                                                for newMinusChar in minusTable[newPlusTwoAndMinusEquation.str[newNewIndex]]:
                                                    newEquation = Equation(self.replace_char(newPlusTwoAndMinusEquation.str, newMinusChar, newNewIndex))
                                                    if DEBUG_MODE:
                                                        print("PlusTwoAndMinusAndMinus:  ", newEquation.str, end="")
                                                        if newEquation.checkRight():
                                                            print(" Save!")
                                                        else:
                                                            print(" Drop")
                                                    if newEquation.checkRight():
                                                        resultPlusTwoAndMinusAndMinus.append(newEquation)
                                                    difficultyPlusTwoAndMinusAndMinus += 1
        return difficultyPlusTwoAndMinusAndMinus, resultPlusTwoAndMinusAndMinus

    def plusTwoAndMinusTwo(self, equation):
        resultPlusTwoAndMinusTwo = []
        difficultyPlusTwoAndMinusTwo = 0
        if equation.plusTwoIndexList != []:
            for index in equation.plusTwoIndexList:
                for plusTwoChar in plusTwoTable[equation.str[index]]:
                    newPlusTwoEquation = Equation(self.replace_char(equation.str, plusTwoChar, index))
                    if newPlusTwoEquation.minusTwoIndexList != []:
                        for newIndex in newPlusTwoEquation.minusTwoIndexList:
                            if newIndex != index:
                                for minusTwoChar in minusTwoTable[newPlusTwoEquation.str[newIndex]]:
                                    newEquation = Equation(self.replace_char(newPlusTwoEquation.str, minusTwoChar, newIndex))
                                    if DEBUG_MODE:
                                        print("plusTwoAndMinusTwo:  ", newEquation.str, end="")
                                        if newEquation.checkRight():
                                            print(" Save!")
                                        else:
                                            print(" Drop")
                                    if newEquation.checkRight():
                                        resultPlusTwoAndMinusTwo.append(newEquation)
                                    difficultyPlusTwoAndMinusTwo += 1
        return difficultyPlusTwoAndMinusTwo, resultPlusTwoAndMinusTwo

    def minusTwoAndPlusAndPlus(self, equation):
        resultMinusTwoAndPlusAndPlus = []
        difficultyMinusTwoAndPlusAndPlus = 0
        if equation.minusTwoIndexList != []:
            for index in equation.minusTwoIndexList:
                for minusTwoChar in minusTwoTable[equation.str[index]]:
                    newMinusTwoEquation = Equation(self.replace_char(equation.str, minusTwoChar, index))
                    if newMinusTwoEquation.plusIndexList != []:
                        for newIndex in newMinusTwoEquation.plusIndexList:
                            if newIndex != index:
                                for plusChar in plusTable[newMinusTwoEquation.str[newIndex]]:
                                    newMinusTwoAndPlusEquation = Equation(self.replace_char(newMinusTwoEquation.str, plusChar, newIndex))
                                    if newMinusTwoAndPlusEquation.plusIndexList != []:
                                        for newNewIndex in newMinusTwoAndPlusEquation.plusIndexList:
                                            if newNewIndex != newIndex and newNewIndex != index:
                                                for newPlusChar in plusTable[newMinusTwoAndPlusEquation.str[newNewIndex]]:
                                                    newEquation = Equation(self.replace_char(newMinusTwoAndPlusEquation.str, newPlusChar, newNewIndex))
                                                    if DEBUG_MODE:
                                                        print("minusTwoAndPlusAndPlus:  ", newEquation.str, end="")
                                                        if newEquation.checkRight():
                                                            print(" Save!")
                                                        else:
                                                            print(" Drop")
                                                    if newEquation.checkRight():
                                                        resultMinusTwoAndPlusAndPlus.append(newEquation)
                                                    difficultyMinusTwoAndPlusAndPlus += 1
        return difficultyMinusTwoAndPlusAndPlus, resultMinusTwoAndPlusAndPlus

    def metaAndPlusAndMinus(self, equation):
        resultMetaAndPlusAndMinus = []
        difficultyMetaAndPlusAndMinus = 0
        if equation.metaIndexList != []:
            for index in equation.metaIndexList:
                for metaChar in metaTable[equation.str[index]]:
                    newMetaEquation = Equation(self.replace_char(equation.str, metaChar, index))
                    if newMetaEquation.plusIndexList != []:
                        for newIndex in newMetaEquation.plusIndexList:
                            for plusChar in plusTable[newMetaEquation.str[newIndex]]:
                                newMetaAndPlusEquation = Equation(self.replace_char(newMetaEquation.str, plusChar, newIndex))
                                if newMetaAndPlusEquation.minusIndexList != []:
                                    for newNewIndex in newMetaAndPlusEquation.minusIndexList:
                                        if newNewIndex != newIndex:
                                            for minusChar in minusTable[newMetaAndPlusEquation.str[newNewIndex]]:
                                                newEquation = Equation(self.replace_char(newMetaAndPlusEquation.str, minusChar, newNewIndex))
                                                if DEBUG_MODE:
                                                    print("metaAndPlusAndMinus:  ", newEquation.str, end="")
                                                    if newEquation.checkRight():
                                                        print(" Save!")
                                                    else:
                                                        print(" Drop")
                                                if newEquation.checkRight():
                                                    resultMetaAndPlusAndMinus.append(newEquation)
                                                difficultyMetaAndPlusAndMinus += 1
        return difficultyMetaAndPlusAndMinus, resultMetaAndPlusAndMinus

    def plusAndMinusAndMeta(self, equation):
        resultPlusAndMinusAndMeta = []
        difficultyPlusAndMinusAndMeta = 0
        if equation.plusIndexList != []:
            for index in equation.plusIndexList:
                for plusChar in plusTable[equation.str[index]]:
                    newPlusEquation = Equation(self.replace_char(equation.str, plusChar, index))
                    if newPlusEquation.minusIndexList != []:
                        for newIndex in newPlusEquation.minusIndexList:
                            if newIndex != index:
                                for minusChar in minusTable[newPlusEquation.str[newIndex]]:
                                    newPlusAndMinusEquation = Equation(self.replace_char(newPlusEquation.str, minusChar, newIndex))
                                    if newPlusAndMinusEquation.metaIndexList != []:
                                        for newNewIndex in newPlusAndMinusEquation.metaIndexList:
                                            for metaChar in metaTable[newPlusAndMinusEquation.str[newNewIndex]]:
                                                newEquation = Equation(self.replace_char(newPlusAndMinusEquation.str, metaChar, newNewIndex))
                                                if DEBUG_MODE:
                                                    print("plusAndMinusAndMeta:  ", newEquation.str, end="")
                                                    if newEquation.checkRight():
                                                        print(" Save!")
                                                    else:
                                                        print(" Drop")
                                                if newEquation.checkRight():
                                                    resultPlusAndMinusAndMeta.append(newEquation)
                                                difficultyPlusAndMinusAndMeta += 1
        return difficultyPlusAndMinusAndMeta, resultPlusAndMinusAndMeta

    def metaPlusAndMinus(self, equation):
        resultMetaPlusAndMinus = []
        difficultyMetaPlusAndMinus = 0
        if equation.metaPlusIndexList != []:
            for index in equation.metaPlusIndexList:
                for metaPlusChar in metaPlusTable[equation.str[index]]:
                    newMetaPlusEquation = Equation(self.replace_char(equation.str, metaPlusChar, index))
                    if newMetaPlusEquation.minusIndexList != []:
                        for newIndex in newMetaPlusEquation.minusIndexList:
                            if newIndex != index:
                                for minusChar in minusTable[newMetaPlusEquation.str[newIndex]]:
                                    newEquation = Equation(self.replace_char(newMetaPlusEquation.str, minusChar, newIndex))
                                    if DEBUG_MODE:
                                        print("metaPlusAndMinus:  ", newEquation.str, end="")
                                        if newEquation.checkRight():
                                            print(" Save!")
                                        else:
                                            print(" Drop")
                                    if newEquation.checkRight():
                                        resultMetaPlusAndMinus.append(newEquation)
                                    difficultyMetaPlusAndMinus += 1
        return difficultyMetaPlusAndMinus, resultMetaPlusAndMinus

    def metaMinusAndPlus(self, equation):
        resultMetaMinusAndPlus = []
        difficultyMetaMinusAndPlus = 0
        if equation.metaMinusIndexList != []:
            for index in equation.metaMinusIndexList:
                for metaMinusChar in metaMinusTable[equation.str[index]]:
                    newMetaMinusEquation = Equation(self.replace_char(equation.str, metaMinusChar, index))
                    if newMetaMinusEquation.plusIndexList != []:
                        for newIndex in newMetaMinusEquation.plusIndexList:
                            if newIndex != index:
                                for plusChar in plusTable[newMetaMinusEquation.str[newIndex]]:
                                    newEquation = Equation(self.replace_char(newMetaMinusEquation.str, plusChar, newIndex))
                                    if DEBUG_MODE:
                                        print("metaMinusAndPlus:  ", newEquation.str, end="")
                                        if newEquation.checkRight():
                                            print(" Save!")
                                        else:
                                            print(" Drop")
                                    if newEquation.checkRight():
                                        resultMetaMinusAndPlus.append(newEquation)
                                    difficultyMetaMinusAndPlus += 1
        return difficultyMetaMinusAndPlus, resultMetaMinusAndPlus

    def space2OneAndMinusTwo(self, equation):
        resultSpace2OneAndMinusTwo = []
        difficultySpace2OneAndMinusTwo = 0
        if equation.space2OneIndexList != []:
            for index in equation.space2OneIndexList:
                newSpace2OneEquation = Equation(self.insert_char(equation.str, "1", index))
                if newSpace2OneEquation.minusTwoIndexList != []:
                    for newIndex in newSpace2OneEquation.minusTwoIndexList:
                        if newIndex != index:
                            for minusTwoChar in minusTwoTable[newSpace2OneEquation.str[newIndex]]:
                                newEquation = Equation(self.replace_char(newSpace2OneEquation.str, minusTwoChar, newIndex))
                                if DEBUG_MODE:
                                    print("space2OneAndMinusTwo:  ", newEquation.str, end="")
                                    if newEquation.checkRight():
                                        print(" Save!")
                                    else:
                                        print(" Drop")
                                if newEquation.checkRight():
                                    resultSpace2OneAndMinusTwo.append(newEquation)
                                difficultySpace2OneAndMinusTwo += 1
        return difficultySpace2OneAndMinusTwo, resultSpace2OneAndMinusTwo
    def plusAndMinusAndPlusAndMinus(self, equation):
        resultPlusAndMinusAndPlusAndMinus = []
        difficultyPlusAndMinusAndPlusAndMinus = 0
        if equation.plusIndexList != []:
            # 找到所有可以进行Plus操作的Char的Index
            for index in equation.plusIndexList:
                for plusChar in plusTable[equation.str[index]]:
                    # 对每个可以进行Plus操作的Char，用其所有可以变成的Char进行替换，生成新的Equation
                    plusEquation = Equation(self.replace_char(equation.str, plusChar, index))
                    if plusEquation.minusIndexList != []:
                        # 在新的等式中，找到所有可以进行Minus操作的Char的Index
                        for minusIndex in plusEquation.minusIndexList:
                            # 为减少重复，要求这里的Index与之前不同
                            if minusIndex != index:
                                # 对每个可以进行Minus操作的Char，用其所有可以变成的Char进行替换，生成新的Equation
                                for minusChar in minusTable[plusEquation.str[minusIndex]]:
                                    minusEquation = Equation(self.replace_char(plusEquation.str, minusChar, minusIndex))                          
                                    if minusEquation.plusIndexList != []:
                                        for newIndex in minusEquation.plusIndexList:
                                            for newPlusChar in plusTable[minusEquation.str[newIndex]]:
                                                newPlusEquation = Equation(self.replace_char(minusEquation.str, newPlusChar, newIndex))
                                                if newPlusEquation.minusIndexList != []:
                                                    for newMinusIndex in newPlusEquation.minusIndexList:
                                                        if newMinusIndex != newIndex:
                                                            for newMinusChar in minusTable[newPlusEquation.str[newMinusIndex]]:
                                                                newEquation = Equation(self.replace_char(newPlusEquation.str, newMinusChar, newMinusIndex))
                                                                if DEBUG_MODE:
                                                                    print("plusAndMinusAndPlusAndMinus:  ", newEquation.str, end="")
                                                                    if newEquation.checkRight():
                                                                        print(" Save!")
                                                                    else:
                                                                        print(" Drop")
                                                                # 如果正确，加入结果List
                                                                if newEquation.checkRight():
                                                                    resultPlusAndMinusAndPlusAndMinus.append(newEquation)
                                                                difficultyPlusAndMinusAndPlusAndMinus += 1
        return difficultyPlusAndMinusAndPlusAndMinus, resultPlusAndMinusAndPlusAndMinus

    # 两根火柴的解法
    def externTwo(self, equation):
        # 拿到所有可能情况的结果和难度，并进行汇总
        result = []
        difficultyExtern, resultExtern = self.extern(equation)
        difficultyMetaTwo, resultMetaTwo = self.metaTwo(equation)
        difficultyMetaAndMeta, resultMetaAndMeta = self.metaAndMeta(equation)
        difficultyPlusTwoAndMinusAndMinus, resultPlusTwoAndMinusAndMinus = self.plusTwoAndMinusAndMinus(equation)
        difficultyPlusTwoAndMinusTwo, resultPlusTwoAndMinusTwo = self.plusTwoAndMinusTwo(equation)
        difficultyMinusTwoAndPlusAndPlus, resultMinusTwoAndPlusAndPlus = self.minusTwoAndPlusAndPlus(equation)
        difficultyMetaAndPlusAndMinus, resultMetaAndPlusAndMinus = self.metaAndPlusAndMinus(equation)
        difficultyPlusAndMinusAndMeta, resultPlusAndMinusAndMeta = self.plusAndMinusAndMeta(equation)
        difficultyMetaPlusAndMinus, resultMetaPlusAndMinus = self.metaPlusAndMinus(equation)
        difficultyMetaMinusAndPlus, resultMetaMinusAndPlus = self.metaMinusAndPlus(equation)
        difficultySpace2OneAndMinusTwo, resultSpace2OneAndMinusTwo = self.space2OneAndMinusTwo(equation)
        difficultyPlusAndMinusAndPlusAndMinus, resultPlusAndMinusAndPlusAndMinus = self.plusAndMinusAndPlusAndMinus(equation)
        result.extend(resultExtern)
        result.extend(resultMetaTwo)
        result.extend(resultMetaAndMeta)
        result.extend(resultPlusTwoAndMinusAndMinus)
        result.extend(resultPlusTwoAndMinusTwo)
        result.extend(resultMinusTwoAndPlusAndPlus)
        result.extend(resultMetaAndPlusAndMinus)
        result.extend(resultPlusAndMinusAndMeta)
        result.extend(resultMetaPlusAndMinus)
        result.extend(resultMetaMinusAndPlus)
        result.extend(resultSpace2OneAndMinusTwo)
        result.extend(resultPlusAndMinusAndPlusAndMinus)
        difficulty = difficultyExtern + difficultyMetaTwo + difficultyMetaAndMeta + difficultyPlusTwoAndMinusAndMinus \
            + difficultyPlusTwoAndMinusTwo + difficultyMinusTwoAndPlusAndPlus + difficultyMetaAndPlusAndMinus + difficultyPlusAndMinusAndMeta \
            + difficultyMetaPlusAndMinus + difficultyMetaMinusAndPlus + difficultySpace2OneAndMinusTwo + difficultyPlusAndMinusAndPlusAndMinus
        if DEBUG_MODE:
            print("Result of externTwo:")
            for e in result:
                print(e.str)
        return difficulty, result

    # 根据参数调用不同的解题函数
    def solve(self, equation, matchNum=1):
        result_str = []
        difficulty = 0
        if matchNum == 1:
            difficulty, result = self.extern(equation)
            for e in result:
                result_str.append(e.str)
        elif matchNum == 2:
            difficulty, result = self.externTwo(equation)
            for e in result:
                result_str.append(e.str)
        else:
            # if more matchNum permitted
            pass
        return difficulty, result_str