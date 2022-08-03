# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
# This is Bob project
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    if operator == '+':
        return int(num0) + int(num1)
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        print('unknown operator!')
        return None
    
    ## Add a test function
    def test():
        print("test")
