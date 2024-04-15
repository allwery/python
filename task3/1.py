class Triangle:
    def __init__(self, id, height, base,):
        if base <=0 or height <=0:
            raise ValueError ("Высота и основание должны быть больше нуля")
        self.id = id
        self.height = height
        self. base = base

    def move(self, new_base, new_height):
        if new_base <=0 or new_height <=0:
            raise ValueError ("Высота и основание должны быть больше нуля")
        self.base = new_base
        self.height = new_height

class Quad:
    def __init__(self, id, side):
        if side <=0:
            raise ValueError ("Основание должно быть больше нуля")
        self.id = id
        self.side = side

    def move(self, new_side):
        if new_side <= 0:
            raise ValueError("Сторона должна быть больше нуля")
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
try:
   height = int(input("Введите высоту треугольника: "))
   base = int(input("Введите основание треугольника: "))
   side = int(input("Введите сторону квадрата: "))

   triangle = Triangle("Triangle1", height, base)
   quad = Quad("Quad1", side)

   num_op = int(input("Введите номер операции: "))
   if num_op == 1:
       move_side = int(input("Введите сдвиг: "))
       quad.move(move_side)
   elif num_op == 2:
       move_base = int(input("Введите сдвиг по основанию: "))
       move_height = int(input("Введите сдвиг по высоте: "))
       triangle.move(move_base,move_height)
   else:
       print('Ошибка')

   print(Quad.compare(triangle, quad))

   inv_triangle = Triangle("InvailedTraingle", -2, 3)
   inv_quad = Quad("InvailedQuad", -2)
except ValueError as e:
    print("Ошибка",str(e))
