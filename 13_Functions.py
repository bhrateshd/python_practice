def function_name(parameters):
    # Function body
    statement(s)
    return value


# Components
# def → Keyword used to define a function.
# function_name → Name of the function.
# parameters → Inputs to the function (optional).
# : → Marks the beginning of the function body.
# return → Sends a value back to the caller (optional).


def great(name):
    print("Hello my name is: ", name)
    
great("Bhratesh")

# name is a parameter 
# Bhratesh is a argument


a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))

def add(a, b):
    result = a + b 
    print(result)
add(a, b)



# Return statement sends a value back to the caller
a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))

def add(a, b):
    return a + b 
    
sum = add(a, b)

print(sum)

# Explanation
# add(5,10) executes.
# 5 + 10 = 15
# return 15
# Value stored in variable sum.
# =====================================================================

def calculateGmean(a, b):
    mean = (a*b)/(a+b)

    print(mean)

def isGreater(a, b):
    if(a>b):
        print("a is greater than b")
    else:    
        print("b is greater than a")
a = 9 
b = 8
isGreater(a, b)
calculateGmean(a, b)


# =====================================================================

def fib(n):  # write a fibo series less than n

    a, b = 0, 1
    while a < n:
        print(a, end='\n ')
        a, b = b, a + b
    print()
    
    
# Now we will call the function
fib(2000)




# Built in functions
print()
len()
type()
max()
min()
sum()

numbers = [10, 20, 30]

print(len(numbers))
print(max(numbers))


# Variable scope
# local variables accesible only within the function
def test():
    x = 100
    print(x)

test()

# Global variable accessible through the program
x = 100

def show():
    print(x)

show()




# =================================================================

# nested function

def outer():
    print("This is a outer function")

    def inner():
        print("This is a inner function")
    
    inner()

outer()



# ==================================================================


# Recusrive function
#Factorial example

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))


# ==================================================================

# Lambda Function
# It is a anonymous function which is written in a single line.

# lambda arguments : expression


square = lambda x: x*x

print(square(5))