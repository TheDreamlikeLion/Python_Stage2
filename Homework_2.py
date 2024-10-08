import fractions

# Решить задачи, которые не успели решить на семинаре.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_number(num: int, mode: str) -> str:
    result = ''
    convert: int = 2
    match mode:
        case "bin":
            convert = 2
        case "oct":
            convert = 8
        case "hex":
            convert = 16
    while num >= 1:
        res = num % convert
        if convert == 16:
            if res == 10:
                res = 'A'
            if res == 11:
                res = 'B'
            if res == 12:
                res = 'C'
            if res == 13:
                res = 'D'
            if res == 14:
                res = 'E'
            if res == 15:
                res = 'F'
        result += str(res)
        num = num // convert
    return result[::-1]

user_num = 31

print(convert_number(user_num, mode="bin"))
print(convert_number(user_num, mode="oct"))
print(convert_number(user_num, mode="hex"))
print('Проверка с помощью функции hex:')
print(hex(user_num))




# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


a = input("Введите первую дробь в формате x/x: ").split("/")
b = input("Введите вторую дробь в формате x/x: ").split("/")

mult_of_fractions = f'{int(a[0]) * int(b[0])}/{int(a[1]) * int(b[1])}'

common_divider = int(a[1]) * int(b[1])
sum_of_fractions = f'{str(int(a[0]) * common_divider // int(a[1]) + int(b[0]) * common_divider // int(b[1]))}/{str(common_divider)}'

print(f'Сложение дробей: {sum_of_fractions}\nПроизведение дробей: {mult_of_fractions} .')
print(f'\nПроверка с помощью модуля "fractions": ')
f1 = fractions.Fraction(int(a[0]), int(a[1]))
f2 = fractions.Fraction(int(b[0]), int(b[1]))
print(f'{f1} + {f2} = {f1 + f2}')
print(f'{f1} * {f2} = {f1 * f2}')
