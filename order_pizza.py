# nested lists within a dictionary for a pizza ordering system
toppings = []
for order in range(5):
    remaining = 5 - order
    userRequest = input(f"{remaining} topping choices (enter 1 at a time): ")
    toppings.append(userRequest)
pizza = {'toppings': toppings, 'crust': 'thin', 'sauce': 'ranch'}
print(f"\nyou have ordered a {pizza['crust']} crust pizza with {pizza['sauce']} drizzle on top."
      f"\nIt includes the following toppings: ")
for item in pizza['toppings']:
    print(f"\t{item}")
