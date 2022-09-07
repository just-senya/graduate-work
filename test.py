import cv2
import sys
import numpy as np

if __name__ == '__main__':
    hsv_min = np.array((95, 20, 5), np.uint8)
    hsv_max = np.array((187, 251, 253), np.uint8)

    hsv_min2 = np.array((0, 20, 5), np.uint8)
    hsv_max2 = np.array((30, 200, 150), np.uint8)

    color_blue = (255,0,0)
    color_yellow = (0,255,255)

    img = cv2.imread("input/four.png")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv2.inRange(hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    M = cv2.moments(cnt)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    print(cx)