import os
from art import logo

def cls():
    """
    функция для очистки экрана
    """
    os.system('CLS')

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide,
}
def calculator():
    print(logo)
    num1 = round(float(input("What's the first number?: ")),2)
    num2 = round(float(input("What's the second number?: ")),2)

    ind = True

    for keys in operations:
        print(keys)
    operation_simbol = input("Pick an operation from the line above: ")
    wer = operations[operation_simbol]
    answer = wer(num1, num2)
    print(f"{num1} {operation_simbol} {num2} = {answer}")

    while ind:
        wont_to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if wont_to_continue == "n":
            cls()
            calculator()
        else:
            operation_simbol = input("Pick an operation from the line above: ")
            num2 = answer
            num3 = int(input("What's the second number?: "))
            wer2 = operations[operation_simbol]
            answer = wer2(num2, num3)
            print(f"{num2} {operation_simbol} {num3} = {answer}")
    print("exit")
calculator()
