class Distance:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calculate_distance(self):
        x_dis = self.point1[0] - self.point2[0]
        y_dis = self.point1[1] - self.point2[1]
        distance = (x_dis**2 + y_dis**2)**0.5
        print(f"Distance between two points: {distance}") 


dis = Distance((0, 2), (13, 24))
dis.calculate_distance()