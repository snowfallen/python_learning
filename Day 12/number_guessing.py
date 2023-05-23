import random

EASY_LEVEL_OF_TURNS = 10
HARD_LEVEL_OF_TURNS = 7    
 

def difficulty():
    set_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if set_difficulty == "easy":
        return EASY_LEVEL_OF_TURNS
    else:
        return HARD_LEVEL_OF_TURNS


def guess(guess_number, number, turns):
    """ Returns numbers of turns remaining."""
    if  guess_number == number:
        print (f"You got it! The answer was {number}.")
    elif guess_number > number:
        print("Too high.")
        return turns - 1
    else:
        print("Too low.")
        return turns - 1


def game():
    print("Welcome to the Number Gueesing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)
    number_of_turns = difficulty()
    guess_number = 0
    while guess_number != number:
        print(f"You have {number_of_turns} attemps remaining to guees the number.")
        guess_number = int(input("Make a guess: "))
        number_of_turns = guess(guess_number, number, number_of_turns)
        if number_of_turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess_number != number:
            print("Guess again")


game()
