import string
import random
import tkinter as tk
from tkinter import ttk
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry('400x400')

        self.title=ttk.Label(root,text='Random Password Generator',font='CAlibri 14 bold')
        self.title.pack()

        self.label = ttk.Label(root, text="Select Password Options:")
        self.label.pack(pady=10)

        predefined_options = ["Letters",
                              "Digits",
                              "Special Characters",
                              "All of the Above",
                              "Letters and Digits",
                              "Digits and Special Characters",
                              "Special Characters and Letters"]

        self.options = ttk.Combobox(root, values=predefined_options, state="readonly")
        self.options.pack()

        self.length_label = ttk.Label(root, text="Enter Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = ttk.Entry(root)
        self.length_entry.pack(pady=5)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_and_display_password)
        self.generate_button.pack(pady=10)

        self.password_label = ttk.Label(root, text="")
        self.password_label.pack(pady=10)

        self.copy_button = ttk.Button(root, text="Copy Password", command=self.copy_password)
        self.copy_button.pack(pady=5)


        
        self.generated_password = ""

    def generate_and_display_password(self):
        option = self.options.get()
        length = int(self.length_entry.get())
        self.generated_password = self.generate_password_by_option(option, length)
        self.password_label.config(text=f"Generated Password: {self.generated_password}")

    def copy_password(self):
        if self.generated_password:
            pyperclip.copy(self.generated_password)
            self.password_label.config(text=f"Generated Password: {self.generated_password} (Copied to Clipboard)")

    def generate_password_by_option(self, option, length):
        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation
        s = []

        if "Letters" in option:
            s.extend(letters)
        if "Digits" in option:
            s.extend(digits)
        if "Special Characters" in option:
            s.extend(special)
        if "All of the Above" in option:
            s.extend(letters)
            s.extend(digits)
            s.extend(special)

        if not s:
            return "No valid option selected."

        random.shuffle(s)
        return "".join(s[:length])

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
