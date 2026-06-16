x = int(input("Enter the value for x"))
# x is the variable to match
match x:
# if x is 0
    case 0:
        print("x is zero")
# case with if-condition
    case 4:
        print("case is 4")

# so it is basically just an else: I
    case _:
        print(x)