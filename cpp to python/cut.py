from segment import Segment
from line import Line
from random import randint
from point import Point

cut_type = ['VERTICAL_SOURCE', 'VERTICAL_TARGET', 'SEGMENT', 'SEGMENT_INTERSECTION', 'NONE']

def generate_point():
    a = randint(1, 30)
    b = randint(1, 30)
    p = Point(a, b)
    return p


class Cut:
    def __init__(self,type):
        self.seg = Segment()
        self.intersecting_segment = Segment()
        self.type = type

    def priority(self):
        return self.seg.priority

    def intersecting_lines(self, line_1, line_2):
            A = line_1.get_point_1()
            B = line_1.get_point_2()
            C = line_2.get_point_1()
            D = line_2.get_point_2()
            a1 = B.y - A.y
            b1 = A.x - B.x
            c1 = a1 * (A.x) + b1 * (A.y)

            # Line CD represented as a2x + b2y = c2
            a2 = D.y - C.y
            b2 = C.x - D.x
            c2 = a2 * (C.x) + b2 * (C.y)

            determinant = a1 * b2 - a2 * b1

            if (determinant == 0):
                # The lines are parallel. This is simplified
                # by returning a pair of FLT_MAX
                return Point(10 ** 9, 10 ** 9)
            else:
                x = (b2 * c1 - b1 * c2) / determinant
                y = (a1 * c2 - a2 * c1) / determinant
                return Point(x, y)

    def intersecting_Segments(self, line_1, line_2):
        A = line_1.get_point_1()
        B = line_1.get_point_2()
        C = line_2.get_point_1()
        D = line_2.get_point_2()
        x1, y1 = A
        x2, y2 = B
        x3, y3 = C
        x4, y4 = D
        denominator = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
        if denominator == 0:  # parallel
            return None
        ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
        if ua < 0 or ua > 1:  # out of range
            return None
        ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator
        if ub < 0 or ub > 1:  # out of range
            return None
        x = x1 + ua * (x2 - x1)
        y = y1 + ua * (y2 - y1)
        return Point(x, y)

    def get_defining_line(self):
        if self.type == cut_type[0]:







