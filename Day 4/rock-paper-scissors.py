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

rock_paper_scissors = [rock, paper, scissors]
user_select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_select = random.randint(0,2)
print(f"Computer choose :{rock_paper_scissors[computer_select]}")


if user_select >= 3 or user_select < 0:
     print("Yout typed invalid number. You lose!")
else: 
    print(rock_paper_scissors[user_select])

    if user_select == 0 and computer_select == 2:
        print("You Win!")
    elif computer_select == 0 and user_select == 2:
        print("You lose!")   
    elif computer_select > user_select:
        print("You Lose!")
    elif user_select > computer_select:
        print("You Win!")
    elif computer_select == user_select:
        print("Draw!")
