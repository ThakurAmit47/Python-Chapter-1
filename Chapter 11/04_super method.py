class Employee():
    def __init__(self):
        print("the constructor of Employee")
    a = 1

class coder(Employee):
    def __init__(self):
        print("the constructor of coder")
    b = 2

class programmer(coder):
    def __init__(self):
        super().__init__()   #Isko lagane uper wale ka bhi contructor run hoga
        print("the constructor of programmer")
    c = 3

o = Employee()
print(o.a)

o = coder()
print(o.a, o.b)

o = programmer()
print(o.a, o.b, o.c)
