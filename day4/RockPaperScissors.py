import random

from pip._internal import self_outdated_check

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
computer_choice = rock
human_choice = scissors
number_selected_by_player = int(input(f"input a number {1} is rock,{2} is paper,{3} is scissors  "))
computer_number = random.randint(1,3)
if computer_number == 1:
    computer_choice = rock
    print(f"computers choice{computer_choice}")
elif computer_number == 2:
    computer_choice = paper
    print(f"computers choice{computer_choice}")
elif computer_number == 3:
    computer_choice = scissors
    print(f"computers choice{computer_choice}")
else:
    print("invalid choice")

if number_selected_by_player == 1:
        human_choice = rock
        print(f"human choice{human_choice}")
elif number_selected_by_player == 2:
        human_choice = paper
        print(f"human choice{human_choice}")
elif number_selected_by_player == 3:
        human_choice = scissors
        print(f"human choice{human_choice}")
else:
        print("invalid choice")

if computer_number == 1 and number_selected_by_player == 2:
    print("you win")
elif computer_number==2 and number_selected_by_player ==3:
    print("you win")
elif computer_number == 3 and number_selected_by_player == 1:
    print("you win")
elif computer_number == 3 and number_selected_by_player == 2:
    print("you lost")
else:
    print("sorry you lost")