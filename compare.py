import cv2
import numpy as np
import math


def distance(A, B):
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


class Couple:
    def __init__(self, p1, p2):
        self.edge = distance(p1, p2)
        if p1[2] > p2[2]:
            self.area1 = p1[2]
            self.area2 = p2[2]
            self.angle1 = p1[3]
            self.angle2 = p2[3]
        else:
            self.area1 = p2[2]
            self.area2 = p1[2]
            self.angle1 = p2[3]
            self.angle2 = p1[3]

    def __eq__(self, other):
        if (abs(self.area1 - other.area1) > 300
                or abs(self.area2 - other.area2) > 300):
            return False

        if abs(self.edge - other.edge) > 35:
            return False

        dif1 = abs(self.angle1 - self.angle2)
        dif2 = abs(other.angle1 - other.angle2)

        if (abs(self.angle1 - other.angle1 > 3)
                or abs(self.angle2 - other.angle2) > 3):
            return False

        if abs(dif1 - dif2) > 4:
            return False

        return True

    def __str__(self):
        return str([self.area1, self.area2, self.edge, self.angle1, self.angle2])


def open_file(filename, array):
    with open(filename, "r") as file:
        for x in file:
            array.append([int(number) for number in x.split()])


data1 = []
data2 = []

file1 = input()
file2 = input()

open_file(file1, data1)
open_file(file2, data2)

n1 = 1
n2 = 1

yellow_color = (0, 255, 255)
pink_color = (255, 0, 255)
img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")

r1 = 2
r2 = 2

status = False

for x1 in data1[:]:  # выбераем первую точку из первого изображения
    for x2 in data1[n1:]:  # выбераем вторую точку из первого изображения
        A = Couple(x1, x2)  # первая пара
        for y1 in data2[:]:  # выбераем первую точку из второго изображения
            for y2 in data2[n2:]:  # выбераем вторую точку из второго изображения
                B = Couple(y1, y2)  # вторая пара
                if A == B:
                    print(x1[0], x1[1], x1[2], sep=' ', file=open('data1.txt', 'a'))
                    print(y1[0], y1[1], y1[2], sep=' ', file=open('data2.txt', 'a'))

                    print(x2[0], x2[1], x2[2], sep=' ', file=open('data1.txt', 'a'))
                    print(y2[0], y2[1], y2[2], sep=' ', file=open('data2.txt', 'a'))

                    cv2.circle(img1, (x1[0], x1[1]), r1, yellow_color, 2)
                    cv2.circle(img1, (x2[0], x2[1]), r1 + 3, pink_color, 1)
                    cv2.circle(img2, (y1[0], y1[1]), r2, yellow_color, 2)
                    cv2.circle(img2, (y2[0], y2[1]), r2 + 3, pink_color, 1)
                    cv2.imwrite("/home/arsen/Documents/programs/diploma/img1.jpg", img1)
                    cv2.imwrite("/home/arsen/Documents/programs/diploma/img2.jpg", img2)
            n2 += 1
        n2 = 1
    n1 += 1