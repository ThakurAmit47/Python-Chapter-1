class Employee:
    company = "tata steel"
    def show(self):
        print(f"The name of company {self.company}")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"The employee of the company language are {self.language}")



class programmer(Employee, coder):
    company = "Mahindra"

    def showtech(self):
        print(f"The salary of the employee of {self.company}")

a = Employee()
b = programmer()

b.show()
b.printlanguage()
b.showtech()