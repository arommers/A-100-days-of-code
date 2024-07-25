from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="Config Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

#New Button
newButton = Button(text="Click me too", command=button_clicked)
newButton.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()



