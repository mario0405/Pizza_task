from database import list_all_pizzas, find_pizzas_with_topping, find_pizza_by_name

def main():
    while True:
        print("\nPizza Menu:")
        print("1. List all pizzas")
        print("2. Find pizzas with a specific topping")
        print("3. Select a pizza by name")
        print("4. Calculate pizza price with discount code")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # List all pizzas
            pizzas = list_all_pizzas()
            print("\nAvailable Pizzas:")
            for pizza in pizzas:
                print(pizza)

        elif choice == '2':
            # Find pizzas with a specific topping
            topping = input("Enter the topping to search for: ")
            pizzas = find_pizzas_with_topping(topping)
            if pizzas:
                print("\nPizzas with", topping, ":")
                for pizza in pizzas:
                    print(pizza)
            else:
                print("No pizzas found with that topping.")

        elif choice == '3':
            # Select a pizza by name
            name = input("Enter the name of the pizza: ")
            pizza = find_pizza_by_name(name)
            if pizza:
                print("\nSelected Pizza Details:")
                print(pizza.get_details())
            else:
                print("Pizza not found.")

        elif choice == '4':
            # Calculate price with discount code
            name = input("Enter the name of the pizza: ")
            pizza = find_pizza_by_name(name)
            if pizza:
                discount_code = input("Enter discount code (or press Enter to skip): ")
                if discount_code == "PIZZA10":
                    discounted_price = pizza.price * 0.9  # 10% discount
                    print(f"Discounted price: ${discounted_price:.2f}")
                else:
                    print(f"Price: ${pizza.price:.2f}")
            else:
                print("Pizza not found.")

        elif choice == '5':
            # Exit the program
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
