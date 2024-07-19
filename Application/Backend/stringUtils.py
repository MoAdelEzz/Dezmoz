import re


def findFirstOccurence(input_string: str, pattern=r''):
    match = re.search(pattern, input_string)
    return -1 if match is None else match.start()


def findLastOccurence(input_string: str, pattern=r''):
    matches = re.finditer(pattern, input_string)
    last_match = None
    for match in matches:
        last_match = match

    return -1 if last_match is None else last_match.start()


def addMissingOperations(equation: str):
    i = 0
    operands = ["X", "DG", "LG", "BR"]
    result = ""
    flag = False
    while i < len(equation):
        if equation[i].capitalize() == 'X' or equation[i: i + 2] in operands:
            operand = 'X' if equation[i].capitalize() == 'X' else equation[i: i + 2]
            withId = equation.find(";", i + len(operand) + 1) + 1 if operand != "X" else i + 1
            if flag:
                result = f"{result}*{equation[i: withId]}"
            else:
                result += equation[i: withId]
            flag = True
            i = withId
        else:
            result += equation[i]
            flag = False
            i += 1

    return result

def tokenizedStringToFloat(equation: str):
    if equation.startswith("N"):
        return float(equation[1:]) * -1
    else:
        return float(equation)
def formatNumber(number: float):
    formatted = ""
    if number == 0:
        return "0"

    if number < 0:
        formatted += 'N'
        number *= -1

    if number > 1:
        formatted += f"{number:.10f}".rstrip('0').rstrip('.')
    elif number == 1:
        formatted += "1"
    else:
        formatted += f"{number:.10f}".rstrip('0').rstrip('.')

    return formatted
