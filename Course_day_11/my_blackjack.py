import random

def append_card(spisok):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand = random.choice(cards)
    if sum(spisok)>10 and rand==11:
        return spisok.append(1)
    else:
        return spisok.append(rand)

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
            ind = True
            end = True
            player_cards.clear()
            computer_cards.clear()
            append_card(player_cards)
            append_card(player_cards)
            append_card(computer_cards)
            print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"    Computer's first card: {sum(computer_cards)}")
            while end:
                get_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if get_card == "y":
                    append_card(player_cards)
                    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
                else:
                    end = False

            if sum(player_cards)<21:
                while sum(computer_cards) <= 14:
                        append_card(computer_cards)

            else:
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
