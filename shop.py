class Coffee_shop:
    items_prices = {
        "iced spanish latte": 100,
        "mocha": 120,
        "matcha": 110,
        "cakes": 80,
        "cheese cakes": 90,
        "salted caramel": 130,
        "fresh juices": 70
    }

    def __init__(self, menu, minimum_charge, rating):
        self.menu = menu
        self.minimum_charge = minimum_charge
        self.rating = rating

    def show_menu(self):
        return self.menu

    def __str__(self):
        return f"{self.menu},{self.minimum_charge},{self.rating}"

    def __eq__(self, value):
        return (
            self.minimum_charge == value.minimum_charge
            and self.rating == value.rating
        )

    def __lt__(self, other):
        return self.rating < other.rating

    @staticmethod
    def is_good_place(rating):
        return rating >= 9.5

    @classmethod
    def special_offers(cls):
        return cls(
            ['two iced spanish latte', 'two cheese cakes'],
            400,
            9.8
        )


# Branches

Branch1 = Coffee_shop(
    ['iced spanish latte', 'matcha', 'mocha', 'cakes', 'cheese cakes'],
    500,
    10
)

Branch2 = Coffee_shop(
    ['iced spanish latte', 'matcha', 'salted caramel', 'cakes', 'fresh juices'],
    700,
    8.6
)


# Payment function

def is_payment_sufficient(payment, price):
    return payment >= price


# Main function

def main():

    Branch = input('Choose the branch: ')

    while Branch not in ['1', '2']:
        print("Invalid choice. Please choose 1 or 2")
        Branch = input('Choose the branch: ')

    if Branch == '1':
        selected_branch = Branch1

    else:
        selected_branch = Branch2

    menu = selected_branch.show_menu()

    for item in menu:
        print(item)

    # Order selection

    while True:
        order = input('Enter your choice: ').strip().lower()

        if order in menu:
            print(order)
            price = Coffee_shop.items_prices[order]
            print(price)
            break

        else:
            print('Order is not found')

    # Payment

    while True:
        try:
            payment = float(input('Please enter payment: '))

            if is_payment_sufficient(payment, price):
                print('Payment successful, your order has been confirmed')
                print('Your order is now being prepared')
                break

            else:
                print(
                    f"Sorry, the amount entered is not enough. "
                    f"Please enter at least {price} EGP."
                )

        except ValueError:
            print('Please enter a valid number')


if __name__ == "__main__":
    main()
