a = int(input("Enter the number: "))

tableofa = [a*i for i in range(1, 11)]
with open("file.txt" , "a") as f:
    f.write(f"table of {n}: {str(tableofa)} + \n")

