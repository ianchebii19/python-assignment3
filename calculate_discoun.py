1001


def calculate_discount(price, discount_percent):
    discounted_price = price - (price * (discount_percent / 100))

    if discount_percent >= 20:
        print("Discounted Price:", discounted_price)
    else:
        print("Original Price:", price)

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

calculate_discount(price, discount_percent)