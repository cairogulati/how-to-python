# Printing a String
print("Hello, World!")

# Printing a variable
x = 10
print("The value of x is:", x)

# Printing Multiple variable in 1 print statement
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

#Using formatting to print the variable values
name = "Bob"
age = 25

print(f"Name: {name}, Age: {age}")
# or 
print("Name: {}, Age: {}".format(name, age))

# Controlling how the print statement ends
print("Hello", end=" ")
print("world", end="!")

# Printing not to console but to a file
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)