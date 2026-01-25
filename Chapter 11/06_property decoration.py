class employee():
    a = 1

    @classmethod 
    def show(cls):
        print(f"The value of class attributes is {cls.a} ")

    @property  #isko getter method bhi bolte hai
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter #upper wali method donate karti hai je wali define karti hai
    def name(self, value):
        self.Fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        

e = employee()
e.a = 23
e.name = "Amit Singh"
print(e.Fname, e.lname)
e.show()