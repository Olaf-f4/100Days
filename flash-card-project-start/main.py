import time
from tkinter import *
from tkinter import messagebox
import random
import pandas as pd
import pyperclip
#------------Constants--------------#
BACKGROUND_COLOR = "#B1DDC6"
timer = 5

csv = pd.read_csv("data/Spanish_words.csv")
to_learn = csv.to.dict(orient="records")
print(to_learn)


# Flip card to back
    # How to flip card? We can flip the images after x seconds.
        # How do you get x seconds
# Red button = Don't know

def next_card():
    text_es = random.choice(csv["Spanish"])

# Green Button = You know

# ----------------------- UI SETUP
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Flash card Back
card_back = PhotoImage(file="images/card_back.png")
cb_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cb_canvas.create_image(400, 263, image=card_back)
word_text = cb_canvas.create_text(400, 270, text=text_es, font=(None, 60, 'bold'))
language_text = cb_canvas.create_text(400, 175, text="Español", font=(None, 25))
cb_canvas.grid(column=1, row=1, columnspan=2, pady=25)


# Flash Card Front
card_front = PhotoImage(file="images/card_front.png")
cf_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cf_canvas.create_image(400, 275, image=card_front)
english_word_text = cf_canvas.create_text(400, 275, text="goodbye")
#cf_canvas.grid(column=1, row=1)

# Correct Button
right_pic = PhotoImage(file="images/right.png")
right_button = Button(image=right_pic, height=85, width=90, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=2)

# Wrong Button
wrong_pic = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_pic, height=85, width=90, bg=BACKGROUND_COLOR, command=unknown)
wrong_button.grid(column=2, row=2)

window.mainloop()