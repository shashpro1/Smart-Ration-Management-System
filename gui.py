import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("ration.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cardholders(
    card_no TEXT PRIMARY KEY,
    name TEXT,
    members INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_name TEXT,
    quantity INTEGER,
    price REAL
)
""")

conn.commit()

def add_cardholder():
    card = card_entry.get()
    name = name_entry.get()
    members = members_entry.get()

    if card == "" or name == "" or members == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        cursor.execute(
            "INSERT INTO cardholders VALUES(?,?,?)",
            (card, name, members)
        )
        conn.commit()

        messagebox.showinfo(
            "Success",
            "Card Holder Added Successfully"
        )

        card_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        members_entry.delete(0, tk.END)

    except:
        messagebox.showerror(
            "Error",
            "Card Number Already Exists"
        )



def add_product():
    pname = product_entry.get()
    qty = quantity_entry.get()
    price = price_entry.get()

    if pname == "" or qty == "" or price == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    cursor.execute(
        "INSERT INTO products VALUES(?,?,?)",
        (pname, qty, price)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Product Added Successfully"
    )

    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def view_products():
    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    result = ""

    for p in products:
        result += (
            f"Product: {p[0]}\n"
            f"Quantity: {p[1]}\n"
            f"Price: ₹{p[2]}\n\n"
        )

    if result == "":
        result = "No Products Found"

    messagebox.showinfo(
        "Product List",
        result
    )


def generate_bill():

    product = bill_product_entry.get()
    qty = bill_qty_entry.get()

    if product == "" or qty == "":
        messagebox.showerror(
            "Error",
            "Fill all fields"
        )
        return

    cursor.execute(
        "SELECT price FROM products WHERE product_name=?",
        (product,)
    )

    result = cursor.fetchone()

    if result:

        price = float(result[0])

        total = price * int(qty)

        bill = (
            f"SMART RATION MANAGEMENT SYSTEM\n\n"
            f"Product : {product}\n"
            f"Quantity : {qty}\n"
            f"Price : ₹{price}\n\n"
            f"Total Amount : ₹{total}"
        )

        messagebox.showinfo(
            "Bill Generated",
            bill
        )

    else:
        messagebox.showerror(
            "Error",
            "Product Not Found"
        )



root = tk.Tk()

root.title("Smart Ration Management System")
root.geometry("750x700")

title = tk.Label(
    root,
    text="SMART RATION MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

subtitle = tk.Label(
    root,
    text="Government Public Distribution System",
    font=("Arial", 10)
)

subtitle.pack()


tk.Label(
    root,
    text="----- CARD HOLDER MANAGEMENT -----",
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Label(root, text="Card Number").pack()
card_entry = tk.Entry(root, width=40)
card_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Family Members").pack()
members_entry = tk.Entry(root, width=40)
members_entry.pack()

tk.Button(
    root,
    text="Add Card Holder",
    command=add_cardholder
).pack(pady=10)



tk.Label(
    root,
    text="----- PRODUCT MANAGEMENT -----",
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Label(root, text="Product Name").pack()
product_entry = tk.Entry(root, width=40)
product_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root, width=40)
quantity_entry.pack()

tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root, width=40)
price_entry.pack()

tk.Button(
    root,
    text="Add Product",
    command=add_product
).pack(pady=5)

tk.Button(
    root,
    text="View Products",
    command=view_products
).pack(pady=5)



tk.Label(
    root,
    text="----- BILL GENERATION -----",
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Label(root, text="Product Name").pack()
bill_product_entry = tk.Entry(root, width=40)
bill_product_entry.pack()

tk.Label(root, text="Quantity").pack()
bill_qty_entry = tk.Entry(root, width=40)
bill_qty_entry.pack()

tk.Button(
    root,
    text="Generate Bill",
    command=generate_bill
).pack(pady=10)

root.mainloop()

conn.close()
