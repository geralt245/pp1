import stack

def calculate(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2


operators = ["+", "-", "*", "/"]
while True:
    user_input = input("Enter something: ")
    
    if user_input == "":
        break
    elif user_input.isdigit():
        stack.push(user_input)
    elif user_input in operators:
        operand2 = int(stack.pop())
        operand1 = int(stack.pop())
        stack.push(calculate(user_input, operand1, operand2))
    elif user_input == "=":
        print(stack.pop())
    else:
        print("Wrong input")
        continue