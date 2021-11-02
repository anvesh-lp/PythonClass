
# define a class
import math


class Rectangle:
    """ This is a class that reports on rectangles """

    def __init__(self, length, width):  # this init sets fields
        self.l = length
        self.w = width

    def area(self):  # find area
        return self.l * self.w

    def circum(self):  # find circumference
        return (self.l + self.w) * 2

    def isSquare(self):  # check if its a square
        if self.l == self.w:
            return True
        else:
            return False

    def isSilly(self):  # check if its silly
        if self.l <= 0 or self.w <= 0:
            return "is silly"
        else:
            return "is not silly"

    # to calculate the size of the rectangle.
    def calculateSize(self):
        # Checking the condition
        if self.l > self.w:
            # returning the output if condition is met
            return "Rectangle is taller"
        else:
            return "Rectangle is shorter"

    # To calculate the diagonal fo the rectangle.
    def calcualteDiagonal(self):
        # formula to calculate the diagional fo the rectangle is d = √(l² + w²)
        square=math.sqrt(self.l*self.l+self.w*self.w)
        return square

        # main method


def main():
    # set fields for three shapes
    shape1 = Rectangle(4, 36)
    shape2 = Rectangle(2, 2)
    shape3 = Rectangle(20, 5)

    # check on area
    print("Shape 1 area is", shape1.area())
    print("Shape 2 area is", shape2.area())

    # check on circumference
    print("Shape 1 circumference is", shape1.circum())
    print("Shape 2 circumference is", shape2.circum())

    # see if shape is a square
    if (shape1.isSquare()):
        print("Shape 1 is a square")
    else:
        print("Shape 1 is not a square")

    if (shape2.isSquare()):
        print("Shape 2 is a square")
    else:
        print("Shape 2 is not a square")

    # check if shape is silly
    print("Shape 2", shape2.isSilly())
    print("Shape 3", shape3.isSilly())

    print()
    print("Calculating the size of the rectangle")
    print()

    print(shape2.calculateSize())
    print(shape1.calculateSize())
    print(shape3.calculateSize())
    print()
    print("Calculating the diagonal fo the rectangle")
    print()
    print(shape2.calcualteDiagonal())
    print(shape1.calcualteDiagonal())
    print(shape3.calcualteDiagonal())


#    print(isSilly(-3,0))


# start process
if __name__ == "__main__":
    main()
