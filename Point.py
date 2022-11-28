import math

class Point:
    #инициализация
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #метод вывода координат
    def write(self):
        print("Координаты точки: " + str(self.x) + ", " + str(self.y))

    #метод расчета от точки до точки
    def get_dist(self,other_point):
        return math.dist((self.x,self.y),(other_point.x,other_point.y))

    def get_dist_to_center(self):
        x0=0
        y0=0
        return math.dist((self.x,self.y),(x0,y0))