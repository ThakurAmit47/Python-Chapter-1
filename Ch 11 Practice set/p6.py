class vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
        
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
        
    def __str__(self):
        return f"vector {self.x}i + {self.y}j + {self.z}k"


V1 = vector(3, 3, 4)
V2 = vector(4, 5, 6)
V3 = vector(7, 8, 9)

print(V1 + V2)