from math import ceil


def input_file(f_input):
    """
    Функция открывающая переданный файл на чтение и записывающая в переменую s данные из файла. Возвращает s.
    :param f_input: имя файла для открытия
    :return: s данные с файла
    """
    try:
        with open(f_input, encoding="utf-8") as file:
            s = file.readline()
            return s
    except FileNotFoundError:
        print("Невозможно открыть файл")
    except:
        print("Ошибка при работе с файлом")


def output_file(o_input, answer):
    """
    Функция открывающая переданный файл на запись и записывающая в файл s данные из результата работы программы.
     Возвращает s.
    :param o_input: имя файла для данных результата работы программы
    :param answer: результат работы программы
    """
    try:
        with open(o_input, "w+", encoding="utf-8") as file:
            file.write(answer)
            print("Данные записаны в файл")
    except FileNotFoundError:
        print("Невозможно открыть файл")
    except:
        print("Ошибка при работе с файлом")


def simple_permutation(s, key_w):
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
    print("\nВывод ключа до сортировки: ", *[i for i in key])
    for i in range(len(key)):   # Заполнение таблицы
        for j in range(n):
            k = j + i * n   # расчет позиции буквы в строке, для её добавления в таблицу
            # если вышли за рамки таблицы, то ставим пробел
            table[j].append(s[k]) if k < len(s) else table[j].append('')
    print('Таблица до перестановки')
    for i in table:     # вывод таблицы
        print(*i)

    for i in range(len(key)-1):         # пузырькова сортировка ключа (по алфавиту) и таблицы
        for j in range(len(key)-2, i-1, -1):
            if key[j+1][0] < key[j][0]:
                key[j], key[j+1] = key[j+1], key[j]     # сортируется ключ
                for k in range(len(table)):
                    table[k][j], table[k][j+1] = table[k][j+1], table[k][j]     # сортируется таблица
    print("\nВывод ключа после сортировки: ", *[i for i in key])
    print('Таблица после перестановки')
    for i in table:
        print(*i)
    return ''.join([t[i] for i in range(len(table[0])) for t in table])


def decoding(s, key):
    """
    Функция для декордирования сообщений зашифрованных простой перестановкой
    :param s: зашифрованная строка
    :param key: ключ
    :return: расшифрованное сообщение
    """
    key = [(key[i], i) for i in range(len(key))]  # добавление позиций для букв ключа
    n = ceil(len(s) / len(key))  # сколько можно раз поделить сообщение на длинну ключа
    table = [[] for _ in range(n)]  # создание пустой таблицы
    for i in range(len(key)):  # Заполнение таблицы
        for j in range(n):
            k = j + i * n  # расчет позиции буквы в строке, для её добавления в таблицу
            # если вышли за рамки таблицы, то ставим пробел
            table[j].append(s[k]) if k < len(s) else table[j].append('')
    key = list(sorted(key, key=lambda x: x[0]))
    print("\nВывод ключа до сортировки по алфавиту: ", *[i for i in key])
    print("Вывод таблицы до перестановки: ")
    for i in table:  # вывод таблицы
        print(*i)

    for i in range(len(key) - 1):  # пузырькова сортировка ключа (по позиции буквы) и таблицы
        for j in range(len(key) - 2, i - 1, -1):
            if key[j + 1][1] < key[j][1]:
                key[j], key[j + 1] = key[j + 1], key[j]  # сортируется ключ
                for k in range(len(table)):
                    table[k][j], table[k][j + 1] = table[k][j + 1], table[k][j]  # сортируется таблица
    print("\nВывод ключа после сортировки: ", *[i for i in key])
    print('Таблица после перестановки')
    for i in table:
        print(*i)
    return ''.join([t[i] for i in range(len(table[0])) for t in table])


if __name__ == '__main__':
    input_f = input("Введите имя входного файла: ")
    key_input = input("Введите ключ: ")
    data = input_file(input_f)
    output_f = input("Введите имя результирующего файла: ")
    mode = input("Введите режим работы\nДля кодирования нажмите 1\nДля декодирования нажмите 2\n")
    output_s = simple_permutation(data, key_input) if mode == '1' else decoding(data, key_input)
    output_file(output_f, output_s)
