# 🐍 Day 6 - Strings & String Methods
# Python Learning Journey


# ==========================================
# 1. CREATING STRINGS
# ==========================================

name = "Mulanga"
message = "Welcome to my Python journey!"

print(name)
print(message)


# ==========================================
# 2. STRING LENGTH
# ==========================================

print("Name length:", len(name))


# ==========================================
# 3. ACCESSING CHARACTERS
# ==========================================

word = "Python"

print(word[0])   # First character
print(word[1])   # Second character
print(word[-1])  # Last character


# ==========================================
# 4. STRING SLICING
# ==========================================

print(word[0:3])
print(word[2:6])


# ==========================================
# 5. CHANGING LETTER CASE
# ==========================================

text = "Python Is Fun"

print(text.upper())
print(text.lower())
print(text.title())


# ==========================================
# 6. REMOVING EXTRA SPACES
# ==========================================

username = "   Mulanga   "

print(username)
print(username.strip())


# ==========================================
# 7. REPLACING TEXT
# ==========================================

sentence = "I am learning Java."

new_sentence = sentence.replace("Java", "Python")

print(new_sentence)


# ==========================================
# 8. CHECKING TEXT
# ==========================================

email = "mulanga@example.com"

print(email.startswith("mulanga"))
print(email.endswith(".com"))

print("@" in email)


# ==========================================
# 9. SPLITTING A STRING
# ==========================================

full_name = "Mulanga Sadiki"

names = full_name.split()

print(names)
print(names[0])
print(names[1])


# ==========================================
# 10. JOINING STRINGS
# ==========================================

words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print(sentence)


# ==========================================
# 11. F-STRINGS
# ==========================================

name = "Mulanga"
age = 20
career = "Cybersecurity"

introduction = f"My name is {name}, I am {age} years old, and I am interested in {career}."

print(introduction)


# ==========================================
# 12. CYBERSECURITY EXAMPLE
# ==========================================

username = "  ADMIN  "

username = username.strip().lower()

print("Processed username:", username)

if username == "admin":
    print("Administrator account detected.")
else:
    print("Standard user account detected.")


# ==========================================
# 13. PASSWORD CHECK
# ==========================================

password = "Python123!"

print("Password length:", len(password))

if len(password) >= 8:
    print("Password has at least 8 characters.")
else:
    print("Password is too short.")


# ==========================================
# 14. PRACTICE CHALLENGE
# ==========================================

user_input = input("Enter your name: ")

clean_name = user_input.strip().title()

print(f"Hello, {clean_name}!")
print(f"Your name has {len(clean_name)} characters.")


# ==========================================
# WHAT I LEARNED TODAY
# ==========================================

# - How to create strings
# - How to find the length of a string
# - How to access individual characters
# - How to slice strings
# - How to change text to upper/lower case
# - How to remove extra spaces
# - How to replace text
# - How to check strings
# - How to split and join strings
# - How to use f-strings
# - How strings can be used in cybersecurity
