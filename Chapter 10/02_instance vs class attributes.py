#Example 
class Employee:
    language = "python" #class attributes
    salary = 30000

Amit = Employee()
Amit.language = "Java" #Output java aega, because instance(object) attributes over write kr deti hai class attributes pe
print(Amit.language, Amit.salary)

#Note: Instance attributes, take preference over class attributes during assignment & retrieval.
 