class employee():
    a = 1

    @classmethod    #Isko lagane se class ki value change nhi hoti apna hi attribute show karti hai
    def show(cls):
        print(f"The value of class attributes is {cls.a} ")

e = employee()
e.a = 23
e.show()