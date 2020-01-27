# 定义了各种表格、常量和小函数

DEBUG_MODE = 0

plusTwoTable = {
"0":[],
"1":["4"],
"2":["8"],
"3":["8"],
"4":["9"],
"5":["8"],
"6":[],
"7":["3"],
"8":[],
"9":[],
"+":[],
"-":[],
"×":[],
"=":[]}

plusTable = {
"0":["8"],
"1":["7"],
"2":[],
"3":["9"],
"4":[],
"5":["9", "6"],
"6":["8"],
"7":[],
"8":[],
"9":["8"],
"+":[],
"-":["+", "="],
"×":[],
"=":[]}

metaTwoTable = {
"0":[],
"1":[],
"2":["5"],
"3":[],
"4":[],
"5":["2"],
"6":[],
"7":[],
"8":[],
"9":[],
"+":["×"],
"-":[],
"×":["+"],
"=":["+", "×"]}

metaTable = {
"0":["6", "9"],
"1":[],
"2":["3"],
"3":["2", "5"],
"4":[],
"5":["3"],
"6":["0", "9"],
"7":[],
"8":[],
"9":["0", "6"],
"+":["="],
"-":[],
"×":[],
"=":["+"]}

minusTwoTable = {
"0":[],
"1":[""],
"2":[],
"3":["7"],
"4":["1"],
"5":[],
"6":[],
"7":[],
"8":["2", "3", "5"],
"9":["4"],
"+":[],
"-":[],
"×":[],
"=":[]}

minusTable = {
"0":[],
"1":[],
"2":[],
"3":[],
"4":[],
"5":[],
"6":["5"],
"7":["1"],
"8":["0", "6", "9"],
"9":["3", "5"],
"+":["-"],
"-":[],
"×":[],
"=":["-"]}

metaPlusTable = {
"0":[],
"1":[],
"2":["6", "0", "9"],
"3":["6", "0"],
"4":["3", "5"],
"5":["0"],
"6":[],
"7":["4"],
"8":[],
"9":[],
"+":[],
"-":[],
"×":[],
"=":[]}

metaMinusTable = {
"0":["2", "3", "5"],
"1":[],
"2":[],
"3":["4"],
"4":["7", "9"],
"5":["4"],
"6":["2", "3"],
"7":[],
"8":[],
"9":["2"],
"+":[],
"-":[],
"×":[],
"=":[]}

def isPlusTwoAble(char):
    return plusTwoTable[char] != []

def isPlusAble(char):
    return plusTable[char] != []

def isMetaTwoAble(char):
    return metaTwoTable[char] != []

def isMetaAble(char):
    return metaTable[char] != []

def isMinusTwoAble(char):
    return minusTwoTable[char] != []

def isMinusAble(char):
    return minusTable[char] != []

def isMetaPlusAble(char):
    return metaPlusTable[char] != []

def isMetaMinusAble(char):
    return metaMinusTable[char] != []

numList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

operatorList = ["+", "-", "×"]

operatorCheckList = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def isNum(char):
    return char in numList

def isOperator(char):
    return char in operatorList

def isEquator(char):
    return char == "="