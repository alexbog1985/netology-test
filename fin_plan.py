# Напишите свой код здесь
class FinPlan:
    def __init__(self, salary, percent_mortgage, percent_life):
        self.salary = salary
        self.percent_mortgage = percent_mortgage
        self.percent_life = percent_life
        self.mortgage = 12 * (self.salary / 100 * self.percent_mortgage)
        self.life = 12 * (self.salary / 100 * self.percent_life)
        self.fin_plan = 12 * self.salary - self.mortgage - self.life


if __name__ == "__main__":
    # Задайте первоначальные значения

    int_salary = 100000  # Заработная плата
    int_percent_mortgage = 30  # Ипотека
    int_percent_life = 50  # На жизнь

    fp = FinPlan(int_salary, int_percent_mortgage, int_percent_life)
    print('Ипотека:', fp.mortgage)
    print('Накопления:', fp.fin_plan)
