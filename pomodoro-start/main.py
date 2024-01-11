from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    c_mark.config(text="")
    t_text.config(text="Pomodoro")
    canvas.itemconfig(timer_text, text="00:00")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        t_text.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        t_text.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        t_text.config(text="Work!", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # second
    if count_sec < 9 > 0:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    # Minute
    if count_min < 9 > 1:
        count_min = f"0{count_min}"
    elif count_min == 0:
        count_min = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        # ✔
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        c_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Text
t_text = Label(text="Timer", font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
t_text.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", highlightthickness=-20, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, bg=PINK, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Mark
c_mark = Label(text="", font=(None, 30), bg=YELLOW, fg=GREEN)
c_mark.grid(column=1, row=3)

window.mainloop()