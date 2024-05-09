def rectangle(a, b):
    perimeter = (a + b) * 2  # Расчёт периметра
    area = a * b  # Расчёт площади
    return {'Периметр': perimeter, 'Площадь': area}


if __name__ == '__main__':
    print(rectangle(5, 7))
