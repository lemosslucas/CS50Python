def main():
    # Storage the expression
    expression = input("Expression: ")
    # Split the expression in 3 variabels
    x, y, z = expression.split(" ")
    # Convert the x and y for float
    x = float(x)
    z = float(z)
    # Call the fuction and storage the output
    result = interprete_math(x, y, z)
    # print the output of fuction
    print(f"{result:.1f}")

def interprete_math(x, y, z):
    # Conditions of who is the operation and does the expression
    if y == "+" :
        result = x + z
    elif y == "/" :
        result = x / z
    elif y == "-" :
        result = x - z
    elif y == "*" :
        result = x * z
    # return the result
    return result

main()