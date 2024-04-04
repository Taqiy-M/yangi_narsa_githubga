# polimorfizm
# method overriding
# method overloading
# operator overloading


# def multi(a=None, b=None):
#     if b == None and a != None:
#         if a%2 == 0:
#             print(a, "juft son")
#         else:
#             print(a, "toq son")
#     elif a == b and a == None:
#         print("Funksiyaga parametr uzating!!")
#     else:
#         print("a*b=", a*b)
# multi(10, 20)
# multi()
# multi(300)


# class Person:
# def __init__(self, name, year, phone):
#     self.name = name
#     self.year = year
#     self.phone = phone
#
# def salom(self):
#     print(f"Assalomu alaykum! "
#           f"Men Odamman. "
#           f"Mening ismim {self.name}. Yoshim {2024 - self.year}")

class Car:
    def __init__(self, model, brand, price, weight, max_speed, year, color, cat):
        self.color = color
        self.year = year
        self.max_speed = max_speed
        self.weight = weight
        self.price = price
        self.brand = brand
        self.cat = cat
        self.model = model

    def __repr__(self):
        return self.model + " " + str(self.weight)

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __add__(self, other):
        return


a = Car("R8", "Audi", 60000, 800, 260, 2024, 'white', "sport")
b = Car("M5", "BMW", 160000, 100, 360, 2025, 'black', "sport")
c = Car("Y2", "GM", 91000, 1090, 360, 2025, 'black', "sport")
d = Car("Q5", "Chevrolet", 1900, 1200, 360, 2025, 'black', "sport")
e = Car("X7", "BMW", 100080, 11200, 360, 2025, 'black', "sport")
f = Car("A67", "BYD", 160, 12000, 360, 2025, 'black', "sport")
g = Car("S60", "Jetour", 16000, 100, 360, 2025, 'black', "sport")

l = [a, b, c, d, e, f, g]
l.sort()
print(l)






# > == greater than
# < == less than
# >=  === greater than or equal to
# <=  === less than or equal to
# ==  equal to
# !=  not equal to
# print(a > "900")
# a = Student("Ali", 2005, 9989999998888, "TATU")
# a.salom()



















