import math
import matplotlib.pyplot as plt
import numpy as np

class Point:
    '''Creates a point on a coordinate plane with values x and y.'''
    X = 0
    Y = 0

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.X = x
        self.Y = y

    def move(self, dx, dy):
        '''Determines where x and y move'''
        self.X = self.X + dx
        self.Y = self.Y + dy

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx ** 2 + dy ** 2)

    # Draw a point based on the x's, y's axis value.
    def draw_points(points, name , color):
        # Draw a points at the given location with size 1000
        xs = []
        ys = []
        for point in points:
            xs.append(point.getX())
            ys.append(point.getY())

        plt.scatter([xs], [ys], c=color)
        plt.show()

        # Set chart title.
        plt.title(name, fontsize=19)

        # Set x axis label.
        plt.xlabel("X Label", fontsize=10)

        # Set y axis label.
        plt.ylabel("Y Label", fontsize=10)

        # Set size of tick labels.
        plt.tick_params(axis='both', which='major', labelsize=9)

        # Display the plot in the matplotlib's viewer.
        plt.savefig(name + ".png")
