def filterer(data: list, val: str) -> list:
    return [i for i in data if val in i]


def maper(data: list, val: str) -> list:
    return [i.split()[int(val)] for i in data]


def uniquer(data: list) -> list:
    return list(set(data))


def sorter(data: list, value: str) -> list:
    if value == 1:
        return sorted(data, reverse=False)
    if value == 2:
        return sorted(data, reverse=True)


def limiter(data: list, val: str) -> list:
    return [data[i] for i in range(int(val))]


def func_data(data: list, com: int, val: str) -> list:
    if com == 1:
        return filterer(data, val)
    elif com == 2 and val.isdigit():
        return maper(data, val)
    elif com == 3 and val == '-':
        return uniquer(data)
    elif com == 4 and val == 1:
        return sorter(data, val)
    elif com == 4 and val == 2:
        return sorter(data, val)
    elif com == 5 and val.isdigit():
        return limiter(data, val)
    else:
        return []


def main():
    while True:
        with open('apache_logs.txt') as file:
            data = file.readlines()
        print('Выберите подходящую команду: \n1. filter - является “поиском” по файлу\n2. map - этой командой мы изменяем формат исходных данных\n3. unique - оставляет только уникальные значения\n4. sort - сортирует данные в '
              'алфавитном порядке или в обратном алфавитном порядке\n5. limit - выводит '
              'только необходимое количество строк из запроса')
        user_input = input("Введите команду: ")
        com = int(user_input)
        if com == 1:
            val = input('Ведите строку, по которой нужно будет фильтровать данные: ')
            data = func_data(data, com, val)
        elif com == 2:
            val = input('Выберите нужную колонку данных: ')
            data = func_data(data, com, val)
        elif com == 3:
            val = '-'
            data = func_data(data, com, val)
        elif com == 4:
            val = input('Введите 1, если хотите вывести запрос в алфавитном порядке\nВведите 2, если хотите вывести '
                        'запрос в обратном алфавитном порядке\nВвод: ')
            if val == 1 or val == 2:
                data = func_data(data, com, val)
            else:
                print('Нужно было ввести 1 или 2\nПовторите запрос сначала.')
        elif com == 5:
            val = input('Введите необходимое количество строк запроса: ')
            data = func_data(data, com, val)
        else:
            print('Не верно введенная команда\n')
            exit()
        if not data:
            print('Не верно введенная команда\n')
            exit()
        for line in data:
            print(line)


if __name__ == "__main__":
    main()