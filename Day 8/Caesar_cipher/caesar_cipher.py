alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
end_of_program = False


def caesar(start_text: str, shift_amount: int, cipher_direction: str): 
    if cipher_direction == "decode":
        shift_amount *= -1
    end_text: str = "" 
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]  
        else:
            end_text += char        
    print(f"Here's the {direction}d result: {end_text}")
    
while not end_of_program:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
        
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    reuse = input("Type 'yes' if you want to go again. Otherwise type 'no'?\n")
    if reuse == "no":
        end_of_program = True
        print("Goodbye")
    
