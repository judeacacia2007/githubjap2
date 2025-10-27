class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def show_menu(self):
        if not self.menu:
            print("no items available!")
        else:
            for i, item in enumerate(self.menu, start=1):
                print(f"{i}. {item.name} - ${item.price}")

class Order:
    def __init__(self):
        self.items=[]

    def add_item(self, food):
        self.items.append(food)

    def bill(self):
        return sum(item.price for item in self.items)
    
    def show_order(self):
        print("\n order summary")
        for item in self.items:
            print(f" -{item.name}-${item.price}")
        print(f"total bill:${self.bill()}")

class FoodDeliveryApp:
    def __init__(self):
        self.restaurants = []
        self.Order = Order()
        self.load_sample_data()

    def load_sample_data(self):
        r1 = Restaurant("Pizza Palace")
        r1.add_food(FoodItem("Margherita Pizza", 200))
        r1.add_food(FoodItem("Farm House Pizza", 350))

        r2 = Restaurant("Burger Hub")
        r2.add_food(FoodItem("Veg Burger", 120))
        r2.add_food(FoodItem("Cheese Burger", 180))

        self.restaurants.extend([r1, r2])

    def show_restaurants(self):
        print("\navailable restaurants")
        for i, r in enumerate(self.restaurants, start=1):
            print(f"{i}.{r.name}")

    def select_restaurant(self):
        self.show_restaurants()
        choice = int(input("Choose a restaurant: "))
        if 1 <= choice <= len(self.restaurants):
            return self.restaurants[choice - 1]
        else:
            print("Invalid choice")
            return None

    def main_menu(self):
        while True:
            print("\n===== FOOD DELIVERY APP =====")
            print("1. View Restaurants")
            print("2. View Menu & Order")
            print("3. Show Bill")
            print("4. Exit")
            ch = input("Enter choice: ")

            if ch == "1":
                self.show_restaurants()

            elif ch == "2":
                restaurant = self.select_restaurant()
                if restaurant:
                    restaurant.show_menu()
                    item_choice = int(input("Select item: "))
                    if 1 <= item_choice <= len(restaurant.menu):
                        food = restaurant.menu[item_choice - 1]
                        self.Order.add_item(food)
                        print(f"{food.name} added to order ✅")
                    else:
                        print("Invalid food selection")

            elif ch == "3":
                self.Order.show_order()

            elif ch == "4":
                print("Thank you for ordering!")
                break

            else:
                print("Invalid option")


app = FoodDeliveryApp()
app.main_menu()

            
            









