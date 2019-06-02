import sys

import numpy as np

import scipy as scipy
from math import ceil
from scipy.spatial import distance
from Point import *
from random import randint
import random

'''Global Varibles'''


# Creating random points
def createPoints(num, size):
    points = []
    rows = np.random.randint(0, size, num)
    cols = np.random.randint(0, size, num)

    for i in range(num):
        points.append(Point(rows[i], cols[i]))

    Point.draw_points(points, "Random Points", 'red')
    return points


def createNeurons(num, size):
    neurons = []
    for i in range(num):
        neurons.append(Point(int(i * size / num), size / 2))

    Point.draw_points(neurons, "init", 'blue')
    return neurons


def findWinner(point):
    winner = 0
    for index in range(len(neurons)):
        if (neurons[winner].distance(point) > neurons[index].distance(point)):
            winner = index

    return winner


def train(neighbors, l_rate):
    randPoint = points[np.random.randint(0, 2499)]
    indexNeuron = findWinner(randPoint)
    for i in range(1, neighbors):
        if (indexNeuron - i > 0):
            neurons[indexNeuron - i].move(l_rate * neurons[indexNeuron-i].distance(randPoint), l_rate * neurons[indexNeuron-i].distance(randPoint))
        if (indexNeuron + i < len(neurons)):
            neurons[indexNeuron + i].move(l_rate * neurons[indexNeuron-i].distance(randPoint), l_rate * neurons[indexNeuron-i].distance(randPoint))


if __name__ == '__main__':
    neurons = createNeurons(100, 2500)
    l_rate = 0.7
    epochs = 30
    neighbors = 10
    points = createPoints(2500, 2500)
    for epoch in range(epochs):
        print("Starting epoch number " + str(epoch))
        for i in range(1000):
            train(neighbors, l_rate)
            if (i % 100 == 0 and neighbors > 1):
                neighbors -= 1
            if (i % 200 == 0 and l_rate > 0):
                l_rate = l_rate * (9 / 10)
        Point.draw_points(neurons, "Epoch number " + str(epoch), 'black')
