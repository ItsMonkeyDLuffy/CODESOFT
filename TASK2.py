'''This project aims to create a simple calculator with basic arithmetic operations.'''

a = int(input("Write first no.:"))
b = int(input("Write second no.:"))
c = input("What do you want to do: +, -, *, / \n")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
else:
    print("Invalid Input")




