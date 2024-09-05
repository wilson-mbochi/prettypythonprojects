# nested lists within a dictionary for a pizza ordering system
print("we have a sale on thin crust pizzas! Choose your toppings!")
toppings = []
for order in range(5):
    remaining = 5 - order
    userRequest = input(f"{remaining} more topping choices (enter 1 at a time): ")
    toppings.append(userRequest)
sauce = input(f"Enter your favorite sauce: ")
pizza = {'toppings': toppings, 'crust': 'thin'}
print(f"\nyou have ordered a promotional {pizza['crust']} crust pizza with {sauce} drizzle on top."
      f"\nIt includes the following toppings: ")
for item in pizza['toppings']:
    print(f"\t{item}")

print("sending order off to Papa RAM's store...")
