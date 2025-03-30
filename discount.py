def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it is applied; otherwise, the original price is returned.
    
    :param price: float - The original price of the item.
    :param discount_percent: float - The discount percentage to be applied.
    :return: float - The final price after applying the discount (if applicable).
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Prompting the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percentage)
    print(f"Final price after discount: {final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")
