a = {21, 34, 56, 32, 21, 21, "Amit"}
a.add(67) #for put value in sets
print(a, type(a))


# Python Set Methods (Beginner Friendly)
# Set = unordered collection, duplicates allowed nahi hote

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

# 1. add() – set me ek element add karta hai
s1.add(100)
print(s1)

# 2. update() – multiple elements ek saath add karta hai
s1.update([70, 80])
print(s1)

# 3. remove() – element remove karta hai (nahi mila to error)
s1.remove(20)
print(s1)

# 4. discard() – element remove karta hai (error nahi deta)
s1.discard(999)
print(s1)

# 5. pop() – random element remove karta hai
s1.pop()
print(s1)

# 6. clear() – set ko empty bana deta hai
temp = s1.copy()
temp.clear()
print(temp)

# 7. copy() – set ka copy banata hai
new_set = s1.copy()
print(new_set)

# ===============================
# Set Operations (Most Important 🔥)
# ===============================

# 8. union() – dono sets ke saare unique elements
print(s1.union(s2))

# 9. intersection() – common elements
print(s1.intersection(s2))

# 10. difference() – s1 - s2
print(s1.difference(s2))

# 11. symmetric_difference() – jo common nahi hain
print(s1.symmetric_difference(s2))

# ===============================
# Relation check
# ===============================

# 12. issubset() – s1, s2 ka subset hai ya nahi
print({30, 40}.issubset(s2))

# 13. issuperset() – s2, s1 ka superset hai ya nahi
print(s2.issuperset({50}))

# 14. isdisjoint() – koi common element hai ya nahi
print(s1.isdisjoint({50}))
