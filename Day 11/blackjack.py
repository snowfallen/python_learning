import random
from art import logo


def clear():
    print("\n" * 50)


def add_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        card = random.choice(cards)
        return card


def score(who_hand: list):
    if sum(who_hand) == 21 and len(who_hand) == 2:
        return 0
    if sum(who_hand) > 21 and 11 in who_hand:
        who_hand.remove(11)
        who_hand.append(1)
    return sum(who_hand)


def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "Lose opponent has a blackjack"
        elif user_score == 0:
            return "Win with a blackjack"
        elif user_score > 21:
            return "You went over. You lose"
        elif computer_score >21:
            return "Opponent went over. You win"
        elif user_score > computer_score:
            return "You Win"
        else:
            return "You lose"


def play_game():
    print(logo)  
    end_of_game = False
    user_hand = []
    computer_hand = []  
    
    for _ in range (2): 
        user_hand.append(add_card())
        computer_hand.append(add_card())

    while not end_of_game:
        
        user_score = score(user_hand)
        computer_score = score(computer_hand)
        print(f"  Your cards: {user_hand}, current score: {user_score}")
        print(f"  Computer first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_of_game = True
        else:
            user_should_deal = input("Type 'y' to get another card, type  'n' to pass: ")
            if user_should_deal == "y":
                user_hand.append(add_card())
            else:
                end_of_game = True

    while computer_score != 0 and  computer_score < 17:
        computer_hand.append(add_card())
        computer_score = score(computer_hand) 

    print(f"  Your final hand: {user_hand}, final score: {user_score}")
    print(f" Computer final hand: {computer_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
    clear()
    play_game()
