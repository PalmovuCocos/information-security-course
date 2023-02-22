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

    for i in range(len(key)-1):         # пузырькова сортировка ключа (по алфавиту) и таблицы
        for j in range(len(key)-2, i-1, -1):
            if key[j+1][0] < key[j][0]:
                key[j], key[j+1] = key[j+1], key[j]     # сортируется ключ
                for k in range(len(table)):
                    table[k][j], table[k][j+1] = table[k][j+1], table[k][j]     # сортируется таблица
    print(key)
    return table


if __name__ == '__main__':
    input_file = input("Введите имя входного файла: ")
    output_file = input("Введите имя результирующего файла: ")
    table = simple_permutation()
    for el in range(len(table)):
        print(*table[el])


