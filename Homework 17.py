# 1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y. კლასში
# დაამატეთ __add__ მეთოდი, რომ მოახდინოთ ვექტორების დამატება და __str__ მეთოდი, რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)




# 2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს
# ორი წიგნის ტოლობას.
# ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False




# 3. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის
# გადაფარვა. Car კლასს დაუმატეთ  თითოეული ატრიბუტისთვის set და get თვისებები მათი ცვლილებებისთვის.
# დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის
# მთელი და ა.შ.

class Car:
    def __new__(cls, *args, **kwargs):
        print("Creating a new Car instance...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        print("Initializing Car instance...")
        super().__init__()
        # ვალიდაცია init-ის დონეზე
        self.brand = brand
        self.model = model
        self.year = year

    # brand ატრიბუტი
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Brand name cannot be empty.")
        self._brand = value

    # model ატრიბუტი
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Model name cannot be empty.")
        self._model = value

    # year ატრიბუტი
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer.")
        if value < 2000 or value > 2025:
            raise ValueError("Year must be between 2000 and 2025.")
        self._year = value

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


# --- გამოყენების მაგალითი ---
car1 = Car("Toyota", "Camry", 2020)
print(car1)


# ატრიბუტების შეცვლა
car1.brand = "Honda"
car1.year = 2024

print("\nმონაცემების განახლების შემდეგ:")
print(car1)



