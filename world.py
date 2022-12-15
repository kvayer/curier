import math


class Point:
    #инициализация
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #метод вывода координат
    def get_coords(self):
        return f'{self.x},{self.y}'

    #метод расчета от точки до точки
    def get_dist(self,other_point):
        return math.dist((self.x,self.y),(other_point.x,other_point.y))

    def get_dist_to_center(self):
        x0 = 0
        y0 = 0
        return math.dist((self.x,self.y),(x0,y0))


class Order:

    def __init__(self,number,x,y,weight,price):
        self.number = number
        self.point = Point(x,y)
        self.weight = weight
        self.price = price

    def order_coords(self):
        return self.point.get_coords()


class Courier:

    def __init__(self, name: str,x,y, capacity=10):
        self.name = name
        self.point = Point(x,y)
        self.history = []
        self.capacity = capacity

    def cpurier_coords(self):
        return self.point.get_coords

# class Record:
#     def __init__(self,name:str,from_point: Point,to_point: Point,time_start,time_finish):
#         self.courier_name = name
#         self.from_point = from_point
#         self.to_point = to_point
#         self.orders = []
#         self.time_start = time_start
#         self.time_finish = time_finish
#     def move(self,time_start,time_finish,from_point,to_point):
#         if self.history:
#             rec = last_start +

plan = {}

orders ={
    0: Order('A',4,7,0,500),
    1: Order('B',4,8,5,500),
    2: Order('C',4,0,10,1000)
}
couriers ={
    0: Courier('Курьер 1',5,0,15),
    1: Courier('Курьер 2',10,10,5)
}
print(orders[0].order_coords())