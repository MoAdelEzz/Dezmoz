from Backend.equationResolver import EquationResolver, LogarithmicError, RootError
from Backend.stringUtils import tokenizedStringToFloat
from Backend.tokenizer import Tokenizer


class Server:
    tokenizer: Tokenizer
    resolver: EquationResolver

    def __init__(self):
        self.tokenizer = Tokenizer()

    def setEquation(self, equation):
        preprocess = equation.replace(" ", "")
        preprocess = preprocess.replace("x", "X")
        self.tokenizer.equation = preprocess

    def __startTokenization__(self):
        return self.tokenizer.execute()

    def processEquation(self):
        self.__startTokenization__()

        self.resolver = self.tokenizer.generateResolver()

    def generatePlot(self, equation: str = "", x_min: float = 0.0, x_max: float = 10.0, steps: int = 10000):
        self.setEquation(equation)
        self.processEquation()
        
        stepSize = (x_max - x_min) / steps
        xList = []
        yList = []
        while x_min <= x_max:
            try:
                y = self.solveEquation(x_min)
                xList.append(x_min)
                yList.append(y)
            except ZeroDivisionError:
                pass
            except LogarithmicError:
                pass
            except RootError:
                pass
            x_min += stepSize
        return xList, yList

    def solveEquation(self, x):
        return tokenizedStringToFloat(self.resolver.f(x)[3: -1])
