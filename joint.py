import cv2
import numpy as np

class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __str__(self):
      return str((self.x, self.y))

def get_shape(data1, data2, shape):
   maxi1 = 0
   maxi2 = 0
   for x in data1:
      if maxi1 < x[0]:
         maxi1 = x[0]
   for x in data2:
      if maxi2 < x[0]:
         maxi2 = x[0]
   k1 = abs(maxi1 - maxi2)
   shape[0] += k1

   maxi1 = 0
   maxi2 = 0
   for x in data1:
      if maxi1 < x[1]:
         maxi1 = x[1]
   for x in data2:
      if maxi2 < x[1]:
         maxi2 = x[1]

   k2 = abs(maxi1 - maxi2)
   shape[1] += k2

   blank_image = np.zeros(shape, np.uint8)
   return [blank_image, k1, k2]


def draw(A, C, img1, img2, blank_image):
   delta_x = A.x - C.x
   delta_y = A.y - C.y
   shape = img1.shape
   res = blank_image[:, :, :]
   if delta_x > 0:
      if delta_y > 0:
         res[:shape[0], :shape[1], :] = img1[:, :, :]
         res[abs(delta_x):, abs(delta_y):, :] = img2[:, :, :]
      else:
         res[:shape[0], abs(delta_y):, :] = img1[:, :, :]
         res[abs(delta_x):, :shape[1], :] = img2[:, :, :]
   else:
      if delta_y > 0:
         res[abs(delta_x):, :shape[1], :] = img1[:, :, :]
         res[:shape[0], abs(delta_y):, :] = img2[:, :, :]
      else:
         res[abs(delta_x):, abs(delta_y):, :] = img1[:, :, :]
         res[:shape[0], :shape[1], :] = img2[:, :, :]
   cv2.imwrite('/home/arsen/Documents/programs/diploma/panorama.jpg', res)



ar1 = []
ar2 = []
data1 = []
data2 = []

with open("panorama1.txt", "r") as file:
   for x in file:
       ar1.append([int(number) for number in x.split()])

with open("panorama2.txt", "r") as file:
   for x in file:
       ar2.append([int(number) for number in x.split()])
for x in ar1:
   if x not in data1:
      data1.append(x)

for x in ar2:
   if x not in data2:
      data2.append(x)

img1 = cv2.imread('res1.jpg')
img2 = cv2.imread('res2.jpg')
shape = list(img1.shape)

blank_image, l1, l2 = get_shape(data1, data2, shape)

A = Point(data1[0][0], data1[0][1])
C = Point(data2[0][0], data2[0][1])

draw(A, C, img1, img2, blank_image)