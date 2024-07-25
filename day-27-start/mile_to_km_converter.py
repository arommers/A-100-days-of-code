from tkinter import *

def button_clicked():
    miles_input = float(input.get())
    km = round(miles_input * 1.609, 2)
    label_four.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

#Labels
label_one = Label(text="Is equal to", font=("Arial", 24, "bold"))
label_one.config(padx=10, pady=10)
label_one.grid(column=0, row=1)

label_two = Label(text="Miles", font=("Arial", 24, "bold"))
label_two.config(padx=10, pady=10)
label_two.grid(column=2, row=0)

label_three = Label(text="Km", font=("Arial", 24, "bold"))
label_three.config(padx=10, pady=10)
label_three.grid(column=2, row=1)

label_four = Label(text="0", font=("Arial", 24, "bold"))
label_four.config(padx=10, pady=10)
label_four.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()