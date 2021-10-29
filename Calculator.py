num1 = float(input("Enter first number: "))
operator = input("Enter operator (+,-,/,*): ")
num2 = float(input("Enter second number: "))

def calculator(num1,num2,operator):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "/":
        return num1/num2
    elif operator == "*":
        return num1*num2
    else:
        print("Invalid Operator!!!")

print(calculator(num1, num2, operator))