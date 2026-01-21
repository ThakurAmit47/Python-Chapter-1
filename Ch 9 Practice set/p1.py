f = open("p1_poem.txt")
data = f.read()
if("twinkle" in data):
    print("twinkle present in the content")
else:
    print("twinkle not present in the content")
print(data)
f.close()