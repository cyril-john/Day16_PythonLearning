from data import available_quantity


def make_order(entered_choice, entered_price):
    payment = int(input(f"pay the price of {entered_choice}"))
    if entered_price <= payment:
        change = payment - entered_price
        print(f"payment is successful , here is your change {change}")
        return True
    else:
        return False


def is_transaction_success(entered_quantity, entered_choice):
    choice_available_quantity = available_quantity[entered_choice]['quantity']
    if entered_quantity <= choice_available_quantity:
        print("transaction success")
        return True
    else:
        print(f"available quantity is : {choice_available_quantity}, you have entered : {entered_quantity}")
        print("No STOCK !")
        return False













