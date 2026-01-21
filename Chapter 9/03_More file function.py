f = open("newfile.txt")

# puri file ko read karne ke liye je code lagega
            # line = f.readlines()
            # print(line, type(line))

# koi indivial line read karani ho to readline lagta or pura file read karana ho to readlines lagta hai

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))

line6 = f.readline()
print(line6, type(line6))

line7 = f.readline()
print(line7, type(line7))

line8 = f.readline()  #agar line 8 me kuch nhi hoga to code ko koi farak nhi padega, program isko ignore mardega
print(line8, type(line8))
print(line8 =="") #output true aega kyunki je blank hai

f.close()