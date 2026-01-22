#Example 
class Employee:
    language = "python" #class attributes
    salary = 30000
    def getInfo(self): #self call karna padega warna error aega
        print(f"The language is {self.language} and salary {self.salary}")

Amit = Employee()
Amit.language = "Java" #Output java aega, because instance(object) attributes over write kr deti hai class attributes pe
print(Amit.language, Amit.salary)

Amit.getInfo()