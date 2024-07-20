class FunctionValidator:
    def __init__(self):
        return

    def __validateBrackets__(self, function: str):
        count = 0
        i = 0
        while i < len(function):
            if function[i] == '(':
                count += 1
            elif function[i] == ')':
                count -= 1
            i += 1
        return count == 0

    def __validateCharacters__(self, function: str):
        sandbox = function
        sandbox = sandbox.replace(" ", "").replace("log10", "").replace("sqrt", "")
        for character in sandbox:
            if character not in ["x", "X", "+", "-", "*", "/", "^", "(", ")", "."] and not character.isdigit():
                return False, character
        return True, ""

    def __validateDots__(self, function: str):
        i = 0
        if len(function) == 1 and function[0] == '.':
            return {False, 0}
        i = -1
        while i + 1 < len(function):
            i += 1
            character = function[i]
            if character == '.':
                if i == len(function) - 1 and function[i - 1].isdigit():
                    continue
                if i == 0 and function[i + 1].isdigit():
                    continue
                if function[i + 1].isdigit() or function[i - 1] == '.':
                    continue
                return False, i+1

        return True, None


    def validate(self, function: str):
        if not self.__validateBrackets__(function):
            return "Invalid Brackets"

        testCharacters, invalidCharacter = self.__validateCharacters__(function)
        if not testCharacters:
            return f"Invalid Character Found, {invalidCharacter} is invalid."

        testDots, invalidIdx = self.__validateDots__(function)
        if not testDots:
            return f"Invalid Dots Found, character @{invalidIdx + 1} is invalid."

        return ""


validator = FunctionValidator()
print(validator.validate("X^2 + 4X + ( sqrt( log10(4)) ) x x x"))
