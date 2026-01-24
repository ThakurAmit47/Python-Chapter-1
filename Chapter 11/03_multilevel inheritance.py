## Isme parents class ke child class ki class banti chali jati hai
class Employee():
    a = 1

class coder(Employee):
    b = 2

class programmer(coder):
    c = 3

o = Employee()
print(o.a)

o = coder()
print(o.a, o.b)

o = programmer()
print(o.a, o.b, o.c)

###############    Agar pehle wale b or c print karate to error aata //Same\\ Second wale me c print karate to error aata