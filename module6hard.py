from math import sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=True):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        self.new_color = (r, g, b)
        if self.is_valid_color(r, g, b):
            self.__color = self.new_color
        else:
            return self.__color
        return self.__color

    def __is_valid_sides(self, *new_sides):
        self.new_sides = list(new_sides)
        if self.sides_count == 1 and len(new_sides) == 1 and self.new_sides[0] > 0:
            return True
        elif self.sides_count == 3 and len(new_sides) == 3 and self.new_sides[0] > 0 and self.new_sides[1] > 0 and \
                self.new_sides[2] > 0:
            return True
        elif self.sides_count == 3 and len(new_sides) == 1 and self.new_sides[0] > 0:
            return True
        elif self.sides_count == 12 and len(new_sides) == 1 and self.new_sides[0] > 0:
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        if self.__is_valid_sides(*new_sides) and self.sides_count == 1:
            self.__sides = self.new_sides
            return self.__sides
        elif not self.__is_valid_sides(*new_sides) and self.sides_count == 1:
            self.__sides = [self.__sides]
            return self.__sides
        elif self.__is_valid_sides(*new_sides) and self.sides_count == 3:
            if len(self.new_sides) == 3:  # Triangle.sides_count:
                self.__sides = self.new_sides
                return self.__sides
            elif len(self.new_sides) == 1:
                sides = [self.new_sides[0]]
                self.__sides = sides * 3
                return self.__sides
        elif not self.__is_valid_sides(*new_sides) and self.sides_count == 3:
            self.__sides = [self.__sides] * 3
            return self.__sides
        elif self.__is_valid_sides(*new_sides) and self.sides_count == 12:
            sides = [self.new_sides[0]]
            self.__sides = sides * 12
            return self.__sides
        elif not self.__is_valid_sides(*new_sides) and self.sides_count == 12:
            sides = [self.__sides]
            self.__sides = sides * 12
            return self.__sides

    def get_sides(self):
        return self.__sides  # enlist = list(self.__sides)

    def __len__(self):
        # self.get_sides()
        if self.sides_count == 1:
            return self.__sides[0]
        elif self.sides_count == 3:
            return self.__sides[0] + self.__sides[1] + self.__sides[2]
        elif self.sides_count == 12:
            return self.__sides[0] * 12


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.per = super().get_sides()
        self.__radius = self.per / 3.14 / 2

    def get_square(self):
        self.square = self.per ** 2 / 4 / 3.14
        return self.square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        self.sides = super().get_sides()
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.side = [super().get_sides()]
        self.__sides = self.side * 12

    def get_volume(self):
        # self.side = super().get_sides()
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# # Проверка на изменение сторон:
# cube1.set_sides(5)  # Не изменится
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# tr = Triangle((222, 35, 130), 4)
# tr.set_sides(2, 3, 4)
# print(tr.get_sides())
# print(len(tr))
# print(tr.get_square())
# print(len(cube1))
#
# tr = Triangle((222, 35, 130), 6)
# tr.set_sides(2, 3, 4)
# print(tr.get_sides())

#
# tr = Triangle((222, 35, 130), 8)
# tr.set_sides(2, -3, 4)
# print(tr.get_sides())
# print(tr.get_square())
#
# tr = Triangle((222, 35, 130), 7)
# tr.set_sides(2)
# print(tr.get_sides())

#
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
# print(circle1.get_square())#
# # Проверка объёма (куба):
print(cube1.get_volume())