Order_amount=float(input('What is the order amount?  '))
Name_of_state=str.upper(input('what is the state? '))

if Name_of_state == "WI" :
    tax = Order_amount * 5.5 / 100
    total = Order_amount + tax
    print(f"The subtotal is ${Order_amount} ")
    print(f"The tax is ${tax} ")
    print(f"The total is ${total} ")
else:
    print(f"The total is ${Order_amount} ")


