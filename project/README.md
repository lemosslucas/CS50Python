# Recipe Organizer
    #### Video Demo:  https://youtu.be/Y4p9H6PbC3A
    #### Description: With the recipe organizer, you can easily register, search, and delete recipes.
# Descriptions
## The reason of the choise
### My grandmother constantly makes various recipes, so she handed me a notebook with all her recipes to make at home. However, the recipes are not very well organized, so I spend a lot of time looking for them. Therefore, I decided to create a system where I can register the recipes, delete recipes that I didn't like, and also easily search for recipes.
## Ease of use
### The user only needs to choose one of the options "[1,4]" and provide the recipe. Much simpler than searching manually.
# Files
## project.py
### Functions: The file is divided into three functions, and "main()" is responsible for grouping all these functions.
- Main
#### The main file is the most important one; it is responsible for calling all the program's functionalities. To enhance user-friendliness with the interface, I used a menu system. The system prints a table with values from 1 to 4, and the user decides which function (1 = register, 2 = search, 3 = delete) to use at the moment. To exit the program, the user should type 4, thus ending the program.
- Register
#### Responsible for writing the recipe (name, ingredients) to the recipes.csv file in CSV file format.
- Search
#### Uses the "recipe" received as a substring to search for the first occurrence in the file's line. Upon finding the substring in the line, it returns the recipe in tabular form.
- Delete
#### Uses the "recipe" received as a substring to search for the first occurrence in the file's line. The lines that are not the recipe are stored in a list, "new", temporarily. Therefore, with the use of file opening in "w" mode, we use a temporary file to store the "rows" stored in the "new" list. After that, we use os.replace, which modifies the file names by swapping the data from the temporary (temp.csv) to the definitive (recipes.csv).
#### Libraries
#### Three libraries are imported: sys (used for program termination), os (for file swapping), and the csv library (responsible for using CSV file functions for the Python language). None of these need to be installed separately.
## test_project.py
### This file is responsible for executing tests on the program to check its efficiency and find possible flaws.
#### São tres funções que importam as funções do "project.py" e a envia parametros setados para utilizar como teste
## recipes.csv
### This file stores all the recipes that users register in the system. It is in CSV format, which is easier for data manipulation.
# Execution of Files
## To use the project.py file, execute the following command:
> python project.py
### This will successfully run the Recipe Organizer.
## To use the test_project.py file, execute the following command:
> pytest test_project.py
#
>[!IMPORTANT]
> The project.py and test_project.py files must be in the same folder for pytest to work.
# Contact
## If you have any further questions or suggestions for improvement, please contact me via email at lucaslemoricaldoni@gmail.com
> [!NOTE]
> This project was developed by @lemoss_lucas.