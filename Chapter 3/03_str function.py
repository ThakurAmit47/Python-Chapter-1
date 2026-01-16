name = "Amit"

print(len(name)) #ye total word batata hai
print(name.endswith("mit")) #ye dhekhta hai jo sabd end me likhe hai wo hai ya nhi
print(name.startswith("Am")) #ye start ka dekhta hai
# uper dono fucntion capital ki jagah small likhne se bhi wrong kar dete hai
print(name.capitalize()) #ye first letter ko capital kare bss

# Python String Most Used Functions (Beginner Friendly)
# String = text data type

text = "  Hello Python World  "

# 1. lower() – string ko lowercase me convert karta hai
print(text.lower())

# 2. upper() – string ko uppercase me convert karta hai
print(text.upper())

# 3. strip() – starting aur ending ke extra spaces remove karta hai
print(text.strip())

# 4. replace() – ek word/character ko dusre se replace karta hai
print(text.replace("Python", "Java"))

# 5. split() – string ko list me tod deta hai (space ke basis pe)
print(text.split())

# 6. find() – kisi word ka index batata hai (nahi mila to -1)
print(text.find("Python"))

# 7. count() – kisi word/character ki frequency batata hai
print(text.count("o"))

# 8. startswith() – check karta hai string kis word se start ho rahi hai ya nahi
print(text.startswith("  He"))

# 9. endswith() – check karta hai string kis word pe end ho rahi hai ya nahi
print(text.endswith("World  "))

# 10. capitalize() – sirf first letter capital karta hai
print(text.capitalize())

# 11. title() – har word ka first letter capital karta hai
print(text.title())

# 12. isalpha() – sirf alphabets hai ya nahi (spaces allowed nahi)
print("Hello".isalpha())

# 13. isdigit() – sirf digits hai ya nahi
print("12345".isdigit())

# 14. isalnum() – alphabets + digits (space allowed nahi)
print("Hello123".isalnum())

# 15. len() – string ki total length batata hai
print(len(text))

# 16. join() – list ke elements ko string me jodta hai
words = ["Python", "is", "awesome"]
print(" ".join(words))
