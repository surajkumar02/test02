class Shape:
    def __init__(self,edge):
        self.edge=edge

    def area(self):
        return 0

class Square(Shape):
    def area(self,edge):
        return edge*edge
