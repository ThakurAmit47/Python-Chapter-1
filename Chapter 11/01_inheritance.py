class Employee:
    company = "tata steel"
    def show(self):
        print(f"The name of employee {self.name}")

class programmer(Employee):
    company = "Mahindra"

    def showtech(self):
        print(f"The salary of the employee {self.salary}")

a = Employee()
b = programmer()
print(a.company, b.company)
