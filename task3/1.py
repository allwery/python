class Triangle:
    def __init__(self, id, height, base,):
        self.id = id
        self.height = height
        self. base = base

    def move(self, new_base, new_height):
        self.base = new_base
        self.height = new_height

class Quad:
    def __init__(self, id, side):
        self.id = id
        self.side = side

    def move(self, new_side):
        self.side = new_side

    @staticmethod
    def compare(t1, t2):
        s_t1 = (t1.base * t1.height)/2
        s_t2 = t2.side**2
        if s_t1 > s_t2:
            return f" у {t1.id} больше площадь"
        elif s_t1 < s_t2:
            return f" у {t2.id} Больше площадь"
        else:
            return "Площадь одинакова"

height = int(input("Введите высоту треугольника: "))
base = int(input("Введите основание треугольника: "))
side = int(input("Введите сторону квадрата: "))

triangle = Triangle("Triangle1", height, base)
quad = Quad("Quad1", side)

number = int(input("Введите номер операции: "))
if number == 1:
    quad.move(6)
elif number == 2:
    triangle.move(4,3)
else:
    print('Ошибка')

print(Quad.compare(triangle, quad))
