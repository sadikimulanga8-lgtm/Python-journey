```python
# 🐍 Day 7 - File Handling
# Python Learning Journey


# ==========================================
# 1. WRITING TO A FILE
# ==========================================

# "w" means write.
# If the file does not exist, Python creates it.

with open("notes.txt", "w") as file:
    file.write("This is my Python learning journey.\n")
    file.write("Today I am learning file handling.\n")

print("File created successfully.")


# ==========================================
# 2. READING A FILE
# ==========================================

with open("notes.txt", "r") as file:
    content = file.read()

print("\nFile contents:")
print(content)


# ==========================================
# 3. READING LINE BY LINE
# ==========================================

with open("notes.txt", "r") as file:

    for line in file:
        print("Line:", line.strip())


# ==========================================
# 4. ADDING MORE INFORMATION
# ==========================================

# "a" means append.
# It adds information without deleting
# what is already in the file.

with open("notes.txt", "a") as file:
    file.write("I am continuing to improve my Python skills.\n")

print("\nNew information added.")


# ==========================================
# 5. READING THE UPDATED FILE
# ==========================================

with open("notes.txt", "r") as file:
    content = file.read()

print("\nUpdated file:")
print(content)


# ==========================================
# 6. CHECKING IF A FILE EXISTS
# ==========================================

import os

if os.path.exists("notes.txt"):
    print("notes.txt exists.")
else:
    print("notes.txt does not exist.")


# ==========================================
# 7. FILE INFORMATION
# ==========================================

if os.path.exists("notes.txt"):

    file_size = os.path.getsize("notes.txt")

    print("File size:", file_size, "bytes")


# ==========================================
# 8. CYBERSECURITY EXAMPLE
# ==========================================

# Imagine these are login events
# recorded by a security system.

login_events = [
    "Successful login - user: admin",
    "Failed login - user: admin",
    "Failed login - user: admin",
    "Successful login - user: student"
]

with open("login_log.txt", "w") as file:

    for event in login_events:
        file.write(event + "\n")

print("\nLogin log created.")


# ==========================================
# 9. FINDING FAILED LOGIN ATTEMPTS
# ==========================================

failed_attempts = 0

with open("login_log.txt", "r") as file:

    for line in file:

        if "Failed login" in line:
            failed_attempts += 1

print("Failed login attempts:", failed_attempts)


if failed_attempts >= 3:
    print("Warning: Multiple failed login attempts detected.")
else:
    print("No unusual number of failed login attempts detected.")


# ==========================================
# WHAT I LEARNED TODAY
# ==========================================

# - How to create a file
# - How to write to a file
# - How to read a file
# - How to read a file line by line
# - How to append information
# - How to check whether a file exists
# - How to check file size
# - How Python can process simple security logs
```
