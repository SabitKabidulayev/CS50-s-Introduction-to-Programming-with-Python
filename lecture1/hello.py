# Ask user for their name
name = input("What's your name? ").strip().title()
# name is a variable
# = assignment operator
# input is a function
# "What's your name? " is an argument
# argument is a value of function's parameter
# return value of input function is assigned to name var

# Say hello to user
print("hello, " + name)
print("hello,", name, sep="???")
# function can have multiple arguments

print("hello, ", end="???")
print(name)
# named parameters can be changed if needed

print('hello, "friend"')
print("hello, \"friend\"") # \ is escape character

# Remove whitespace from string
name = name.strip()
# Capitalize string
name = name.capitalize() 

print(f"hello, {name}")

# Capitalize each word
name = name.title()

# Split user's name into first name and last name
first, last = name.split(" ")

print(f"hello, {name}")
print(f"hello, {first}")

