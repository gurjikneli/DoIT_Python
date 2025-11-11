# 1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. ასევე, შექმენით კლასის მეთოდი car_info(), რომელიც
# დაბეჭდავს ატრიბუტების ინფორმაციას.

from datetime import datetime

class Car:
    number_of_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def car_info(self):
        print("კლასის ატრიბუტებია: ", self.make, self.model, self.year)
        print("მანქანის ასაკი: ", self.age_of_car())

    def total_cars(self):
        return Car.number_of_cars

# 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს. ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.

    def age_of_car(self):
        date = datetime.today()
        year = date.year
        # month = date.month
        # day = date.day
        age = year - self.year
        return age

car = Car('Ford', 'Mustang', 2020)
car.car_info()

car2 = Car('Audi', 'R8', 2022)

# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი
# battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".
class ElectricCar(Car):
    def __init__(self, battery_life, make, model, year):
        super().__init__(make, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")

ecar = ElectricCar('50000', 'Toyota', 'Prius', 2015)
ecar.battery_info()

ecar2 = ElectricCar('100000', 'Lexus', 'GS450H', 2010)


# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ
# ჯერზე, მანქანის შექმნისას.

for _ in range(10):
    Car('Mercedes', 'E Class', 2010 + _)


# 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.
print("მანქანების მთლიანი რაოდენობაა:", car.total_cars())

print(Car.number_of_cars)
print(car2.total_cars())

