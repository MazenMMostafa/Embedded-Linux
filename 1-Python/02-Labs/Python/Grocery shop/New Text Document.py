# Order Tuple
inventory = (
    ('apple', 2, 1.0),
    ('banana', 3, 2.0),
    ('bread', 4, 2.5),
    ('milk', 5, 1.5),
    ('eggs', 6, 2.0)
)

# Total Cost Function
def calculate_cost(items):
    total_cost = 0
    for item in items:
        for product in inventory:
            if item == product[0]:
                total_cost += product[1]
    return total_cost;

# Printing Function
def print_inventory():
    print("Inventory:");
    for product in inventory:
        print(f"{product[0]} -> ${product[1]} per unit, {product[2]} units available")

print_inventory()
shopping_list = ['apple', 'banana', 'bread']
total_cost = calculate_cost(shopping_list)
print(f"Total cost of shopping list: ${total_cost}")
