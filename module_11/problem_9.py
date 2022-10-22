class CalculateFunctions:
    def __init__(self, X, n):
        self.X = X
        self.n = n

    def sum(self):
        return self.X + self.n

    def pow(self):
        return self.X**self.n


fun = CalculateFunctions(3, 4)
print(fun.sum())
print(fun.pow())