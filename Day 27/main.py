from tkinter import *


def button_clicked():
    my_label.config(text=f"{input.get()}")


window = Tk()
window.title("Program")
window.minsize(800, 550)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="I am a label", font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

#button Two
button_two = Button(text="rat")
button_two.grid(column=2, row=0)

# Other options to change text
my_label["text"] = "new text"
my_label.config(text="New Text")

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=20)
input.grid(column=3, row=2)


window.mainloop()