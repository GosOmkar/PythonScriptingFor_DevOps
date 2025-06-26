# Python Basics for Beginners :-

This README provides beginner-friendly Python concepts explained in very simple English. No emojis, just clear explanations. Ideal for absolute beginners and scripting learners.

---

## 1. Variables and Constants

- **Variables** store values.
- **Constants** are values that don't change (by convention, written in capital letters).

Example:
```python
a = 10  # variable
PI = 3.14  # constant (by naming convention)
```

---

## 2. Data Types

Python has several built-in data types:
- `int` → Integer (e.g. `10`)
- `float` → Decimal numbers (e.g. `2.3`)
- `str` → String/Text (e.g. `'omkar'`)
- `bool` → Boolean (e.g. `True`, `False`)

### How to Check Data Type
```python
a = 10
b = 2.3
c = "omkar"

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
```

---

## 3. Type Casting

Convert one data type to another.

Example:
```python
a = 10
print(float(a))  # 10.0
```

---

## 4. Operators

Operators are used to perform operations.

### Arithmetic Operators:
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

### Assignment Operator:
- `=` Assign a value

### Comparison Operators:
- `<`, `<=`, `>`, `>=`, `==`, `!=`

### Logical Operators:
- `and`, `or`, `not`

---

## 5. Input and Output

### Taking Input:
```python
name = input("Enter your city name: ")
```

### Printing Output:
```python
print("I am from", name)
print(f"I am from {name}")  # f-string formatting
```

---

## 6. Conditionals (if, elif, else)

Used to make decisions in code.

```python
age = 20

if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")
```

---


# Python Intermediate :- 

## 7. Functions

Used to group code for reuse.

### Basic Function:
```python
def greet():
    print("Hello, welcome to Python!")

greet()
```

### Function with Argument:
```python
def greet(name):
    print(f"Hello {name}, welcome to Python!")

greet("Omkar")
```

---

## 8. Core Data Structures

### List:
```python
my_list = [1, 2, 3]
```

### Tuple (immutable):
```python
my_tuple = (1, 2, 3)
```

### Set (unique, unordered):
```python
my_set = {1, 2, 3}
```

### Dictionary (key-value pairs):
```python
my_dict = {"name": "Omkar", "age": 25}
```

---

## 9. Classes (Object-Oriented Programming)

Used to define custom data types.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

p = Person("Omkar")
p.say_hello()
```

---

## 10. File Handling

### Read from File:
```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

### Write to File:
```python
file = open("example.txt", "w")
file.write("This is a new line.")
file.close()
```

### Append to File:
```python
file = open("example.txt", "a")
file.write("\nThis is an added line.")
file.close()
```

### Using with (auto close):
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 11. Exception Handling

Handle errors during program execution.

### Basic Example:
```python
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

### Multiple Exceptions:
```python
try:
    file = open("myfile.txt")
    num = int("abc")
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Cannot convert string to number.")
```

### Finally Block:
```python
try:
    file = open("example.txt")
except:
    print("Some error occurred.")
finally:
    print("This block always runs.")
```

---

Feel free to practice and expand these topics as you grow in Python programming!
