#!/usr/bin/python
def parsing_data():
    result = []
    with open('out_wifi.txt') as file:
        for i in file.readlines():
            i = i[8:64]
            result.append(i)
            itog = set(result)
        for el in itog:
            print(el)

def main():
    parsing_data()

if __name__ == '__main__':
    main()