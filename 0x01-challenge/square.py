#!/usr/bin/python3
"""
my square class
"""


class Square():
    """class Square"""
    def __init__(self, width=0,  height=0):
        """DOCUMENTED"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """DOCUMENTED"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """DOCUMENTED"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
