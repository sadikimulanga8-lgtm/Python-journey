```python
# 🐍 Day 8 - Error Handling
# Python Learning Journey


# ==========================================
# 1. A SIMPLE TRY / EXCEPT
# ==========================================

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid number.")


# ==========================================
# 2. HANDLING DIVISION ERRORS
# ==========================================

try:
    number1 = int(input("\nEnter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 / number2

    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")


# ==========================================
# 3. TRY / EXCEPT / ELSE
# ==========================================

try:
    age = int(input("\nEnter your age: "))

except ValueError:
    print("Invalid age.")

else:
    print("Your age is:", age)


# ==========================================
# 4. FINALLY
# ==========================================

try:
    number = int(input("\nEnter a number: "))
    print("Number:", number)

except ValueError:
    print("That was not a valid number.")

finally:
    print("This message always runs.")


# ==========================================
# 5. HANDLING A LIST ERROR
# ==========================================

languages = ["Python", "C#", "Java"]

try:
    print("\nLanguage:", languages[5])

except IndexError:
    print("That position does not exist in the list.")


# ==========================================
# 6. HANDLING A DICTIONARY ERROR
# ==========================================

user = {
    "username": "admin",
    "role": "administrator"
}

try:
    print("Email:", user["email"])

except KeyError:
    print("The email information does not exist.")


# ==========================================
# 7. CYBERSECURITY EXAMPLE
# ==========================================

failed_attempts = input("\nEnter the number of failed login attempts: ")

try:
    failed_attempts = int(failed_attempts)

    if failed_attempts >= 5:
        print("⚠️ Warning: Multiple failed login attempts detected.")

    else:
        print("Login activity is within the expected range.")

except ValueError:
    print("Invalid input. Please enter a number.")


# ==========================================
# 8. SAFE FILE READING
# ==========================================

try:

    with open("security_log.txt", "r") as file:
        logs = file.read()

    print("\nSecurity log:")
    print(logs)

except FileNotFoundError:
    print("\nSecurity log was not found.")
    print("Make sure the file exists before trying to read it.")


# ==========================================
# WHAT I LEARNED TODAY
# ==========================================

# - Errors can cause programs to stop.
# - try is used for code that might cause an error.
# - except handles the error.
# - Different errors can have different except blocks.
# - else runs when no error occurs.
# - finally runs whether an error occurs or not.
# - Error handling can make programs safer and easier to use.
```
