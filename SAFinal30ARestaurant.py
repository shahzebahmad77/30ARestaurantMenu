import tkinter as tk
from tkinter import messagebox

# Base class for food items
class FoodItem:
    def __init__(self, name, price, extras, extra_price):
        self.name = name  # Name of the food item
        self.price = price  # Base price
        self.extras = extras  # List of extra options
        self.extra_price = extra_price  # Price per extra

    def calculate_total(self, chosen_extras):
        """Calculate total cost based on selected extras."""
        total = self.price + (self.extra_price * len(chosen_extras))
        return total

# Subclass for restaurant menu items
class MenuItem(FoodItem):
    def __init__(self, name, price, extras, extra_price):
        super().__init__(name, price, extras, extra_price)

# Main Restaurant Order System
class RestaurantOrderSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Mexican-American Restaurant Order System")
        self.total_price = 0
        self.selected_orders = []

        # Food menu dictionary
        self.food_menu = {
            "Tacos": MenuItem("Tacos", 4.99, ["Guacamole", "Sour Cream", "Jalapeños"], 1.50),
            "Burrito": MenuItem("Burrito", 6.99, ["Cheese", "Rice", "Beans", "Salsa"], 1.50),
            "Enchiladas": MenuItem("Enchiladas", 7.99, ["Extra Cheese", "Avocado", "Sour Cream"], 1.50),
            "Burger": MenuItem("Burger", 6.99, ["Fries", "Mushrooms", "Lettuce", "Tomatoes"], 1.99),
            "Pizza": MenuItem("Pizza", 8.99, ["Pepperoni", "Extra Cheese", "Mushrooms"], 1.99),
            "Ice Cream": MenuItem("Ice Cream", 3.99, ["Sprinkles", "Whipped Cream", "Chocolate Syrup"], 1.50)
        }

        # Build the GUI
        self.create_widgets()

    def create_widgets(self):
        """Creates and displays the GUI elements."""
        tk.Label(self.root, text="Enter Your Name:").pack()
        self.name_input = tk.Entry(self.root)
        self.name_input.pack()

        tk.Label(self.root, text="Choose a food item:").pack()
        self.food_choice = tk.StringVar(self.root)
        self.food_choice.set("Tacos")  # Default option
        self.food_menu_dropdown = tk.OptionMenu(self.root, self.food_choice, *self.food_menu.keys(), command=self.display_extras)
        self.food_menu_dropdown.pack()

        self.extras_frame = tk.Frame(self.root)
        self.extras_frame.pack()

        self.display_extras("Tacos")  # Display default extras

        tk.Button(self.root, text="Add to Order", command=self.add_to_order).pack()
        tk.Button(self.root, text="Complete Order", command=self.finalize_order).pack()

    def display_extras(self, selected_food):
        """Show available extras based on the selected food item."""
        for widget in self.extras_frame.winfo_children():
            widget.destroy()

        self.selected_extras = []
        item = self.food_menu[selected_food]

        tk.Label(self.extras_frame, text="Select Extras:").pack()
        for extra in item.extras:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.extras_frame, text=extra, variable=var)
            checkbox.pack(anchor="w")
            self.selected_extras.append((var, extra))

    def add_to_order(self):
        """Adds selected food and extras to the order."""
        customer_name = self.name_input.get().strip()
        if not customer_name:
            messagebox.showerror("Error", "Please enter your name!")
            return

        selected_food = self.food_choice.get()
        chosen_extras = [extra for var, extra in self.selected_extras if var.get()]
        item = self.food_menu[selected_food]
        item_total = item.calculate_total(chosen_extras)

        self.selected_orders.append((selected_food, chosen_extras, item_total))
        self.total_price += item_total

        messagebox.showinfo("Added", f"Added {selected_food} with {', '.join(chosen_extras) or 'no extras'}.\nTotal: ${item_total:.2f}")

    def finalize_order(self):
        """Finalizes the order and writes the summary to a file."""
        customer_name = self.name_input.get().strip()
        if not customer_name:
            messagebox.showerror("Error", "Please enter your name!")
            return

        if not self.selected_orders:
            messagebox.showerror("Error", "You haven't added anything to the order!")
            return

        with open("restaurant_order.txt", "w") as file:
            file.write(f"Customer Name: {customer_name}\n\n")
            for food, extras, cost in self.selected_orders:
                file.write(f"Item: {food}\n")
                file.write(f"Extras: {', '.join(extras) or 'None'}\n")
                file.write(f"Cost: ${cost:.2f}\n\n")
            file.write(f"Total Price: ${self.total_price:.2f}\n")

        messagebox.showinfo("Order Complete", f"Thank you for your order, {customer_name}!\nTotal Price: ${self.total_price:.2f}")
        self.root.quit()

# Run the program
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderSystem(root)
    root.mainloop()
