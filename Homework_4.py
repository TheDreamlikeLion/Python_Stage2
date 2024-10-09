# 1. Напишите функцию для транспонирования матрицы
# Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def matrix(list_: list[list]) -> list[list]:
    return list(map(list, zip(*list_)))
  
print(matrix([[3, 4, 5], [6, 7, 8]]))


# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def dict_from_args(**kwargs):
    equipments = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        equipments[v] = k
    return equipments


print(dict_from_args(desktop='DellOptiplex750', laptop={'DellLatitude1200': 3, 'DellLatitude1400': 2}, mobile=['SamsungET100', 'XiaomiM5s', 'RedmiNote10'], dect={'PanasonicEB1275', 'SamsungDR7025'}))
