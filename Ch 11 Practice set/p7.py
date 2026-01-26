class vector():
    def __init__(self, list):
        self.list = list
    
    def __len__(self):
        return len(self.list)


V1 = vector([1, 2, 3])

print(len(V1))