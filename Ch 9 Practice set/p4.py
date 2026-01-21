word = "Donkey"

with open("p4_file.txt", "r") as f:
    content = f.read()

contentnew = content.replace(word, "######")

with open("p4_file.txt", "w") as f:
    f.write(contentnew)