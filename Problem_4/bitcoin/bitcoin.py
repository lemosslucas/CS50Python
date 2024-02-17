import requests
import sys
# If the input user is before the file name
if len(sys.argv) == 2 :
    try:
        # Storage the number of bitcoins
        n_bitcoins = float(sys.argv[1])
    except :
        # return this msg if not float
        sys.exit("Comand-line argument is not a number")
else:
    #If the input user not is before the file name
    sys.exit("Missing comand-line argument")
try:
    # Storage the value in the site
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # Called a own fuction of the requests
    answer = request.json()
    # Separetes all information of the site in Dollar, bit and float value
    bitcoin = answer["bpi"]["USD"]["rate_float"]
    # Does how many dolars will be
    amount = bitcoin * n_bitcoins
    # Print the dollar
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit("Request Exception")
