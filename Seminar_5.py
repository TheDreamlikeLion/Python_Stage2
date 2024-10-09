# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

one, two, three, *other = input('Введите строку через / ').split('/')
my_dict = {int(two): int(one), int(three): map(int, other)}
print(my_dict)

text = '3/5/7/8/10/12/13'


def make_dict(text: str) -> dict[int:int]:
    first, second, third, *other = (int(i) for i in text.split('/'))
    return {second: first, third: tuple(other)}


# print(make_dict(text))


# Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

text = 'Создайте из строки словарь, где ключ — буква, а значение — код буквы.'
my_dict = {symbol: ord(symbol) for symbol in set(text)}
print(my_dict)


# Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.


COUNT = 5

text = 'Создайте из строки словарь, где ключ — буква, а значение — код буквы.'
my_dict = {symbol: ord(symbol) for symbol in set(text)}
my_dict_iter = iter(my_dict.items())

for _ in range(COUNT):
  print(next(my_dict_iter))
print(*my_dict_iter)


# Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

evens = (num for num in range(0, 100, 2) if (num % 10)+(num // 10) != 8)
print(*evens, sep='\n')


# Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.


fizzbuzz = []
for number in range(1, 101):
  if number % 15 == 0:
    fizzbuzz.append('FizzBuzz')
  elif number % 3 == 0:
    fizzbuzz.append('Fizz')
  elif number % 5 == 0:
    fizzbuzz.append('Buzz')
  else:
    fizzbuzz.append(number)

print(*fizzbuzz)

fizzbuzz_gen = ('FizzBuzz' if number % 15 == 0 else 'Fizz' if number % 3 == 0 else 'Buzz' if number % 5 == 0 else number for number in range(1, 101))
print(*fizzbuzz_gen)


# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.


LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4
ONE = 1

# for i_main in range(LOWER_LIMIT, LOWER_LIMIT + COLUMN):
#     for s_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE):
#         for f_num in range(i_main, i_main + COLUMN):
#             print(f'{f_num:>2} x {s_num:>2} = {f_num*s_num:>2}', end='\t')
#         print()
#     print()

table_generator = (f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\t' if f_num < i_main + COLUMN - ONE else
                   f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\n' if s_num < UPPER_LIMIT else
                   f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\n\n'
                   for i_main in (LOWER_LIMIT, LOWER_LIMIT + COLUMN)
                   for s_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE)
                   for f_num in range(i_main, i_main + COLUMN))

print(*table_generator)


# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def is_prime(num: int):
    if num % 2 == 0 and num != 2:
        return False
    for div in range(3, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True
  

def prime_generator(n: int):
    for number in range(2, n + 1):
        if is_prime(number):
            yield number

print(*prime_generator(80))
