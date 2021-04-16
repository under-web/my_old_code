import re


class Separator:
    """
    Класс для парсинга личных данных из текстов и файлов
    """
    def get_email_in_file(self, path):
        """
        Возвращает из файла emails
        :param path: путь к файлу в котором искать email
        :return: количество строк
        """
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+')  # создали шаблон
            result = pattern.findall(text)  # указываем что ищем и где ищем
            lister_email = []
            s = 0  # счетчик
            for i in result:
                lister_email.append(i)
                s += 1
        print("Количество строк = ", s)

        with open('output_mail.txt', 'a') as file:
            for index in lister_email:
                file.write(index + '\n')
        return lister_email

    def get_phone_in_file(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            pattern = re.compile(r'\+7|8|7\d{11}]')  # создали шаблон
            result = pattern.findall(text)  # указываем что ищем и где ищем
            lister_phone = []
            s = 0  # счетчик
            for i in result:
                lister_phone.append(i)
                s += 1
        print("Количество строк = ", s)

        with open('output_phone.txt', 'a') as file:
            for index in lister_phone:
                file.write(index + '\n')
        return lister_phone






# Example
var = Separator()

var.get_phone_in_file('ooo.txt')
