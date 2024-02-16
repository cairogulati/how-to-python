# 02. How to Use the print() Statement in Python
The print() statement in Python is one of the most fundamental ways to display information to the user. It allows you to output text, variables, and expressions to the console or standard output device.

## Basic Usage
To print a simple string or text to the console, you can use the print() function:

```python
print("Hello, World!")
```
## Printing Variables
You can also print the value of variables using the print() function:

```python
x = 10
print("The value of x is:", x)
```

## Printing Multiple Values
The print() function can accept multiple arguments, separated by commas. It will print each argument, separated by a space:

```python
name = "Alice"
age = 30
print("Name:", name, "Age:", age)
```

## Formatting Strings (f-strings)
Python also supports formatted string literals, or f-strings, which allow you to embed expressions inside string literals. This provides a more concise and readable way to format output:
 
 ```python
name = "Bob"
age = 25
print(f"Name: {name}, Age: {age}")
```

Another way to formatting is: 

 ```python
name = "Bob"
age = 25
print("Name: {}, Age: {}".format(name, age))
```

## Controlling How Things are Printed
You can also control how things are printed, like adding a space instead of a new line at the end:

 ```python
print("Hello", end=" ")
print("world", end="!")
```

## Printing to a File
Lastly, you can even print stuff to a file if you want:

 ```python
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
```

This will put "Hello, file!" in a file called output.txt.
To put anything is a txt file you will need to convert it into string first, Keep up to find out how to do that. 

## Conclusion
The print() statement is a powerful tool for displaying information in Python programs. Whether you need to print simple text, variables, or formatted output, print() provides a flexible and convenient way to interact with the user.

Experiment with different ways of using print() to enhance the readability and usability of your Python programs.

That's it! print() is your friend for showing what's happening in your Python programs. It's great for seeing results, checking values, or just saying "Hello" to the world!

If you want to try out the different ways to use print statement go to [Try here!](./print.py).