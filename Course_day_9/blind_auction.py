from art import logo
import os

def cls():
    """
    функция для очистки экрана
    """
    os.system('CLS')
#объявление переменных
ind = True
participants = {}
winner_name = ""
winner_bid = 0

#цикл сбора участников аукциона
while ind:
    print(logo)
    print("Welcome to the secret auction program.\n")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    participants[name] = bid

    other= input("Are there any other bidders? Type 'yes' or 'no'.\n ")
    if other == "no":
        cls()
        ind=False
    elif other == "yes":
        cls()

# определение победителя аукциона
for keys in participants:
    if participants[keys] > winner_bid:
        winner_bid = participants[keys]
        winner_name = keys
#вывод имени победителя
print(f"The winner is {winner_name} with a bid of {winner_bid}$.")
