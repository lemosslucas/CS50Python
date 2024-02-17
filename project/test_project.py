import project

def main():
    test_register()
    test_search()
    test_delete()


def test_register():
    assert project.register("rice", ["rice", "garlic"]) == "\nThe recipe Rice was register with sucessfull\n"
    assert project.register("cake", ["sugar", "milk", "eggs"]) == "\nThe recipe Cake was register with sucessfull\n"
    assert project.register("whey", ["whey", "water"]) == "\nThe recipe Whey was register with sucessfull\n"

def test_search():
    assert project.search("milk") == "\nThe recipe Milk was not found in our database system\n"
    assert project.search("cake") == "\nThe recipe Cake was found!\n"


def test_delete():
    assert project.delete("rice") == "\nThe recipe Rice was deleted with sucessful\n"
    assert project.delete("milk") == "\nThe recipe Milk was not found in our database system\n"

main()