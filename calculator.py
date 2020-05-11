def again():
    x = input('''To continue press Y/y, To exit press N/n 
    Choice :: ''')
    if x.lower() == 'y':
        calc()
    elif x.lower() == 'n':
        quit()
    else:
        print("Input error, Enter the  choice again ")
        again()
def calc():
    a = float(input("Enter first no. : "))
    b = float(input("Enter second no. : "))
    c = input("Enter operator : ")
    if c == "+":
        print("Addition is ",a+b)
    elif c == "-":
        print("Sub. is ",a-b)
    elif c == "*":
        print("Mul. is ",a*b)
    elif c == "/":
        print("Div. is ",a/b)
    elif c == "%":
        print("Rem. is ",a%b)
    else:
        print("Wrong operation")
    again()
calc()