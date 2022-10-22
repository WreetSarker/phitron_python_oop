class GenerateSum:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def get_indices(self):
        for i in range(len(self.numbers)-1):
            if self.numbers[i] + self.numbers[i+1] == target:
                return i+1, i+2


numbers= [10,20,10,40,50,60,70]
target=50
gSum = GenerateSum(numbers, target)
print(gSum.get_indices())