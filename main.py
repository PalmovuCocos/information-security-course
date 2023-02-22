from math import ceil


def input_file():
    pass


def simple_permutation(s='ЗАСЕДАНИЕ СОСТОИТСЯ ЗАВТРА ЮСТАС', key_w='КОРЕНЬ'):
    """
    Функция выполняет шифорвание простой перестановки
    Отображает этаы зашифровки и возвращает зашифрованную таблицу
    :param s: строка, которую необходимо зашифровать
    :param key_w: ключ с помощью которого будет проходить зашифровка
    :return: Таблица с зашифрованным словом
    """

    s = s.replace(' ', '')  # удаление пробелов из текста
    key = [(key_w[i], i) for i in range(len(key_w))]  # добавление позиций для букв ключа
    n = ceil(len(s) / len(key))     # сколько можно раз поделить сообщение на длинну ключа
    table = [[] for _ in range(n)]  # создание пустой таблицы

    for i in range(len(key)):   # Заполнение таблицы
        for j in range(n):
            k = j + i * n   # расчет позиции буквы в строке, для её добавления в таблицу
            # если вышли за рамки таблицы, то ставим пробел
            table[j].append(s[k]) if k < len(s) else table[j].append('')

    for i in table:     # вывод таблицы
        print(i)
    s_key = sorted(key, key=lambda x: x[0])

    print(s_key)
    new_table = [[] for _ in range(len(table))]
    for i in range(len(key)):
        for j in range(len(new_table)):
            new_table[j].append(table[j][s_key[i][1]])

    return new_table


if __name__ == '__main__':
    input_file = input("Введите имя входного файла: ")
    output_file = input("Введите имя результирующего файла: ")
    table = simple_permutation()
    for el in range(len(table)):
        print(*table[el])


