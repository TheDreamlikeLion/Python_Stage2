import random as rd


def print_desk(position: list[list[int]]) -> None:
    DESKSIZE=8
    EMPTY = 0
    BUSY = 1
    desk = [[EMPTY for _ in range(DESKSIZE)] for _ in range(DESKSIZE)]
    for i in range(len(position)):
        desk[position[i][0]-1][position[i][1]-1] = BUSY
    print(*desk, sep='\n')
    print()


def check_queens_position(matrix: list[list[int]]) -> bool:
    MAX_NUMBER = 8
    crosspoints = []

    for (x, y) in [map(list, zip(*matrix))]:
        if len(set(y)) == len(set(x)) == MAX_NUMBER:#Проверяем вертикаль и горизонтали: если координаты любого из ферзей совпадут, то равенство нарушится.
            for i in range(MAX_NUMBER):
                for j in range(i + 1, MAX_NUMBER):
                    crosspoints.extend([abs(y[i] - y[j]) == abs(x[i] - x[j])])#Проверяем диагонали: если ферзи находятся на одной диагонали, то совпадет их относительное смещение по координатам.
    return False if any(crosspoints) or len(crosspoints) < 1 else True


def generate_queens_coordinates(max_number: int) -> map:
    x = [x for x in range(1, max_number + 1)]
    y = [x for x in range(1, max_number + 1)]
    rd.shuffle(x)
    rd.shuffle(y)
    return map(list, zip(x, y))


def show_success_positions(true_count: int) -> None:
    QUEEN_NUMBER = 8
    try_count = 0
    
    while true_count > 0:
        queens_position = [*generate_queens_coordinates(QUEEN_NUMBER)]
        result = check_queens_position(queens_position)
        if result:
            print(result, " :")
            print_desk(queens_position)
            true_count -= 1
        try_count += 1
    print(f'\nВсего было обработано комбинаций: {try_count}.\n')


if __name__ == "__main__":
    show_success_positions(4)