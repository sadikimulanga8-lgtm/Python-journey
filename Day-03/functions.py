# 🐍 Day 3 - Python Functions
# Python Learning Journey


# ==========================================
# 1. CREATING A SIMPLE FUNCTION
# ==========================================

def greet():
    print("Hello! Welcome to my Python journey.")


# Calling the function
greet()


# ==========================================
# 2. FUNCTION WITH A PARAMETER
# ==========================================

def greet_person(name):
    print("Hello,", name)


greet_person("Mulanga")
greet_person("Python")


# ==========================================
# 3. MULTIPLE PARAMETERS
# ==========================================

def introduce(name, career):
    print("My name is", name)
    print("I am interested in", career)


introduce("Mulanga", "Cybersecurity")


# ==========================================
# 4. RETURNING A VALUE
# ==========================================

def add_numbers(number1, number2):
    result = number1 + number2
    return result


answer = add_numbers(10, 5)

print("The answer is:", answer)


# ==========================================
# 5. EVEN NUMBER FUNCTION
# ==========================================

def is_even(number):

    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(10))
print(is_even(7))


# ==========================================
# 6. FIND EVEN NUMBERS
# ==========================================

def find_even_numbers(n):

    evens = []

    for i in range(n + 1):

        if i % 2 == 0:
            evens.append(i)

    return evens


numbers = find_even_numbers(10)

print("Even numbers:", numbers)


# ==========================================
# 7. SIMPLE CALCULATOR
# ==========================================

def calculator(number1, number2, operation):

    if operation == "+":
        return number1 + number2

    elif operation == "-":
        return number1 - number2

    elif operation == "*":
        return number1 * number2

    elif operation == "/":

        if number2 == 0:
            return "Cannot divide by zero."

        return number1 / number2

    else:
        return "Invalid operation."


print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))


# ==========================================
# WHAT I LEARNED TODAY
# ==========================================

# - How to create functions using def
# - How to call a function
# - How to use parameters
# - How to pass arguments
# - How return works
# - How functions can be reused
# - How to build a simple calculator using functions
