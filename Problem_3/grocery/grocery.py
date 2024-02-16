# define a empty dict
d = dict()
new_value = 1

while(True):
    try:
        # Storage the item
        item = input()
        new_item = item.upper()
        # calculate the quant of itens in the dict
        if new_item in d:
            d[new_item] += 1
        else:
            d[new_item] = new_value
    # When the user digit control + d
    except EOFError:
        #print the quant of itens in a sorted ordem
        for key, value in sorted(d.items(), key = lambda x: x[0]):
            print(f"{value} {key}")
        # Close the loop
        break
