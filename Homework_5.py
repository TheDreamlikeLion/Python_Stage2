# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


path_text = r"C:\\Users\\admin\\Downloads\\3867791.pdf"

def split_path(abs_path: str) -> tuple():
    list_abs_path = abs_path.split('\\')
    list_last_elem = list_abs_path[-1].split('.')
    path = '\\'.join(list_abs_path[0:-1])
    name = list_last_elem[0]
    extension = list_last_elem[1]
    return path, name, extension

print(*split_path(path_text))


# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ['Денис', 'Павел', 'Александр', 'Олег', 'Илья']
salary = [200000, 300000, 220000, 500000, 150000]
bonus = ['10.25%', '15.00%', '10.50%', '10.75%', '13.50%']

def bonus_generator(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in bonus))}.items()

print(*bonus_generator(names, salary, bonus))


# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(*(fib(20)))
