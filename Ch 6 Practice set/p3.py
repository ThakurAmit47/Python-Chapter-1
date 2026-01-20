s1 = "Make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

a = input("Enter text in Email: ")


if(s1 in a or s2 in a or s3 in a or s4 in a):
    print("it is spam")

else:
    print("it is not spam")