import math
import cv2


def distance(A, B):
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.edge1 = distance((p1[0], p1[1]), (p2[0], p2[1]))
        self.edge2 = distance((p1[0], p1[1]), (p3[0], p3[1]))
        self.edge3 = distance((p2[0], p2[1]), (p3[0], p3[1]))

        self.area1 = p1[2]
        self.area2 = p2[2]
        self.area3 = p3[2]

        sum = self.area1 + self.area2 + self.area3

        self.area1 = max(self.area1, self.area2, self.area3)
        self.area3 = min(self.area1, self.area2, self.area3)
        self.area2 = sum - self.area1 - self.area3

        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]
        self.x3 = p3[0]
        self.y3 = p3[1]

        sum = self.edge1 + self.edge2 + self.edge3
        self.edge1 = max(self.edge1, self.edge2, self.edge3)
        self.edge3 = min(self.edge1, self.edge2, self.edge3)
        self.edge2 = sum - self.edge1 - self.edge3

    def __eq__(self, other):
        if (abs(self.edge1 - other.edge1) > 30
                or abs(self.edge2 - other.edge2) > 30
                or abs(self.edge3 - other.edge3) > 30):
            return False

        # if (abs(self.area1 - other.area1) > 300
        #         or abs(self.area2 - other.area2) > 300
        #         or abs(self.area3 - other.area3) > 300):
        #     return False
        return True

    def __str__(self):
        return str([self.x1, self.y1, self.x2, self.y2, self.x3, self.y3])


if __name__ == '__main__':
    data1 = []
    data2 = []

    with open("data1.txt", "r") as file:
        for x in file:
            data1.append([int(number) for number in x.split()])

    with open("data2.txt", "r") as file:
        for x in file:
            data2.append([int(number) for number in x.split()])

    n1 = 1
    n2 = 2
    m1 = 1
    m2 = 2

    img1 = cv2.imread('img1.jpg')
    img2 = cv2.imread('img2.jpg')

    for x1 in data1[:]:
        for x2 in data1[n1:]:
            for x3 in data1[n2:]:
                for y1 in data2[:]:
                    for y2 in data2[m1:]:
                        for y3 in data2[m2:]:
                            A = Triangle(x1, x2, x3)
                            B = Triangle(y1, y2, y3)
                            if A == B:
                                # print("Yes")
                                # print(A)
                                # print(B)
                                cv2.circle(img1, (A.x1, A.y1), 3, (255, 0, 255), 2)
                                cv2.circle(img1, (A.x2, A.y2), 3, (255, 0, 255), 2)
                                cv2.circle(img1, (A.x3, A.y3), 3, (255, 0, 255), 2)
                                cv2.circle(img2, (B.x1, B.y1), 3, (255, 0, 255), 2)
                                cv2.circle(img2, (B.x2, B.y2), 3, (255, 0, 255), 2)
                                cv2.circle(img2, (B.x3, B.y3), 3, (255, 0, 255), 2)
                                cv2.imwrite('/home/arsen/Documents/programs/diploma/img1.jpg', img1)
                                cv2.imwrite('/home/arsen/Documents/programs/diploma/img2.jpg', img2)
                        m2 += 1
                    m1 += 1
            n2 += 1
        n1 += 1
