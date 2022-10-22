class GetSubsets:
    def __init__(self, values):
        self.values = values

    def generate_subsets(self):
        x = len(self.values)
        res = []
        for i in range(1 << x):
            res.append([self.values[j] for j in range(x) if (i & (1 << j))])
        return res


sub = GetSubsets([4, 5, 6])
print(sub.generate_subsets())
