import matplotlib

class Line:

    def __init__(self, p1, p2):
        self.point_1 = p1
        self.point_2 = p2

    def create_line(self):
        x_values = [self.point_1[0], self.point_2[0]]
        y_values = [self.point_1[1], self.point_2[1]]
        matplotlib.plot(x_values, y_values, 'bo', linestyle="--")

    def get_point_1(self):
        return self.point_1

    def get_point_2(self):
        return self.point_2