# Python Tuple Methods (Beginner Friendly)
# Tuple = ordered, immutable (change nahi hota)

t = (10, 20, 30, 20, 40, 20)

# 1. count() – tuple me kisi value kitni baar aayi hai
print(t.count(20))   # Output: 3

# 2. index() – kisi value ka first index batata hai
print(t.index(30))   # Output: 2

# ===============================
# Built-in functions jo tuple ke saath bahut use hote hain
# ===============================

# 3. len() – tuple ki total length
print(len(t))        # Output: 6

# 4. max() – tuple ka sabse bada element
print(max(t))        # Output: 40

# 5. min() – tuple ka sabse chhota element
print(min(t))        # Output: 10

# 6. sum() – tuple ke sab numbers ka sum
print(sum(t))        # Output: 140

# 7. sorted() – tuple ko sort karke list return karta hai
print(sorted(t))     # Output: [10, 20, 20, 20, 30, 40]

# 8. tuple() – kisi iterable ko tuple me convert karta hai
lst = [1, 2, 3]
print(tuple(lst))    # Output: (1, 2, 3)

# ===============================
# Tuple unpacking (important 🔥)
# ===============================
a, b, c, d, e, f = t
print(a, b, c)       # Output: 10 20 30

# ===============================
# Membership check
# ===============================
print(20 in t)       # True
print(41 not in t)   # True
