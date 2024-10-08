from math import pi
import decimal


# Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные.

# a = 1
# b = 'строка'
# c = 0.3
# d = (1, 1)
# e = {1: 3}
# print(f'a - {type(a)}, b - {type(b)}, c - {type(c)}, d - {type(d)}, e - {type(e)} ')

# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты

# import sys
#
# data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1 'Привет, мир!']
#
# for nn, value in enumerate(data, 1):
#     check_int = 'Похоже на целое число' if isinstance(value, int) else ''
#     check_str = 'Похоже на строку' if isinstance(value, str) else ''
#     print(f'{nn]. Значение {value}.\nАдрес в памяти {id(value)}.\tРазмер в памяти {sys.getsizeof(value)}'
#           f'\tХэш объекта {hash(value)}.\t{check_int}{check_str}')


# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
#
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

# BIN = 2
# OCT = 8
#
# num = int(input('Введите целое число: '))
#
# fur div in (BIN, OCT):
#     result: str = ''
#     test_num: int = num
#     while test_num > 0:
#         result = str(test_num % div) + result
#         test_num //= div
#     print(f'For {div=} {result=}')
#
# print(f'Двоичное число {bin(num)}, восьмеричное число {oct(num)}')

# def task3(num: int, mode: str) -> str:
#     result = ''
#     convert: int = 2
#
#     match mode:
#         case "bin":
#             convert = 2
#         case "oct":
#             convert = 8
#
#     while num >= 1:
#         res = num % convert
#
#         result += str(res)
#         num = num // convert
#
#     return result[::-1]
#
#
# print(task3(21, mode="bin"), f"assert: {bin(21)}")
# print(task3(21, mode="oct"), f"assert: {oct(21)}")


# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
#
# ✔ Диаметр не превышает 1000 у.е.
#
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import math
# import decimal
# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)
#
# d = decimal.Decimal(input('Введите диаметр окружности: '))
# while d> 1000:
#     print('Некорректный ввод!')
#     d = decimal.Decimal(input('Введите диаметр окружности: '))
# print(f'Площадь круга = {PI * (d / 2) ** 2},\nДлина окружности = {PI * d}')


# def circle(d: decimal) -> tuple[decimal, decimal]:
#     decimal.getcontext().prec = 42
#     _pi = decimal.Decimal(pi)
#     if d <= 1000:
#         s = (_pi * d ** 2) / 4
#         l = _pi * d
#
#     return decimal.Decimal(s), decimal.Decimal(l)


# 5) Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

# a = float(input('Введите коэффициент a = '))
# b = float(input('Введите коэффициент b = '))
# c = float(input('Введите коэффициент c = '))
#
# d = b ** 2 -4 *a * c
# if d > 0:
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     result = f'У уравнения 2 корня: {x1=}, {x2=}'
# elif d == 0:
#     x = -b / (2 * a)
#     result = f'У уравнения 1 корень: {x=}'
# else d < 0:
#     d = complex(d, 0)
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     result = f'У уравнения 2 комплексных корня: x1 = {round(x1.real, 2)} + round(x1.imag, 2) * 1j}, '
#              f'x2 = {round(x2.real, 2) + round(x2.imag, 2) * 1j}')
# print(result)

# def quadratic_equation():
#     print('Решаем уравнение a•x²+b•x+c=0')
#     a = input('Введите значение a: ')
#     b = input('Введите значение b: ')
#     c = input('Введите значение c: ')
#     a = float(a)
#     b = float(b)
#     c = float(c)
#     discriminant = b ** 2 - 4 * a * c
#     print('Дискриминант = ' + str(discriminant))
#     if discriminant == 0:
#         x = -b / (2 * a)
#         print('x = ' + str(x))
#     else:
#         x1 = (-b + discriminant ** 0.5) / (2 * a)
#         x2 = (-b - discriminant ** 0.5) / (2 * a)
#         print('x₁ = ' + str(x1))
#         print('x₂ = ' + str(x2))
#
# quadratic_equation()

# 6) Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


class Bank:
    _BALANCE = 0
    _MIN = 50
    _MAX = 5000000
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION: int
    _OPERATIONS: list[str]

    def __init__(self):
        self._OPERATION = 0
        self._OPERATIONS = dict()

    def _in(self, cash: int, tax: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0:
            self._BALANCE += cash + tax
            self._OPERATION += 1
            self._OPERATIONS[f'+ {cash + tax}'] = 'Пополнение'
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _out(self, cash: int, commission: int, tax: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE - (cash + commission + tax) >= 0:
            self._BALANCE -= cash + commission + tax
            self._OPERATION += 1
            self._OPERATIONS[f'- {cash + commission + tax}'] = 'Снятие'
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _check_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION
        _MAX = 600
        _MIN = 30
        if sum_commission > _MAX:
            sum_commission = _MAX
        elif sum_commission < _MIN:
            sum_commission = _MIN
        else:
            sum_commission = int(sum_commission)
        return sum_commission

    def _check_tax(self, cash: int) -> int:
        if cash >=self._MAX:
            print(f'\nВнимание был снят налог на богатство в размере {cash * self._TAX}')
            return cash * self._TAX
        else:
            return 0

    def _exit(self):
        return "Всего доброго, приходите к нам еще"

    def add_bonus(self):
            self._BALANCE += self._BALANCE * self._BONUS
            return f'Поздравляем, вы получили бонус за каждую 3-юю операцию в нашем банке . ' \
                   f'На ваш счет было зачислено: {int(self._BALANCE * self._BONUS)}\n'

    def _show_operations(self) -> None:
        for summ, op in self._OPERATIONS.items():
            print(f'{summ} - {op}')

    def start(self, mode: str, cash: int = 0) -> str:
        if self._OPERATION % 3 == 0:
             print(self.add_bonus())
        tax = self._check_tax(cash)
        match mode:
            case "in":
                self._in(cash=cash, tax=tax)
                return f"Средства были зачислены сумма: {cash}, баланс: {int(self._BALANCE)}"
            case "out":
                commission = self._check_commission(cash=cash)
                data = self._out(cash=cash, commission=commission, tax=tax)
                if data:
                    return f"Операция осуществлена успешно, сумма: {cash}, коммисия: {commission}, " \
                           f"баланс: {int(self._BALANCE)}"
                else:
                    return "Нехватает средств"

            case "show":
                self._show_operations()

            case "exit":
                return self._exit()


bank = Bank()
print(bank.start(mode='in', cash=4000000))
print(bank.start(mode='in', cash=100000))
print(bank.start(mode='out', cash=100000))
print(bank.start(mode='in', cash=100000))
print(bank.start(mode='in', cash=1000000))
print(bank.start(mode='in', cash=2000000))
print(bank.start(mode='out', cash=5000000))
print(bank.start(mode='show'))
