from data import GROCERY_PRICE_LIST, available_quantity
from orders import make_order, is_transaction_success


def grocery_store():
    while True:
        choice = input("what do you want to purchase sugar or salt :")

        if choice == "off":
            False
        else:
            commodity_price = GROCERY_PRICE_LIST[choice]['price']
            print(commodity_price)
            quantity = int(input("enter quantity : "))
            if is_transaction_success(quantity, choice):
                if make_order(choice, commodity_price):
                    print("thank you for shopping with us")


grocery_store()
