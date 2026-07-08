Great choice. Random Password Generator (Task 3) is one of the easiest projects and fully satisfies the internship requirements if implemented properly. �
OASIS INFOBYTE — SIP Task List.pdf
I recommend building the Advanced (GUI) version because it looks much more impressive on GitHub while still being manageable.
Project Structure
Random-Password-Generator/
│── password_generator.py
│── requirements.txt
│── README.md
Step 1: Install Dependencies
pip install pyperclip
Step 2: password_generator.py
import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip

# Generate Password
def generate_password():
    length = length_var.get()

    upper = uppercase_var.get()
    lower = lowercase_var.get()
    digits = numbers_var.get()
    symbols = symbols_var.get()

    if length < 8:
        messagebox.showerror("Error", "Password length must be at least 8.")
        return

    selected = ""

    if upper:
        selected += string.ascii_uppercase
    if lower:
        selected += string.ascii_lowercase
    if digits:
        selected += string.digits
    if symbols:
        selected += string.punctuation

    if len(selected) == 0:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = ''.join(secrets.choice(selected) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Weak")
    elif score <= 4:
        strength_label.config(text="Medium")
    else:
        strength_label.config(text="Strong")

def copy_password():
    password = password_entry.get()

    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("450x450")
root.resizable(False, False)

tk.Label(root, text="Password Length", font=("Arial",12)).pack()

length_var = tk.IntVar(value=12)

tk.Spinbox(root, from_=8, to=50, textvariable=length_var).pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root,text="Uppercase",variable=uppercase_var).pack(anchor="w", padx=80)
tk.Checkbutton(root,text="Lowercase",variable=lowercase_var).pack(anchor="w", padx=80)
tk.Checkbutton(root,text="Numbers",variable=numbers_var).pack(anchor="w", padx=80)
tk.Checkbutton(root,text="Symbols",variable=symbols_var).pack(anchor="w", padx=80)

tk.Button(root,text="Generate Password",command=generate_password,font=("Arial",12)).pack(pady=10)

password_entry = tk.Entry(root,font=("Arial",14),justify="center",width=30)
password_entry.pack()

tk.Button(root,text="Copy Password",command=copy_password).pack(pady=10)

strength_label = tk.Label(root,text="Strength",font=("Arial",12))
strength_label.pack()

root.mainloop()
requirements.txt
pyperclip
README.md
# Random Password Generator

A Python GUI application that generates secure random passwords.

## Features

- Password length selection
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols
- Password strength indicator
- Copy password to clipboard

## Technologies

- Python
- Tkinter
- Secrets
- Pyperclip

## Run

pip install -r requirements.txt

python password_generator.py
Internship Feature Checklist
This project includes:
✔ GUI using Tkinter
✔ Adjustable password length
✔ Uppercase, lowercase, numbers, symbols selection
✔ Uses secrets module for secure password generation
✔ Password strength indicator
✔ Copy to Clipboard
Optional enhancements (to score even better)
You can add:
Exclude ambiguous characters (0, O, l, 1)
Password history (last 5 generated passwords)
Ensure at least one character from each selected category is always included
These align with the advanced task checklist and make your submission even stronger. �
OASIS INFOBYTE — SIP Task List.pdf
Once you've completed this project, I'll help you build the Basic Weather App with a modern GUI so you'll have all three required Python projects ready for submission.