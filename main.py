import sqlite3

conn = sqlite3.connect("ration.db")
cursor = conn.cursor()

while True:
    print("\nSMART RATION MANAGEMENT SYSTEM")
    print("1. Add Card Holder")
    print("2. View Card Holders")
    print("3. Add Product")
    print("4. View Products")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        card = input("Card Number: ")
        name = input("Name: ")
        members = int(input("Family Members: "))

        cursor.execute(
            "INSERT INTO cardholders VALUES(?,?,?)",
            (card, name, members)
        )

        conn.commit()
        print("Card Holder Added Successfully")

    elif choice == "2":
        cursor.execute("SELECT * FROM cardholders")
        records = cursor.fetchall()

        if records:
            for row in records:
                print(row)
        else:
            print("No Card Holders Found")

    elif choice == "3":
        pname = input("Product Name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))

        cursor.execute(
            "INSERT INTO products VALUES(?,?,?)",
            (pname, qty, price)
        )

        conn.commit()
        print("Product Added Successfully")

    elif choice == "4":
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        if products:
            for p in products:
                print(p)
        else:
            print("No Products Found")

   elif choice == "5":
    print("\n----- RATION BILL -----")

    card_no = input("Enter Card Number: ")
    product = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))

    cursor.execute(
        "SELECT price FROM products WHERE product_name=?",
        (product,)
    )

    result = cursor.fetchone()

    if result:
        price = result[0]
        total = qty * price

        print("\n----- BILL -----")
        print("Card Number :", card_no)
        print("Product :", product)
        print("Quantity :", qty)
        print("Price :", price)
        print("Total Amount : ₹", total)

    else:
        print("Product Not Found")
        elif choice == "6":
            print("Thank You")
    break
else:
    print("Invalid Choice!")


conn.close()