import tkinter as tk
from tkinter import messagebox
import random

generated_otp = ""

def generate_otp():
    global generated_otp

    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":
        generated_otp = str(random.randint(1000, 9999))

        messagebox.showinfo(
            "OTP Generated",
            f"Your OTP is: {generated_otp}"
        )
    else:
        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )

def verify_otp():
    entered_otp = otp_entry.get()

    if entered_otp == generated_otp:
        messagebox.showinfo(
            "Success",
            "Login Successful"
        )

        root.destroy()


    else:
        messagebox.showerror(
            "Error",
            "Invalid OTP"
        )

root = tk.Tk()
root.title("Smart Ration Login")
root.geometry("400x300")

tk.Label(root,
         text="Smart Ration Login",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root,
          text="Generate OTP",
          command=generate_otp).pack(pady=10)

tk.Label(root, text="Enter OTP").pack()
otp_entry = tk.Entry(root)
otp_entry.pack()

tk.Button(root,
          text="Verify OTP",
          command=verify_otp).pack(pady=10)

root.mainloop()
