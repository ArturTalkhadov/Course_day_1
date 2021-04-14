import random
import os
from art import logo

def cls():
    """
    функция для очистки экрана
    """
    os.system('CLS')

def append_card(spisok):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand = random.choice(cards)
    if sum(spisok)>10 and rand==11:
        return spisok.append(1)
    else:
        return spisok.append(rand)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

player_cards=[]
computer_cards=[]


def blackjack():
    ind = True
    end = True
    while ind:
        reason = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if reason == "n":
            ind = False
        else:
            cls()
            print(logo)
            ind = True
            end = True
            player_cards.clear()
            computer_cards.clear()
            #раздача 2 карты игроку и 2 диллеру:
            for i in range(2):
                append_card(player_cards)
                append_card(computer_cards)
            print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"    Computer's first card: {computer_cards[0]}")


            computer_score = calculate_score(computer_cards)


            while end:
                get_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if get_card == "y":
                    append_card(player_cards)
                    user_score = calculate_score(player_cards)
                    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
                    if user_score == 0 or computer_score == 0 or user_score>21:
                        end=False
                else:
                    end = False

                if computer_score != 0 and computer_score < 17:
                    append_card(computer_cards)


        print(f"    Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"    Computer's final hand: {computer_cards} final score: {sum(computer_cards)}")
        if sum(player_cards)>21:
            print("You went over. Player lose")

        elif sum(computer_cards)>21:
            print("Computer went over. Player win")

        if 21 >= sum(computer_cards)>sum(player_cards):
            print("Player lose")
        if 21 >= sum(player_cards)>sum(computer_cards):
            print("Player win")

blackjack()
