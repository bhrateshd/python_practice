# # Index starts from 0

# name = "Bhratesh"
# friend = "Manthan"
# anotherFriend = 'Rohit'

# apple = '''He Said, 
# Hi Bhratesh
# hey I am good
# I want to eat and apple'''

# print("Hello, " + name)
# print(apple)

# # Printg index 0 of name
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# for character in apple:
#     print(character)


# # String slicing and Operations on string

# names = "Bhratesh,Manthan"
# print(name[0:5])



# # We can find the length of any string using len function 

# fruit = "Mango"
# mangoLen = len(fruit)

# print(mangoLen)

# print(fruit[0:4])
# print(fruit[:4])
# print(fruit[:])


# String Methods 
# Strings are immutable - you cant change strings you can make another copy of that

# a = "Bhratesh!!!"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("Bhratesh", "John"))
# print(a.split(" "))


# find method is used to print the index
str1 = "He's name is John. He is a honest man."
print(str1.find("is")) # this will written -1 is it dosent find the exact sgtring 
# print(str1.index("ishh")) # it will print error 

# is lower = it will print true or false 
str1 = "Welcome Bhratesh"
print(str1.islower())