import numpy as np
import cv2
import math


def find_contours(pict=str('')):
    horiz_vect = (1, 0)  # горизонтальный вектор
    radius = 3
    thickness = 2
    color_yellow = (0, 255, 255)
    hsv_min = np.array((95, 20, 5), np.uint8)
    hsv_max = np.array((187, 251, 253), np.uint8)
    imagename = 'input/' + pict
    img = cv2.imread(imagename)

    name = str()
    for letter in pict:
        if letter == '.':
            break
        name += letter
    f = open(name + ".txt", "w")
    f.close()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    color_filter = cv2.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр

    contours, hierarchy = cv2.findContours(color_filter.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:  # перебираем все найденные контуры в цикле
        rectangle = cv2.minAreaRect(contour)  # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rectangle)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат

        edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
        edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))
        edge = edge1
        if cv2.norm(edge2) > cv2.norm(edge1):
            edge = edge2

        angle = 180.0 / math.pi * math.acos(
            (horiz_vect[0] * edge[0] + horiz_vect[1] * edge[1]) / (cv2.norm(horiz_vect) * cv2.norm(edge)))
        area = int(rectangle[1][0] * rectangle[1][1])  # вычисление площади
        center = (int(rectangle[0][0]), int(rectangle[0][1]))  # центр прямоугольника

        if area > 700:
            cv2.drawContours(img, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник
            cv2.circle(img, center, radius, color_yellow, thickness)
            data = name + ".txt"
            print(center[0], center[1], area, int(angle), sep=' ', file=open(data, "a"))

    cv2.imwrite('/home/arsen/Documents/programs/diploma/output/' + pict, img)


if __name__ == '__main__':
    find_contours()