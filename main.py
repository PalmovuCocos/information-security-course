from math import ceil


def input_file(f_input):
    try:
        with open(f_input, encoding="utf-8") as file:
            s = file.readline()
            return s
    except FileNotFoundError:
        print("Невозможно открыть файл")
    except:
        print("Ошибка при работе с файлом")
    finally:
        print(file.closed)


def output_file(o_input, answer):
    try:
        with open(o_input, "w+", encoding="utf-8") as file:
            file.write(answer)
            print("Расшифрованные данные записаны в файл")
    except FileNotFoundError:
        print("Невозможно открыть файл")
    except:
        print("Ошибка при работе с файлом")
    finally:
        print(file.closed)


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

    return ''.join([t[i] for i in range(len(table[0])) for t in table])


def decoding(s, key):
    pass


if __name__ == '__main__':
    input_f = input("Введите имя входного файла: ")
    s = input_file(input_f)
    output_f = input("Введите имя результирующего файла: ")
    decoding_s = simple_permutation()
    output_file(output_f, decoding_s)



