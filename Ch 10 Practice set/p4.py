class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of given number is {self.n*self.n}")
    
    def cube(self):
        print(f"The cube of given number is {self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The squareroot of given number is {self.n**0.5}")
    @staticmethod
    def hello():
        print("Hello Colonel!")

    
a = calculator(16)
a.square()
a.cube()
a.squareroot()
a.hello()