def filterer(data: list, val: str) -> list:
    return [i for i in data if val in i]


def maper(data: list, val: str) -> list:
    return [i.split()[int(val)] for i in data]


def uniquer(data: list) -> list:
    return list(set(data))


def sorter(data: list, val: str) -> list:
    if val == 'asc':
        return sorted(data, reverse=False)
    if val == 'desc':
        return sorted(data, reverse=True)


def limiter(data: list, val: str) -> list:
    return [data[i] for i in range(int(val))]


def func_data(data: list, com: str, val: str) -> list:
    if com == 'filter':
        return filterer(data, val)
    elif com == 'map' and val.isdigit():
        return maper(data, val)
    elif com == 'unique' and val == '-':
        return uniquer(data)
    elif com == 'sort' and val in ['asc', 'desc']:
        return sorter(data, val)
    elif com == 'limit' and val.isdigit():
        return limiter(data, val)
    else:
        return []


def main():
    while True:
        with open('apache_logs.txt') as file:
            data = file.readlines()
        print('Выберите подходящую команду и необходимое значение: \nfilter - является “поиском” по файлу\nmap - этой '
              'командой мы '
              'изменяем формат исходных данных\nunique - оставляет только уникальные значения\nsort - сортирует данные в '
              'алфавитном порядке или в обратном алфавитном порядке\nlimit - выводит '
              'только необходимое количество строк из запроса')
        user_input = input("Введите команду: ")
        commands = user_input.split(' | ')
        for command in commands:
            com = command.split()
            if len(com) != 2:
                print('Некорректная команда\n')
                exit()
            data = func_data(data, com[0], com[1])
            if not data:
                print('Не верно введенная команда\n')
                exit()
        for line in data:
            print(line)


if __name__ == "__main__":
    main()
