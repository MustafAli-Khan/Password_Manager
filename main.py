from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    Password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        Website_input.get():
            {
                "email": Email_input.get(),
                "password": Password_input.get()
            }
    }

    if len(Website_input.get()) == 0 or len(Password_input.get()) == 0:
        messagebox.showinfo("Oops", "Please enter your website and your password")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading Old Data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)

        else:
            # Updating Old Data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            Website_input.delete(0, END)
            Password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = Website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Helvetica", 20))
website_label.grid(column=0, row=1)

Email_label = Label(text="Email/Username:", font=("Helvetica", 20))
Email_label.grid(column=0, row=2)

Password_label = Label(text="Password:", font=("Helvetica", 20))
Password_label.grid(column=0, row=3)

# Entries
Website_input = Entry(width=20)
Website_input.grid(column=1, row=1, columnspan=1)
Website_input.focus()

Email_input = Entry(width=38)
Email_input.grid(column=1, row=2, columnspan=2)
Email_input.insert(0, "mustafa.ali.khan0909@gmail.com")

Password_input = Entry(width=20)
Password_input.grid(column=1, row=3)

# Buttons
search_btn = Button(text="Search", width=14, command=find_password)
search_btn.grid(column=2, row=1, columnspan=1)

Generate_pwd_btn = Button(text="Generate Password", command=generate_password)
Generate_pwd_btn.grid(column=2, row=3)

Add_btn = Button(text="Add", width=36, command=save)
Add_btn.grid(column=1, row=4, columnspan=2)









window.mainloop()
