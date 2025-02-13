# Name: Shahzeb Ahmad
# Date: 2/13/2025
# Class: CIS-30A

import tkinter as tk
from tkinter import messagebox
import menufinal  # Importing the custom menu module

# Function to create the menu
def create_menu():
    return {
        "Tacos": {"price": 5.99, "extras": ["Guacamole", "Sour Cream", "Jalapeños"], "extra_price": 1.50},
        "Burrito": {"price": 7.99, "extras": ["Cheese", "Rice", "Beans", "Salsa"], "extra_price": 1.50},
        "Enchiladas": {"price": 8.99, "extras": ["Extra Cheese", "Avocado", "Sour Cream"], "extra_price": 1.50},
        "Burger": {"price": 6.99, "extras": ["Fries", "Mushrooms", "Lettuce", "Tomatoes"], "extra_price": 1.99},
        "Pizza": {"price": 8.99, "extras": ["Pepperoni", "Extra Cheese", "Mushrooms"], "extra_price": 1.99},
        "Ice Cream": {"price": 3.99, "extras": ["Sprinkles", "Whipped Cream", "Chocolate Syrup"], "extra_price": 1.50}
    }

class RestaurantOrderSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order System")
        self.total_price = 0
        self.selected_orders = []

        # Use the create_menu function from the menu module
        self.food_menu = create_menu()

        # Create the user interface (UI)
        self.create_widgets()

    def create_widgets(self):
        """Creates and displays the UI elements."""
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

        self.display_extras("Tacos")  # Show default extras for "Tacos"

        tk.Button(self.root, text="Add to Order", command=self.add_to_order).pack()
        tk.Button(self.root, text="Complete Order", command=self.finalize_order).pack()

    def display_extras(self, selected_food):
        """Show available extras based on the selected food item."""
        # Clear previously displayed extras
        for widget in self.extras_frame.winfo_children():
            widget.destroy()

        self.selected_extras = []
        item = self.food_menu[selected_food]

        tk.Label(self.extras_frame, text="Select Extras:").pack()
        for extra in item["extras"]:
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
        item_total = item["price"] + (item["extra_price"] * len(chosen_extras))

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

# Running the program
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderSystem(root)
    root.mainloop()
