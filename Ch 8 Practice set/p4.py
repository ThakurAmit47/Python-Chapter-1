def natural(n):
    if(n==1):
        return 1
    return natural(n-1) + n
n = int(input("Enter naural number.: "))
print(f"the sum of natural number is:{natural(n)}")
    