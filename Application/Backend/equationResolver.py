import math
from Backend.stringUtils import formatNumber, findFirstOccurence, findLastOccurence, tokenizedStringToFloat


class LogarithmicError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class RootError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EquationResolver:
    __tokenizedEquation__: str
    __x__: float
    __bracketEquations__: dict
    __logsEquations__: dict
    __rootsEquations__: dict

    def __init__(self, bracketDict: dict, logsDict: dict, rootsDict: dict, tokenizedEquation: str):
        self.__tokenizedEquation__ = tokenizedEquation + "+DG;0;"
        self.__bracketEquations__ = bracketDict
        self.__logsEquations__ = logsDict
        self.__rootsEquations__ = rootsDict

    def __decodeOperand__(self, operand: str):

        if operand == 'X' or operand == 'x':
            return self.__x__

        answer = None
        if operand.startswith("BR"):
            answer = self.__resolveBrackets__(operand)[3: -1]
        if operand.startswith("LG"):
            answer = self.__resolveLogs__(operand)[3: -1]
        if operand.startswith("RW"):
            answer = self.__resolveRoots__(operand)[3: -1]
        if operand.startswith("DG"):
            answer = operand[3: -1]

        if answer is None:
            raise Exception("Unknown operand")

        return tokenizedStringToFloat(answer)

    def __generalResolver__(self, equation: str, operator: str):

        def executePower(op1: float, op2: float):
            return op1 ** op2

        def executeAddition(op1: float, op2: float):
            return op1 + op2

        def executeSubtraction(op1: float, op2: float):
            return op1 - op2

        def executeMultiplication(op1: float, op2: float):
            return op1 * op2

        def executeDivision(op1: float, op2: float):
            if op2 == 0:
                return -1 * 1e40 if op1 < 0 else 1e40
            return op1 / op2

        regex = r"[\^]" if operator == "^" else r"[\*/]" if operator in ["/", "*"] else r"[\+-]"
        allOperandsRegex = r'[+\-*/^]'

        while True:
            idx = findFirstOccurence(equation, regex)
            if idx == -1: break

            previousOperatorIdx = findLastOccurence(equation[:idx], allOperandsRegex)

            nextOperatorIdx = findFirstOccurence(equation[idx + 1:], allOperandsRegex)
            nextOperatorIdx = nextOperatorIdx + idx + 1 if nextOperatorIdx != -1 else len(equation)

            firstOperand = self.__decodeOperand__(equation[previousOperatorIdx + 1: idx])
            secondOperand = self.__decodeOperand__(equation[idx + 1: nextOperatorIdx])

            result = None
            if equation[idx] == "^":
                result = executePower(firstOperand, secondOperand)
            elif equation[idx] == "+":
                result = executeAddition(firstOperand, secondOperand)
            elif equation[idx] == "-":
                result = executeSubtraction(firstOperand, secondOperand)
            elif equation[idx] == "*":
                result = executeMultiplication(firstOperand, secondOperand)
            elif equation[idx] == "/":
                result = executeDivision(firstOperand, secondOperand)
            else:
                raise Exception("Invalid Equation Parsing")

            resultString = formatNumber(result)
            equation = equation[: previousOperatorIdx + 1] + f"DG;{resultString};" + equation[nextOperatorIdx:]
        return equation

    def __resolveBrackets__(self, operand: str):
        if not operand.startswith("BR"): return operand
        subEquation = self.__bracketEquations__[operand]
        return self.__solve__(subEquation, self.__x__)

    def __resolveLogs__(self, operand: str):
        if not operand.startswith("LG"): return operand
        internalEquation = self.__logsEquations__[operand]

        resultString = self.__resolveBrackets__(internalEquation)[3: -1]
        if resultString.startswith("N") or float(resultString) == 0:
            raise LogarithmicError("err")

        result = math.log10(tokenizedStringToFloat(resultString))

        resultString = formatNumber(result)
        return f"DG;{resultString};"

    def __resolveRoots__(self, operand: str):
        if not operand.startswith("RW"): return operand
        ## TODO: check if the internal part is negative
        internalEquation = self.__rootsEquations__[operand]
        resolvedEquation = tokenizedStringToFloat(self.__resolveBrackets__(internalEquation)[3: -1])
        if resolvedEquation < 0:
            raise RootError("Square Root Of Negative Value")
        result = math.sqrt(resolvedEquation)
        resultString = formatNumber(result)
        return f"DG;{resultString};"

    def __resolvePowers__(self, equation):
        return self.__generalResolver__(equation, operator='^')

    def __resolveMultiplicationAndDivision__(self, equation):
        return self.__generalResolver__(equation, operator='*')

    def __resolveAdditionAndSubtraction__(self, equation):
        return self.__generalResolver__(equation, operator="+")

    def __solve__(self, equation: str, x: float):
        equation = equation + "+DG;0;"
        self.__x__ = x
        equation = self.__resolvePowers__(equation)
        equation = self.__resolveMultiplicationAndDivision__(equation)
        equation = self.__resolveAdditionAndSubtraction__(equation)
        return equation

    def f(self, x: float):
        return self.__solve__(self.__tokenizedEquation__, x)
