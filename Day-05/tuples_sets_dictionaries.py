# 🐍 Day 5 - Tuples, Sets & Dictionaries
# Python Learning Journey


# ==========================================
# 1. TUPLES
# ==========================================

# A tuple is an ordered collection of values.
# Unlike a list, a tuple cannot normally be changed.

coordinates = (25.75, 28.19)

print("Coordinates:", coordinates)

print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])


# ==========================================
# 2. SETS
# ==========================================

# A set stores unique values.
# Duplicate values are automatically removed.

numbers = {1, 2, 3, 3, 4, 4, 5}

print("Set:", numbers)


# Adding a value to a set

numbers.add(6)

print("After adding 6:", numbers)


# Removing a value

numbers.remove(2)

print("After removing 2:", numbers)


# ==========================================
# 3. DICTIONARIES
# ==========================================

# A dictionary stores information using
# key-value pairs.

student = {
    "name": "Mulanga",
    "age": 20,
    "course": "Computer Science"
}

print(student)


# ==========================================
# 4. ACCESSING DICTIONARY VALUES
# ==========================================

print("Name:", student["name"])
print("Course:", student["course"])


# ==========================================
# 5. ADDING DATA TO A DICTIONARY
# ==========================================

student["career_goal"] = "Cybersecurity"

print(student)


# ==========================================
# 6. CHANGING DATA
# ==========================================

student["age"] = 21

print("Updated age:", student["age"])


# ==========================================
# 7. REMOVING DATA
# ==========================================

student.pop("career_goal")

print(student)


# ==========================================
# 8. LOOPING THROUGH A DICTIONARY
# ==========================================

for key, value in student.items():
    print(key, ":", value)


# ==========================================
# 9. CYBERSECURITY EXAMPLE
# ==========================================

user = {
    "username": "admin",
    "failed_logins": 5,
    "account_locked": False
}

print("\nSecurity Information")

print("Username:", user["username"])
print("Failed login attempts:", user["failed_logins"])

if user["failed_logins"] >= 5:
    user["account_locked"] = True

print("Account locked:", user["account_locked"])


# ==========================================
# 10. PRACTICE CHALLENGE
# ==========================================

# Create your own dictionary containing:
# - your name
# - your favourite programming language
# - your current Python day
# - your career goal

my_profile = {
    "name": "Mulanga",
    "favourite_language": "Python",
    "python_day": 5,
    "career_goal": "Cybersecurity"
}

print("\nMy Python Profile")

for key, value in my_profile.items():
    print(key, ":", value)


# ==========================================
# WHAT I LEARNED TODAY
# ==========================================

# - Tuples store ordered data that should not change.
# - Sets store unique values.
# - Dictionaries store key-value pairs.
# - Dictionary values can be accessed using their keys.
# - Dictionary data can be added, changed and removed.
# - Dictionaries can be used to represent structured information.
