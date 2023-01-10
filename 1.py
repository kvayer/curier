import math


class Point:
    # инициализация
    def __init__(self, x, y):
        self.x = x
        self.y = y
        coords = x, y

    # метод вывода координат
    def get_coords(self):
        return f'{self.x},{self.y}'

    # метод расчета от точки до точки
    def get_dist(self, other_point):
        return math.dist((self.x, self.y), (other_point.x, other_point.y))

    def get_dist_to_center(self):
        x0 = 0
        y0 = 0
        return math.dist((self.x, self.y), (x0, y0))


class Order:

    def __init__(self, x, y, weight, price):
        self.point = Point(x, y)
        self.weight = weight
        weight = weight
        self.price = price

    def order_coords(self):
        return self.point.get_coords()


class Courier:
    def __init__(self, x, y, capacity=10):
        self.point = Point(x, y)
        self.history = []
        self.capacity = capacity
        capacity = capacity

    def courier_coords(self):
        return self.point.get_coords


class World:
    def distribution(self, orders, couriers):
        closest_order = {}
        dist = 1
        for c_key in couriers:
            min_dist = 1000000000000000
            for o_key in orders:
                coords = orders[o_key].point
                if couriers[c_key].capacity <= orders[o_key].weight:
                    dist = (orders[o_key].point).get_dist_to_center() + (couriers[c_key].point).get_dist(orders[o_key].point)
                if dist < min_dist:
                    min_dist = dist
                    coords = orders[o_key].point
                    order = o_key
            del orders[order]
            closest_order[c_key] = order
        return closest_order

plan = {}

orders = {
    'A': Order(4, 0, 5, 500),
    'B': Order(6, 0, 5, 500),
    'C': Order(3, 0, 10, 1000),
    'D': Order(11,0,5,5000)
}
couriers = {
    'Курьер 1': Courier(5, 0, 15),
    'Курьер 2': Courier(10,0,5)
}
closest_order = World().distribution(orders, couriers)
print(closest_order)
closest_order = World().distribution(orders, couriers)
print(closest_order)
# while len(orders)>0:
#     closest_order = World().distribution(orders, couriers)
#     for key, val in closest_order.items():
#         print(key,"delivered order",val)