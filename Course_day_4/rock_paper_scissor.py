import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
result = [["draw","you lose","you win!"],
          ["you win!","draw","you lose"],
          ["you lose","you win!","draw"],
         ]

choice_player = int(input("What do you choose& Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
if choice_player>2 or choice_player<0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[choice_player])
    choice_computer=random.randint(0,2)
    print(f"Computer chose:\n{game_images[choice_computer]}")
    print(f"result:\n{result[choice_player][choice_computer]}")
