import csv
import sys
import os

def main():
    while True:
        print("Welcome to Recipe Organizer!")
        option = input("[1] = Register a Recipe\n[2] = Search a Recipe\n[3] = Delete a Recipe\n[4] = Close\n")
        if option == "1":
            recipe = input("What is the name of the recipe? ")
            try:
                size = int(input("How many ingredients are? "))
            except ValueError:
                print("The answer need be a integer!")
                main()
            ingredients = []
            for x in range(size):
                ingredient = input("Ingredient: ")
                ingredients.append(ingredient)
            output = register(recipe, ingredients)
            print(output)

        elif option == "2" :
            recipe = input("What recipe do you want? ")
            output = search(recipe)
            print(output)

        elif option == "3" :
            recipe = input("What recipe do you want deleted? ")
            output = delete(recipe)
            print(output)

        elif option == "4" :
            sys.exit("Thank for the use of Recipe Organizer, devolamenpt for Lucas Lemos")
        else:
            print("Invalid option, need to be in [1,4]")

def register(recipe, ingredients):
    # create a empty array for storage the ingredients
    with open("recipes.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([recipe.lower()] + ingredients)
    return (f"\nThe recipe {recipe.capitalize()} was register with sucessfull\n")

def search(recipe):
    string = "Recipe"
    with open("recipes.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            # name of recipe is equal the name of recipe in file
            if recipe.lower() == row[0] :
                print(f"\n{string.ljust(20)}|Ingredients")
                # print the name of recipe
                print(f"{row[0].ljust(20)}|", end="")
                # print the ingredients
                for ingredient in row[1:]:
                    print(f"{ingredient}|" , end="")
                print("")
                return (f"\nThe recipe {recipe.capitalize()} was found!\n")
    # Clean the terminal outuput
    return (f"\nThe recipe {recipe.capitalize()} was not found in our database system\n")


def delete(recipe):
    # Create a empty array for storage the new file
    new = []
    deleted = False
    # open a file in reader mode
    with open("recipes.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if recipe.lower() == row[0].lower():
                deleted = True
            else :
                new.append(row)
    # open a file in write mode
    with open("recipes_temp.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(new)
    os.replace("recipes_temp.csv", "recipes.csv")
    # Do a feedback if the recipe was deleted
    if deleted == True:
        return(f"\nThe recipe {recipe.capitalize()} was deleted with sucessful\n")
    else:
        return(f"\nThe recipe {recipe.capitalize()} was not found in our database system\n")


if __name__ == "__main__" :
    main()
