# BASIC PYTHON SYNTAX #
# 1. Print to Console:
print("Hello, World!")
# 2. Variable Assignment:
a = 'pycode.hubb'
# 3. Commenting:
# This is single line comment!
# 4. Multi-line Comment:
"""This is a multi-line comment!"""
# 5. Input from User:
name = input("Enter your name: ")
print("Hello, " + name + "!")
# 6. Data Types:
x = 10  # Integer
y = 10.5  # Float
z = "Hello"  # String   
# 7. List:
my_list = [1, 2, 3, 4, 5]  # List of integers   
# 8. Tuple:
my_tuple = (1, 2, 3, 4, 5)  # Tuple of integers 
# 9. Dictionary:
my_dict = {"name": "John", "age": 30, "city": "New York"}  # Dictionary with key-value pairs
print("Name:", my_dict["name"])  # Accessing dictionary value by key
print("Age:", my_dict["age"])  # Accessing dictionary value by key
print("City:", my_dict["city"])  # Accessing dictionary value by key
print("Hello, " + a + "!")  # Using the variable in a print statement
print("Value of x is:", x)  # Displaying the value of x
print("Value of y is:", y)  # Displaying the value of y
# 10. Set:
my_set = {1, 2, 3, 4, 5}  # Set of integers
# 11. Boolean:
is_active = True  # Boolean value
# 12. Conditional Statements:
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
# 13. Loops:
for i in range(5):
    print("Iteration:", i)
# 14. Function Definition:
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"
# 15. Function Call:
print(greet("Alice"))
# 16. Exception Handling:
try:
    result = 10 / 0  # This will raise an exception
except ZeroDivisionError as e:
    print("Error:", e)  
# 17. Importing Modules:
import math  # Importing the math module    
# 18. Using a Module Function:
print("Square root of 16 is:", math.sqrt(16))  # Using the sqrt function from the math module       
# 19. List Comprehension:
squared_numbers = [x**2 for x in range(10)]  # List comprehension to square numbers
# 20. Lambda Function:
square = lambda x: x**2  # Lambda function to square a number
# 21. Using Lambda Function:
print("Square of 5 is:", square(5))  # Using the lambda function    
# 22. File Handling:
with open("example.txt", "w") as file:  # Writing to a file
    file.write("Hello, File Handling!") 
with open("example.txt", "r") as file:  # Reading from a file
    content = file.read()
    print("File Content:", content)  # Displaying the content of the file   
# 23. Class Definition:
class Person:
    """Class to represent a person."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Method to introduce the person."""
        return f"My name is {self.name} and I am {self.age} years old."
# 24. Class Instantiation:          
john = Person("John", 30)  # Creating an instance of the Person class
print(john.introduce())  # Calling the introduce method of the Person class