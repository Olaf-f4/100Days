from tkinter import *


def button_clicked():
    conversion = float(text_box.get()) * 1.609344
    text_snip3.config(text=f"{conversion}")


window = Tk()
window.title("Mile-To-Kilometer")
window.minsize(800, 550)
window.config(padx=20, pady=20)

text_box = Entry(width=10)
text_box.grid(column=1, row=0)

text_snip = Label(text="Miles", font=('Arial', 24, 'bold'))
text_snip.grid(column=2, row=0)

text_snip2 = Label(text="is equal to", font=('Arial', 24, 'bold'))
text_snip2.grid(column=0, row=1)

text_snip3 = Label(text=f"", font=('Arial', 24, 'bold'))
text_snip3.grid(column=1, row=1)

text_snip4 = Label(text="Km", font=('Arial', 24, 'bold'))
text_snip4.grid(column=2, row=2)

button = Button(text="calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()