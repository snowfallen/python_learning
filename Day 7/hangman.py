import random
import hangman_words
from hangman_art import stages, logo

word_list = hangman_words.word_list
lives = 6

print(logo)

chosen_word = random.choice(word_list)
world_length = len(chosen_word)

# create switch
end_of_game = False 

# create blanks 
display = []
for letter in range(world_length):
    display.append("_")
    
# use switch
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed - '{guess}'")
        
    # check guessed letter            
    for position in range(world_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"No match. Lives left {lives}")
        if lives == 0:
            end_of_game = True
            print("You Lose")
            
    print(f"{' '.join(display)}") 
     
    # check if a word has run out of letters
    if "_" not in display:
        end_of_game = True
        print("You Win")
        
    # ASCII check lives      
    print(stages[lives])
    