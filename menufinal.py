class FoodItem:
    def __init__(self, name, price, extras, extra_price):
        self.name = name
        self.price = price
        self.extras = extras
        self.extra_price = extra_price

    def calculate_total(self, chosen_extras):
        total = self.price + (self.extra_price * len(chosen_extras))
        return total


class MenuItem(FoodItem):
    def __init__(self, name, price, extras, extra_price):
        super().__init__(name, price, extras, extra_price)


def create_menu():
    # Create food menu dictionary
    return {
        "Tacos": MenuItem("Tacos", 4.99, ["Guacamole", "Sour Cream", "Jalapeños"], 1.50),
        "Burrito": MenuItem("Burrito", 6.99, ["Cheese", "Rice", "Beans", "Salsa"], 1.50),
        "Enchiladas": MenuItem("Enchiladas", 7.99, ["Extra Cheese", "Avocado", "Sour Cream"], 1.50),
        "Burger": MenuItem("Burger", 6.99, ["Fries", "Mushrooms", "Lettuce", "Tomatoes"], 1.99),
        "Pizza": MenuItem("Pizza", 8.99, ["Pepperoni", "Extra Cheese", "Mushrooms"], 1.99),
        "Ice Cream": MenuItem("Ice Cream", 3.99, ["Sprinkles", "Whipped Cream", "Chocolate Syrup"], 1.50)
    }
