from tkinter import *


def ml_to_km():
    ml = input_component.get()
    km = round(float(ml) * 1.609344)
    label3.config(text=km)


window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=400, height=100)
window.config(padx=100, pady=20)


input_component = Entry(width=10)
input_component.grid(column=1, row=0)

label = Label(text="Miles", font=("Arial", 10))
label.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Arial", 10))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("Arial", 10))
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=("Arial", 10))
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=ml_to_km)
button.grid(column=1, row=2)





window.mainloop()