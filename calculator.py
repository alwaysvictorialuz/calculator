number = int(input("first number"))
number2 = int(input("second number"))
function1 = input("multiply, add, divide, subtract?")

if function1 == "multiply":
    answer = number*number2
elif function1 == "add":
    answer = number+number2
elif function1 == "divide":
    answer = number//number2
else:
    answer = number-number2

print("answer:", int(answer))