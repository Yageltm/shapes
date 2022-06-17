class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length*self.width

    def __add__(self, other):
        return self.get_area()+other.get_area()


class Square(Rectangle):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length ** 2





if __name__ == "__main__":
    s = Square(5)
    r = Rectangle(8, 2)

    print(f"square area = {s.get_area()}")
    print(f"rectangle area = {r.get_area()}")

    print(f"aggregated area is: {s+r}")
