from datetime import date


# 1_____________________________________________

class Parallelogram:
    def __init__(self, side_a, side_b, height_a, height_b):
        self.side_a = side_a
        self.side_b = side_b
        self.height_a = height_a
        self.height_b = height_b

    def perimeter(self):
        return (self.side_a+self.side_b)*2

    def square(self):
        return self.side_a*self.height_a


figure = Parallelogram(2, 3, 6, 4)

perimeter_figure = figure.perimeter()
square_figure = figure.square()

print(perimeter_figure, square_figure)

# 2______________________________________________________


class Human:
    def __init__(self, name, city, year_of_birth):
        self.name = name
        self.city = city
        self.year_of_birth = year_of_birth

    def age(self):
        return date.today().year - self.year_of_birth


person = Human("andrew", "ufa", 1991)
print(f"{person.age()} года")

# 3___________________________________________________________________


class Calculator:

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def difference(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a/b if b != 0 else "На 0 делить нельзя"


print("Сумма:", Calculator.sum(1,2), "Разность:", Calculator.difference(2, 3),
      "Умножение:", Calculator.multiplication(4,5), "Деление:", Calculator.division(5, 0))

# 4____________________________________________________________


class Human:
    def __init__(self, name, surname, lastname):
        self.name = name
        self.surname = surname
        self.lastname = lastname

    def __str__(self):
        return f"{self.surname} {self.name} {self.lastname}"


person = Human("Андрей", "Бардуков", "Александрович")
print(person)

# 5______________________________________________


class Employee:
    def get_paid(self):
        pass


class Manager(Employee):
    def get_paid(self):
        return 35000


class Worker(Employee):
    def get_paid(self):
        return 30000


# 6__________________________________________________________

class Furniture:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def deliver_furniture(self, address):
        return f"Мебель {self.name} доставлена на адрес {address}"


class SitDownMixin:
    def sit_down(self):
        return f"Вы сели на {self.name}"


class LieDownMixin:
    def lie_down(self):
        return f"Вы легли на {self.name}"


class Chair(Furniture, SitDownMixin):
    pass


class Bed(Furniture, LieDownMixin):
    pass

chair_andrew = Chair("Стул-конструктор", 5, 6)
print(chair_andrew.sit_down())

bed_andrew = Bed("Кровать-книжка", 16, 10)
print(bed_andrew.lie_down())
