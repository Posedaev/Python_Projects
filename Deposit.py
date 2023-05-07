per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита: "))
#Возвращаем значение по ключу при помощи методе get
bank_1 = per_cent.get("ТКБ")
TKB = bank_1*money/100
bank_2 = per_cent.get("СКБ")
SKB = bank_2*money/100
bank_3 = per_cent.get("ВТБ")
VTB = bank_3*money/100
bank_4 = per_cent.get("СБЕР")
SBER = bank_4*money/100
print("Накопленные средства за год вклада в каждом из банков", TKB, SKB, VTB, SBER)
#Расчитываем максимальную сумму депозита которую можем заработать за год
deposit = [TKB, SKB, VTB, SBER]
print("Максимальная сумма, которую вы можете заработать: ", max(deposit))




    
