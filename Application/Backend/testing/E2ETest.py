import math
from Application.Backend.Server import Server

server = Server()

test_cases = [
    {"function": "(x + 3) * 2", "xValue": 5, "expected": (5 + 3) * 2},
    {"function": "(x - 2) ^ 3", "xValue": 4, "expected": (4 - 2) ** 3},
    {"function": "sqrt(x) + 4", "xValue": 25, "expected": math.sqrt(25) + 4},
    {"function": "log10(x) * (x - 1)", "xValue": 1000, "expected": math.log10(1000) * (1000 - 1)},
    {"function": "(x * (x - 1)) / 2", "xValue": 10, "expected": (10 * (10 - 1)) / 2},
    {"function": "sqrt(x ^ 2 + 4 * x + 4)", "xValue": 3, "expected": math.sqrt(3 ** 2 + 4 * 3 + 4)},
    {"function": "(x / 2) ^ 2 + 1", "xValue": 8, "expected": (8 / 2) ** 2 + 1},
    {"function": "sqrt((x + 2) ^ 2 - 4)", "xValue": 5, "expected": math.sqrt((5 + 2) ** 2 - 4)},
    {"function": "log10(sqrt(x + 1) * (x - 2))", "xValue": 100, "expected": math.log10(math.sqrt(100 + 1) * (100 - 2))},
    {"function": "((x ^ 2 + 1) / (x + 1)) * log10(x)", "xValue": 10, "expected": ((10 ** 2 + 1) / (10 + 1)) * math.log10(10)},
    {"function": "(x * (x / 2) - sqrt(x ^ 2 + x))", "xValue": 6, "expected": (6 * (6 / 2) - math.sqrt(6 ** 2 + 6))},
    {"function": "sqrt((x + 3) * (x - 2) / (x ^ 2 - 1))", "xValue": 4, "expected": math.sqrt((4 + 3) * (4 - 2) / (4 ** 2 - 1))},
    {"function": "log10(x ^ 2 + (x - 1) ^ 2) / sqrt(x)", "xValue": 25, "expected": math.log10(25 ** 2 + (25 - 1) ** 2) / math.sqrt(25)},
    {"function": "((x + sqrt(x ^ 2 + 4)) / 2) ^ 2 - 1", "xValue": 7, "expected": (((7 + math.sqrt(7 ** 2 + 4)) / 2) ** 2 - 1)},
]

for testCase in test_cases:
    equation, x, expected = testCase["function"], testCase["xValue"], testCase["expected"]
    server.setEquation(equation)
    server.processEquation()
    y = server.solveEquation(x)
    try:
        assert abs(y - expected) < 1e-5;
    except AssertionError:
        print(f"AssertionError: expected{expected}, found{y}, f(x) = {equation}, x = {x}")
        exit(400)

server.setEquation("1 / X")
server.processEquation()
server.generatePlot(x_min=0, x_max=20, steps=100)

