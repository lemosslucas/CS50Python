# Storage the fruit
fruit = input("Item: ")
# Does this to doenst make any error of write
fruit = fruit.lower()
# Declaration the fruit calories
fruit_dict = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80
}
# If fruit has in the dict
if fruit in fruit_dict :
    # print the calories of the fruit
    print(f"Calories: {fruit_dict[fruit]}")
