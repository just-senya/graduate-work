import cv2

class Point:
	def __init__(self, p):
		self.x = p[0]
		self.y = p[1]
		self.area = [2]

	def __eq__(self, other):
		m1 = self.x - other.x
		m2 = self.y - other.y
		return m1 ** 2 + m2 ** 2 < 36

	def __str__(self):
		return str((self.x, self.y))



class Vector(Point):
	def __init__(self, p1, p2):
		self.vx = p1.x - p2.x
		self.vy = p1.y - p2.y
		self.area1 = p1.area
		self.area2 = p2.area

	def __add__(self, other):
		return Point((self.vx + other.x, self.vy + other.y, 0))


data1 = []
data2 = []

with open("data1.txt", "r") as file:
   for x in file:
       data1.append([int(number) for number in x.split()])

with open("data2.txt", "r") as file:
   for x in file:
       data2.append([int(number) for number in x.split()])


img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')

n1 = 1
n2 = 1

status = True

open('panorama1.txt', 'w')
open('panorama2.txt', 'w')

for x1 in data1[:]: # выбираем первую точку из первого изображения
	A = Point(x1)
	for x2 in data1[n1:]:# выбираем вторую точку из первого изображения
		B = Point(x2)
		vec11 = Vector(A, B) # создаем вектор AB
		vec12 = Vector(B, A) # создаем вектор BA
		for y1 in data2[:]:# выбираем первую точку из второго изображения
			C = Point(y1)
			test_point1 = vec11 + C
			test_point2 = vec12 + C
			for y2 in data2[n2:]:# выбираем вторую точку из второго изображения
				D = Point(y2)
				vec21 = Vector(C, D)
				if test_point1 == D:
					cv2.circle(img1, (A.x,A.y), 2, (0, 230, 240), 2)
					cv2.circle(img1, (B.x,B.y), 2, (0, 230, 240), 2)
					cv2.circle(img2, (C.x,C.y), 2, (0, 230, 240), 2)
					cv2.circle(img2, (D.x,D.y), 2, (0, 230, 240), 2)

					if status:
						status = False
						print(B.x, B.y, sep=' ', file=open('panorama1.txt', 'a'))
						print(C.x, C.y, sep=' ', file=open('panorama2.txt', 'a'))

				elif test_point2 == D:
					cv2.circle(img1, (A.x,A.y), 2, (0, 230, 240), 2)
					cv2.circle(img1, (B.x,B.y), 2, (0, 230, 240), 2)
					cv2.circle(img2, (C.x,C.y), 2, (0, 230, 240), 2)
					cv2.circle(img2, (D.x,D.y), 2, (0, 230, 240), 2)

					if status:
						status = False
						print(B.x, B.y, sep=' ', file=open('panorama1.txt', 'a'))
						print(C.x, C.y, sep=' ', file=open('panorama2.txt', 'a'))
			n2 += 1
		n2 = 1
	n1 += 1
cv2.imwrite('/home/arsen/Documents/programs/diploma/res1.jpg', img1)
cv2.imwrite('/home/arsen/Documents/programs/diploma/res2.jpg', img2)