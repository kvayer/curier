import time
k=0
while k!=100:
    if k>=90 and k!=99:
        print('Создание курьера:',k,"%")
        time.sleep(1)
        k+=1
    elif k == 99:
        print("Ошибка при создании курьера.\nКурьер сдох.\nПопробуйте нанять нового...")
        break
    else:
        print('Создание курьера:', k, "%")
        time.sleep(1)
        k += 10