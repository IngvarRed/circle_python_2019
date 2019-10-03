# stupid calculator

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

# print(Back.BLUE)

what = input("prompt operatiom (+, -, *, /) : ")

# print(Back.CYAN)

a = float(input("enter the first number : "))
b = float(input("enter the second number : "))

# print(Fore.BLACK)
# print(Back.GREEN)

if what == "+":
    c = a + b
    print("rezult = " + str(c))
elif what == "-":
    c = a - b
    print("rezult = " + str(c))
elif what == "*":
    c = a * b
    print("rezult = " + str(c))
elif what == "/":
    c = a / b
    print("rezult = " + str(c))
else:
    print("wrong operation selected ! ")

# compile .py
# pip install pyinstaller
# pyinstaller -F "filename.py"