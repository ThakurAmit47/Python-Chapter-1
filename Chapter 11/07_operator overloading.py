class Number():
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        return self.n - num.n
    
    def __mul__(self, num):
        return self.n * num.n
    
    
    def __floordiv__(self, num):
        return self.n // num.n
    
################################     Calculation Ke liye Fuction hai
n = Number(10)
m = Number(5)

print(n + m)
print(n - m)
print(n * m)
print(n // m)