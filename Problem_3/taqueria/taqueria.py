# Define the dict
taqueria_dict = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
final_price = 0.0
while (True):
    try:
        # Storage the item input
        item = input("Item: ")
        # lower the item
        new_item = item.lower()
        if new_item in taqueria_dict:
            # sum the itens prices
            final_price += taqueria_dict[new_item]
            print(f"Total: ${final_price:.2f}")
        #Check the user digit the control d
    except EOFError:
        # to most clean output
        print()
        break