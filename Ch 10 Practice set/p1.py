class programmer:
    Company = "Microsoft"

    def __init__(self, name, salary, proffesion):
        self.name = name
        self.salary = salary
        self.proffesion = proffesion

    
Abhishek = programmer("Abhishek", 50000, "Full stack")
Simran = programmer("Simran", 40000, "C programmer")
Anmol = programmer("Anmol", 80000, "Data Scientist")
Akash = programmer("Akash", 30000, "DSA")
Krishna = programmer("Krishna", 60000, "Data analysist")
Aman = programmer("Aman", 200000, "Front-end")

print(Abhishek.name, Abhishek.salary, Abhishek.proffesion, Abhishek.Company)
print(Simran.name, Simran.salary, Simran.proffesion, Simran.Company)
print(Anmol.name, Anmol.salary, Anmol.proffesion, Anmol.Company)
print(Akash.name, Akash.salary, Akash.proffesion, Akash.Company)
print(Krishna.name, Krishna.salary, Krishna.proffesion, Krishna.Company)
print(Aman.name, Aman.salary, Aman.proffesion, Aman.Company)
        