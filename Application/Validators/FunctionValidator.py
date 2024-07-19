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
            if character not in ["x", "X", "+", "-", "*", "/", "^", "(", ")"] and not character.isdigit():
                return False, character
        return True, ""

    def validate(self, function):
        if not self.__validateBrackets__(function):
            return "Invalid Brackets"

        testCharacters, invalidCharacter = self.__validateCharacters__(function)
        if not testCharacters:
            return f"Invalid Character Found, {invalidCharacter} is invalid."

        return ""


validator = FunctionValidator()
print(validator.validate("X^2 + 4X + ( sqrt( log10(4)) ) x x x"))
