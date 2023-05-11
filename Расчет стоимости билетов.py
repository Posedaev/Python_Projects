tickets_sum = 0
tickets = int(input("Введите нужное количество билетов: "))
for age in range(tickets):
    age = int(input("Сколько вам лет? "))
    if age < 18:
        print("Проходит бесплатно")
    elif (age >= 18 and age <= 24) and (tickets <=3):
        print("К оплате: ", 990, "Рублeй")
        tickets_sum = tickets_sum +990
    elif tickets >3 and age < 24:
        print("К оплате: ", int(990 - 990 * 10 / 100), "Рублeй")
        tickets_sum = tickets_sum +891
    elif age > 24 and (tickets <=3):
        print("К оплате: ", 1390, "Рублeй")
        tickets_sum = tickets_sum +1390
    elif tickets >3:
        print("К оплате: ", int(1390 - 1390 * 10 / 100), "Рублeй")
        tickets_sum = tickets_sum +1251
print("----------------------------->")
print ("Всего билетов", tickets, "на сумму", tickets_sum)
