from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------------- READING FILE ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    fr_word = current_card["French"]
    canvas.itemconfig(image, image=front_image)
    canvas.itemconfig(word_text, text=fr_word, fill="black")
    canvas.itemconfig(lang_text, text="French", fill="black")
    window.after(3000, flip_card)

# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #

def is_known():
    to_learn.remove(current_card)
    next_card()
    print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    print()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.after(3000, flip_card)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right.grid(row=1, column=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card )
wrong.grid(row=1, column=1)

back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
image = canvas.create_image(400, 263, image=front_image)
lang_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=2)

next_card()


window.mainloop()
