tickets = int(input("Введите нужное количество билетов: "))
age = int(input("Сколько вам лет? "))
if age <18:
    print("Проходит бесплатно")
elif (age >= 18 and age <= 24) and (tickets > 3):
    print("К оплате: ", int((990 - 990 * 10 / 100) * tickets), "Рублей")
elif age >= 18 and age <= 24:
    print("К оплате: ", tickets * 990, "Рублeй")
elif age > 24 and tickets > 3:
    print("К оплате: ", int((1390 - 1390 * 10 / 100) * tickets), "Рублeй")
else:
    print("К оплате: ", tickets * 1390, "Рублeй")

