from random import randint
from Point import Point

# Метод создания и записи рандомных координат в файл
def get_random_dict(dict):
    count = randint(1,10)
    for index in range(count):
        x = randint(0,10)
        y = randint(0,10)
        point = Point(x,y)
        dict.write(str(x))
        dict.write(str(','))
        dict.write(str(y))
        dict.write(str('\n'))

# Открываем файл с заказами, записываем координаты и закрывает
orders = open('orders.txt', 'w')
get_random_dict(orders)
orders.close()

# Открываем файл с курьерами, записываем координаты и закрывает
couriers = open('couriers.txt', 'w')
get_random_dict(couriers)
couriers.close()

# Метод считывания координат из файла
def save_to_dict(file):
    array = []
    k=0
    dict = {}
    for index in file:
        line = index.split(',')
        line[1]=line[1][:1]
        array.append(line)
        k+=1
    for i in range(k):
        dict[i] = Point(int(array[i][0]),int(array[i][1]))
    return dict

# Создания словарей с координатами
orders = {0:Point(3,1),1:Point(2,4)}
curiers = {0:Point(3,10),1:Point(4,7)}

# Словарь вида: Курьер(ключ):Заказ(значение)
def get_min_dist(curiers,orders):
    min_dict_distance = {}

    for c_key,c_val in curiers.items():
        min_dist = curiers[c_key].get_dist(orders[0]) + orders[0].get_dist_to_center()
        order = 0
        for o_key,o_val in orders.items():
            if curiers[c_key] == orders[o_key]:
                dist = orders[o_key].get_dist_to_center()
            else:
                dist = curiers[c_key].get_dist(orders[o_key]) + orders[o_key].get_dist_to_center()
            if dist < min_dist:
                min_dist = dist
                order = o_key
        min_dict_distance[c_key] = order,min_dist
    return min_dict_distance

def indificate_minimum(min_dict_distance):
    min = min_dict_distance[0][1]
    for c_key,c_val in min_dict_distance.items():
        if min_dict_distance[c_key][1]<min:
            min = min_dict_distance[c_key][1]
            to_deliver()


# Метод поиска ближайшего курьера к заказу


# Метод доставки заказа


