tickets = int(input("Введите нужное количество билетов: "))
for age in range(tickets):
    age = int(input("Сколько вам лет? "))
    if age < 18:
        print("Проходит бесплатно")
    elif (age >= 18 and age <= 24) and (tickets <=3):
        print("К оплате: ", 990, "Рублeй")
    elif tickets >3 and age < 24:
        print("К оплате: ", int(990 - 990 * 10 / 100), "Рублeй")
    elif age > 24 and (tickets <=3):
        print("К оплате: ", 1390, "Рублeй")
    elif tickets >3:
        print("К оплате: ", int(1390 - 1390 * 10 / 100), "Рублeй")
