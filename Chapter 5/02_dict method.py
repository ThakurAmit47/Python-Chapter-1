marks = {
    "Amit": 56,
    "Krishna": 45, #this is mutable they can change
    "Akash": 12
}
print(marks.items()) #Returns a list of (key,value)tuples
print(marks.keys()) #Returns a list containing left side elements.
marks.update({"Amit": 57, "Narayan": 32 }) #Updates the numbers and also add new names with numbers
print(marks.values()) #Returns a list containing  right side elements.
print(marks.get("Aman")) #this give none for not finding
# print(marks["Aman"]) #this give error for not finding

# Python Dictionary Methods (Beginner Friendly)
# Dictionary = key : value pair

data = {
    "name": "Amit",
    "age": 19,
    "city": "Delhi",
    "skills": "Python"
}

# 1. get() – key ki value deta hai (error nahi deta agar key na mile)
print(data.get("name"))
print(data.get("salary", "Not Found"))   # default value

# 6. pop() – given key ko remove karke value return karta hai
data.pop("city")
print(data)

# 7. popitem() – last inserted key-value pair remove karta hai
data.popitem()
print(data)

# 8. clear() – dictionary ko empty bana deta hai
temp = data.copy()
temp.clear()
print(temp)

# 9. copy() – dictionary ka copy banata hai
new_data = data.copy()
print(new_data)

# 10. setdefault() – key nahi hogi to add karega
data.setdefault("gender", "Male")
print(data)

# ===============================
# Extra useful checks
# ===============================

# Membership check
print("name" in data)       # True
print("salary" not in data) # True

# Length of dictionary
print(len(data))
