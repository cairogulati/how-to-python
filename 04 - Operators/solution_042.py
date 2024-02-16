x = 10
y = 5

# Arithmetic Operators
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y) # Floor Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation

# Comparison Operators
print(x == y) # Equal to
print(x != y) # Not equal to
print(x > y)  # Greater than
print(x < y)  # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to

# Logical Operators
print(x > 5 and y < 10)
print(x > 5 or y < 10)
print(not(x > 5 and y < 10))

# Assignment Operators
x += 1
print(x)

# Bitwise Operators
a = 60 # 0011 1100
b = 13 # 0000 1101
print(a & b) # Bitwise AND
print(a | b) # Bitwise OR
print(a ^ b) # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 2) # Left Shift
print(a >> 2) # Right Shift

# Membership Operators
list_example = [1, 2, 3, 4, 5]
print(3 in list_example)
print(6 not in list_example)

# Identity Operators
m = [1, 2, 3]
n = [1, 2, 3]
print(m is n)     # False because m and n are two different objects
print(m is not n) # True because m and n are two different objects
