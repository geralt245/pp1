import stack

number_to_convert = int(input("Enter a number to convert: "))
print(f"Natural number: {number_to_convert}")

while number_to_convert > 0:
    remainder = number_to_convert % 2
    stack.push(remainder)
    number_to_convert = number_to_convert // 2

binary = ""

while stack.empty() == False:
    binary += str(stack.pop())


print(f"Binary number: {binary}")