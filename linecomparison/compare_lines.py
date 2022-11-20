import logging
import math


class Line:
    def __init__(self, para):
        self.x1 = para.get('x1')
        self.x2 = para.get('x2')
        self.y1 = para.get('y1')
        self.y2 = para.get('y2')
        self.x3 = para.get('x3')
        self.x4 = para.get('x4')
        self.y3 = para.get('y3')
        self.y4 = para.get('y4')

    def compare_line(self):
        """
        Function calculate length of lines
        :return: length of line
        """
        try:
            line_one = math.sqrt(math.pow((self.x2 - self.x1), 2)) + math.sqrt(math.pow((self.y2 - self.y1), 2))
            line_two = math.sqrt(math.pow((self.x4 - self.x3), 2)) + math.sqrt(math.pow((self.y4 - self.y3), 2))

            if line_one == line_two:
                print("Line1 and Line2 equals")
            elif line_one > line_two:
                print("Line1 greater than Line2")
            else:
                print("Line2 is greater than Line1")

        except Exception as e:
            logging.exception(e)


def length_lines():
    """
    Function to take user input and to call compare_line function

    """
    try:
        x1 = int(input("Enter x1: "))
        x2 = int(input("Enter x2: "))
        y1 = int(input("Enter y1: "))
        y2 = int(input("Enter y2: "))
        x3 = int(input("Enter x3: "))
        x4 = int(input("Enter x4: "))
        y3 = int(input("Enter y3: "))
        y4 = int(input("Enter y4: "))

        lines = Line({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'x3': x3, 'x4': x4, 'y3': y3, 'y4': y4})
        lines.compare_line()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    length_lines()

