import sys
import numpy as np
import cv2 as cv

#hsv_min = np.array((0, 54, 5), np.uint8)
hsv_min = np.array((95, 20, 5), np.uint8)
hsv_max = np.array((187, 251, 253), np.uint8)

color_blue = (255,0,0)
color_yellow = (0,255,255)

def go(pict=str('')):
    #fn = 'input/one.png' # имя файла, который будем анализировать
    fn = 'input/' + pict
    fn = 'input/img1.jpg'
    img = cv.imread(fn)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
        box = np.int0(box) # округление координат
        area = int(rect[1][0]*rect[1][1]) # вычисление площади
        center = (int(rect[0][0]), int(rect[0][1])) # центр прямоугольника
        if area > 200:
            cv.drawContours(img,[box],0,(255,0,0),2) # рисуем прямоугольник
            cv.circle(img, center, 2, color_yellow, 2)
            #print(center[0], center[1], area, sep=' ',  file=open("data3.txt", "a"))

    cv.imwrite('/home/arsen/Documents/programs/sobel/output/img1.jpg', img)
    #cv.imwrite('/home/arsen/Documents/programs/sobel/output/'+pict, img)

if __name__ == '__main__':
    go()