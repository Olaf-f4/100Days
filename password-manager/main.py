from tkinter import messagebox
from tkinter import *
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    p_entry.delete(0, END)
    p_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_entry = w_entry.get().lower()
    email_entry = eu_entry.get()
    password_entry = p_entry.get()
    new_data = {
        website_entry: {
            "email": email_entry,
            "password": password_entry,
        }
    }

    # response = messagebox.askokcancel(website_entry, "Is that information correct?")

    if len(website_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo("Oops", "Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading Old Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updating data
                json.dump(data, data_file, indent=4)
        finally:
            w_entry.delete(0, END)
            p_entry.delete(0, END)

# ---------------------------- Search Password ------------------------------- #
def search_password():
    try:
        with open("data.json", "r")as p_file:
            p_list = json.load(p_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "You have no passwords")
    else:
        website = w_entry.get().lower()
        if website in p_list:
            s_email = p_list[website]["email"]
            s_password = p_list[website]["password"]
            messagebox.showinfo(website, f"Email: {s_email}\n"
                                         f"Password: {s_password}")
        else:
            print("Password not found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

# Picture
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website Text
w_text = Label(text="Website: ", font=(None, 22, 'bold'))
w_text.grid(column=0, row=1)

# Website Chat Entry
w_entry = Entry(width=23)
w_entry.grid(column=1, row=1, columnspan=1)
w_entry.focus()

# Email/Username Text
eu_text = Label(text="Email/Username: ", font=(None, 22, 'bold'))
eu_text.grid(column=0, row=2)

# Email/Username Entry
eu_entry = Entry(width=40)
eu_entry.grid(column=1, row=2, columnspan=2)
eu_entry.insert(0, "olafsenb@yahoo.com")

# Password Text
password_text = Label(text="Password: ", font=(None, 22, 'bold'))
password_text.grid(column=0, row=3)

# Password Entry
p_entry = Entry(width=23)
p_entry.grid(column=1, row=3)

# Search Password Button
s_password = Button(text="Search", width=13, highlightthickness=0, command=search_password)
s_password.grid(column=2, row=1)

# Generate Password Button
gen_password = Button(text="Generate Password", highlightthickness=0, command=pass_gen)
gen_password.grid(column=2, row=3)

# Add Password Button
add_password = Button(text="Add", highlightthickness=0, width=30, command=save_password)
add_password.grid(column=1, row=4, columnspan=2)

window.mainloop()