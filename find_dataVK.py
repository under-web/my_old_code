import re

'''
Скрипт по поиску почты в большом файле
'''


def get_reader():
    with open('ooo.txt', 'r', encoding='utf-8') as file:
        text = file.read(20000)  # указываем размер считывания из файла
        pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+')  # создали шаблон
        result = pattern.findall(text)  # указываем что ищем и где ищем
        lister = []  # пустой список
        s = 0  # счетчик
        for i in result:
            lister.append(i)
            s += 1

    print("Количество строк = ", s)
    return lister


def get_writer(lister):
    with open('output.txt', 'a') as file:
        for index in lister:
            file.write(index + '\n')


def main():
    get_writer(get_reader())


if __name__ == '__main__':
    main()
