class Square:
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        perimeter = self.a * 4  # Расчёт периметра
        return perimeter

    def get_area(self):
        area = self.a ** 2  # Расчёт площади
        return area


if __name__ == '__main__':
    s1 = Square(6)
    print(f'Периметр: {s1.get_perimeter()}')
    print(f'Площадь: {s1.get_area()}')
