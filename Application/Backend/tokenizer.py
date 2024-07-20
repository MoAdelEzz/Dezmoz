import re

from Backend.equationResolver import EquationResolver
from Backend.stringUtils import findFirstOccurence, addMissingOperations


class Tokenizer:
    equation: str

    def __init__(self):
        self.equation = ""
        self.BR_ID = 0
        self.bracketDictionary = {}

    def __generalPreBracketTokenizer__(self, equation: str, fieldToken: str, lastId: int, keyword: str, tokenMap:dict):
        keywordLength = len(keyword)

        while True:
            idx = findFirstOccurence(equation, keyword)
            if idx == -1:
                break
            bracketEnd = equation[idx + keywordLength + 3:].find(";") + idx + keywordLength + 3
            tokenMap[f"{fieldToken};{lastId};"] = equation[idx + keywordLength: bracketEnd + 1]
            equation = equation.replace(equation[idx: bracketEnd + 1], f"{fieldToken};{lastId};")
            lastId += 1

        return equation, lastId

    BR_ID: int
    bracketDictionary: dict
    def __tokenizeBrackets__(self, equation=""):
        result = ""
        i = 0

        while i < len(equation):
            if equation[i] == "(":
                bracketStart = i
                count = 1
                while count:
                    i += 1
                    if equation[i] == "(":
                        count += 1
                    elif equation[i] == ")":
                        count -= 1

                self.bracketDictionary[f"BR;{self.BR_ID};"] = self.__tokenizeEquation__(equation[bracketStart + 1: i])
                result += f"BR;{self.BR_ID};"
                self.BR_ID += 1
            else:
                result += equation[i]
            i += 1

        return result

    LG_ID = 1
    logsTokens = {"LG;ID;": "X + 4 "}
    def __tokenizeLogs__(self, equation: str):
        result, self.LG_ID = self.__generalPreBracketTokenizer__(equation, "LG", self.LG_ID, "logDG;10;",
                                                                 self.logsTokens)
        return result

    RT_ID = 1
    rootTokens = {"PW;ID;": "X + 4 "}

    def __tokenizeRoots__(self, equation: str):
        result, self.RT_ID = self.__generalPreBracketTokenizer__(equation, "RW", self.RT_ID, "sqrt", self.rootTokens)
        return result

    def __tokenizeDigits__(self, equation: str):
        pattern = re.compile(r"\d+(\.\d+)?")

        i = 0
        result = ""
        while i < len(equation):
            if equation[i] == ".":
                if i == 0:
                    result += '0' + equation[i]
                elif i == len(equation) - 1:
                    result += equation[i]
                elif equation[i - 1].isdigit() and equation[i + 1].isdigit():
                    result += equation[i]
                elif equation[i + 1].isdigit():
                    result += '0' + equation[i]
                else:
                    result += equation[i] + '0'
            else:
                result += equation[i]
            i += 1
        equation = result

        def replace_non_matching(match):
            number = match.group()
            if pattern.match(number):
                return f"DG;{number};"
            return number

        result = re.sub(pattern, replace_non_matching, equation)
        result = result.replace("-", "+DG;0;-")

        return result

    def generateResolver(self):
        return EquationResolver(self.bracketDictionary, self.logsTokens, self.rootTokens, self.equation)

    def __tokenizeEquation__(self, equation: str):
        equation = self.__tokenizeBrackets__(equation)
        equation = self.__tokenizeLogs__(equation)
        equation = self.__tokenizeRoots__(equation)
        equation = addMissingOperations(equation)
        equation = self.removeExtraOperations(equation)

        return equation

    def removeExtraOperations(self, equation: str):
        i = 0
        result = ""

        while i < len(equation):
            if equation[i] not in ["+", "-", "*", "/", "^"]:
                result += equation[i]
            elif i > 0 and equation[i - 1] in [";", "x", "X"]:
                result += equation[i]
            i += 1
        return result

    def execute(self):
        self.equation = self.__tokenizeDigits__(self.equation)
        self.equation = self.__tokenizeEquation__(self.equation)
        return self.equation
