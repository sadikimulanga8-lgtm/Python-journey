# 🐍 Day 4 - Python Lists
# Python Learning Journey


# ==========================================
# 1. CREATING A LIST
# ==========================================

languages = ["Python", "C#", "Java", "SQL"]

print(languages)


# ==========================================
# 2. ACCESSING LIST ITEMS
# ==========================================

print(languages[0])
print(languages[1])

# Negative indexes start from the end
print(languages[-1])


# ==========================================
# 3. CHANGING A LIST ITEM
# ==========================================

languages[2] = "JavaScript"

print(languages)


# ==========================================
# 4. ADDING ITEMS
# ==========================================

languages.append("HTML")

print(languages)


# Insert an item at a specific position
languages.insert(1, "CSS")

print(languages)


# ==========================================
# 5. REMOVING ITEMS
# ==========================================

languages.remove("CSS")

print(languages)


# Remove the last item
languages.pop()

print(languages)


# ==========================================
# 6. LIST LENGTH
# ==========================================

print("Number of languages:", len(languages))


# ==========================================
# 7. LOOPING THROUGH A LIST
# ==========================================

for language in languages:
    print("I am learning:", language)


# ==========================================
# 8. NUMBERS IN A LIST
# ==========================================

numbers = [10, 5, 20, 3, 15]

print("Original numbers:", numbers)

numbers.sort()

print("Sorted numbers:", numbers)


# ==========================================
# 9. FINDING THE HIGHEST AND LOWEST
# ==========================================

print("Highest number:", max(numbers))
print("Lowest number:", min(numbers))


# ==========================================
# 10. PRACTICE CHALLENGE
# ==========================================

shopping_list = ["Bread", "Eggs", "Milk"]

shopping_list.append("Apples")
shopping_list.append("Rice")

print("My shopping list:")

for item in shopping_list:
    print("-", item)


# ==========================================
# WHAT I LEARNED TODAY
# ==========================================

# - How to create lists
# - How to access list items
# - How to change list items
# - How to add items using append() and insert()
# - How to remove items using remove() and pop()
# - How to find the length of a list
# - How to loop through a list
# - How to sort a list
# - How to find the highest and lowest values
