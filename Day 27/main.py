from tkinter import *


def button_clicked():
    new_text = input_component.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 15))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me1")
new_button.grid(column=2, row=0)


# Entry component
input_component = Entry(width=10)
input_component.grid(column=3, row=1)
input_component.get()





window.mainloop()