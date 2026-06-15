

x = int(input("Enter the value of x: "))

# x is a variable to match

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is a 4")
    case 7:
        print("x is a 7")
    case _:
        print("x is neither 0, 4, nor 7")