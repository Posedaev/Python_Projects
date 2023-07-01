class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def __str__(self):
        return f"{self.x}, {self.y}, {self.width}, {self.heigth}"

    def get_area(self):
        return self.width * self.heigth

pramoygolnik_1 = Rectangle(5, 10, 50, 100)
print(pramoygolnik_1.get_area())


#21.9.3
class Client:
    def __init__(self, firstname, lastname, city, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def get_info(self):
        return f'''{self.firstname} {self.lastname}.{self.city}. Баланс: {self.balance}руб.'''

    def guest_lst(self):
        return f'''{self.firstname} {self.lastname} {self.city}'''

client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Сидоров", "Иван", "Орел", 100)

list_of_guest = [client_1, client_2]
for i in list_of_guest:
    print(i.guest_lst())












