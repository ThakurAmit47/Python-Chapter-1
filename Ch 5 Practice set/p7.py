d = {}
n = input("Enter your name friend 1: ")
m = input("Enter your language: ")
d.update({n: m})
n = input("Enter your name friend 2: ")
m = input("Enter your language: ")
d.update({n: m})
n = input("Enter your name friend 3: ")
m = input("Enter your language: ")
d.update({n: m})
n = input("Enter your name friend 4: ")
m = input("Enter your language: ")
d.update({n: m})
print(d)
print(d.get("amit"))
#agar ek naam do baar repeat ho jaye to last wali value hogi vohi print karaega 
#this is same as Q6