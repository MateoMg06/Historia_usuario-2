
# Ask the user for sale data

def register_sale():
    name_ok = False
    while name_ok == False:
        name = input("Product name: ").strip().lower()
        try:
            float(name)
            print("Write only letters")
            name_ok = False
        except:
            if name == "":
                print("Write only letters")
                name_ok = False
            else:
                name_ok = True

    price_ok = False
    while price_ok == False:
        try:
            price = float(input("Product price: "))
            if price < 0:
                print("Price cannot be negative")
                price_ok = False
            else:
                price_ok = True
        except:
            print("Write a number")

    quantity_ok = False
    while quantity_ok == False:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative")
                quantity_ok = False
            else:
                quantity_ok = True
        except:
            print("Write a whole number")

    total_cost = price * quantity

    sale = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "subtotal": total_cost,     
    }

    return sale