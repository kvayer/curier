from random import randint
from Point import Point


# Автоматическое создание словаря с координатами
def get_random_dict():
    count = randint(1, 10)
    random_dict = {}
    for index in range(count):
        x = randint(0, 10)
        y = randint(0, 10)
        point = Point(x, y)
        random_dict[index] = point
    return random_dict


# Функция расчета минимального расстояния от заказа до курьера
def get_closest_couriers_dict(orders_dict, couriers_dict):
    closest_couriers_dict = {}
    for o_keys, o_val in orders_dict.items():
        min_dist = orders_dict[o_keys].get_dist(couriers_dict[0]) + couriers_dict[0].get_dist_to_center()
        courier = 0
        for c_keys, c_val in couriers_dict.items():
            dist = orders_dict[o_keys].get_dist(couriers_dict[c_keys]) + couriers_dict[c_keys].get_dist_to_center()
            if dist < min_dist:
                min_dist = dist
                courier = c_keys
        closest_couriers_dict[o_keys] = courier
    return closest_couriers_dict


# Удаление заказа из словаря, присваивание курьеру точки (0,0). Вывод того, кто какой заказ доставил.
def to_deliver(delivering_order, closest_courier, orders, couriers):
    orders.pop(delivering_order)
    couriers[closest_courier] = Point(0, 0)
    print("Заказ №" + str(delivering_order) + " был доставлен курьером №" + str(closest_courier))
    return orders, couriers



orders = {0:Point(0,4),1:Point(0,6),2:Point(0,5)}
couriers = {0:Point(0,5)}

while len(orders) > 0:
    closest_couriers = get_closest_couriers_dict(orders, couriers)
    curier = list(closest_couriers.keys())
    orders, couriers = to_deliver(curier[0], closest_couriers[curier[0]], orders, couriers)
