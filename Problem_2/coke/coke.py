machine_value = 50
money_spent = 0

while money_spent < machine_value :
    money_place = int(input("Insert a coin: "))
    if money_place in [5, 10, 25]:
        money_spent += money_place
        remained_money = machine_value - money_spent
        if remained_money > 0 :
            #print the Amount Due
            print(f"Amount Due: {remained_money}")
        elif remained_money <= 0:
            # Convert the negative value for positive value
            remained_money = abs(remained_money)
            print(f"Change Owed: {remained_money}")
    else:
        print(f"Amount Due: {machine_value}")
