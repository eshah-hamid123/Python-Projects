from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_numbers + password_symbol

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_name = website_entry.get()
    email_acc = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": email_acc,
            "password": password,
        }}

    if len(website_name) == 0 or len(password) == 0 or len(email_acc) == 0:
        messagebox.showinfo(title="Oops!", message="You left some fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered:\n Email: {email_acc} \n Password: {password} \n Is it okay?")

        if is_ok:
            try:
                with open ("data.json", mode='r') as text_file:
                    data = json.load(text_file)

            except FileNotFoundError:
                with open("data.json", mode='w') as text_file:
                    json.dump(new_data, text_file, indent=4)

            else:
                data.update(new_data)
                with open("data.json", mode='w') as text_file:
                    json.dump(data, text_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode='r') as text_file:
            data = json.load(text_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title="Details", message=f'Email is: {email}\n Password is: {password}')
        else:
            messagebox.showerror(message="No data found")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", font=("Calibri", 12, "normal"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username", font=("Calibri", 12, "normal"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password", font=("Calibri", 12, "normal"))
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=41)
email_entry.insert(0, "eshahhamid02@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

search = Button(text='Search', highlightthickness=0, width=15, command=find_password)
search.grid(column=2, row=1)

password_button = Button(text="Password Generator", highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()