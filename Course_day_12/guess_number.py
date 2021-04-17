#from art import logo
import random
import os

def cls():
    """
    функция для очистки экрана
    """
    os.system('CLS')

def game_logic(attempts):
    global secret_number
    global ind
    i=attempts

    while i>=1:
        print(f"You have {i} attempts remaining to guess the number.")
        k = int(input("Make a guess: "))
        if k > secret_number:
            print("Too high")
        if k < secret_number:
            print("Too low")
        if k == secret_number:
            print("match")
            ind=False
            break
        i-=1
        if i == 0 and k != secret_number:
            print("you lose")


def guess_number():
    ind = True
    end = True
    while ind:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        reason = input("Choose a difficulty. Type 'easy' or 'hard':")
        if reason == "easy":
            attempts = 10
        if reason == "hard":
            attempts = 5
        game_logic(attempts)



ind = True
while ind:
    reason = input("Do you want to play a game of guess number? Type 'y' or 'n':")
    if reason == "n":
        ind = False
    else:
        cls()
        secret_number = random.randint(1,100)
        guess_number()
