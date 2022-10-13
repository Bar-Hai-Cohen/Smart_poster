import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x150")
root.title('Sign In Form')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()
dict_password = {
  "email": "barcohen687@gmail.com",
  "password": "209499284"
}

def new_window():
    root_post=tk.Tk()
    root_post.geometry("300x150")
    root_post.title('Smart_Post')

def login_clicked():
    email=email_entry.get()
    password=password_entry.get()
    if email == dict_password.get("email") and password == dict_password.get("password"):
        root.destroy()
        new_window()


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)


root.mainloop()