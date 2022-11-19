import logging
import math


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def length_line(self):
        """
        Function calculate length of lines
        :return: length of line
        """
        try:
            length = math.sqrt(math.pow((self.x2 - self.x1), 2)) + math.sqrt(math.pow((self.y2 - self.y1), 2))
            return length

        except Exception as e:
            logging.exception(e)

    def compare_line(self, line_obj):
        """
        Function to compare length of line
        """
        try:
            return self.length_line() == line_obj.length_line()
        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':
    a1 = int(input("Enter x1: "))
    b1 = int(input("Enter y1: "))
    a2 = int(input("Enter x2: "))
    b2 = int(input("Enter y2: "))
    line1 = Line(a1, b1, a2, b2)
    a1 = int(input("Enter x1: "))
    b1 = int(input("Enter y1: "))
    a2 = int(input("Enter x2: "))
    b2 = int(input("Enter y2: "))
    line2 = Line(a1, b1, a2, b2)
    print(line1.compare_line(line2))
