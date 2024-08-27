import random
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,_-"

    all = ""
    if lowercase_var.get():
        all += lower
    if uppercase_var.get():
        all += upper
    if numbers_var.get():
        all += numbers
    if symbols_var.get():
        all += symbols

    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive number.")

        if not all:
            messagebox.showwarning("Warning", "You must include at least one character type!")
            return

        password = "".join(random.sample(all, length))
        result_label.config(text=f"Generated Password: {password}")
        copy_button.config(state=tk.NORMAL)  # Enable the copy button
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = result_label.cget("text").replace("Generated Password: ", "")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main application window
root = tk.Tk()
root.title("Password Generator")

# User options for character types
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var).pack(anchor='w')
tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var).pack(anchor='w')
tk.Checkbutton(root, text="Include numbers", variable=numbers_var).pack(anchor='w')
tk.Checkbutton(root, text="Include symbols", variable=symbols_var).pack(anchor='w')

# Password length input
tk.Label(root, text="Choose Password Length:").pack(anchor='w')
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack()

# Button to copy the password to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", state=tk.DISABLED, command=copy_to_clipboard)
copy_button.pack()

# Start the application
root.mainloop()
