#!/usr/bin/python
import smtplib  # Импортируем библиотеку по работе с SMTP
import requests
from bs4 import BeautifulSoup
import time
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML
import mimetypes                                          # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders                                # Импортируем энкодер
from email.mime.base import MIMEBase                      # Общий тип
from email.mime.text import MIMEText                      # Текст/HTML
from email.mime.image import MIMEImage                    # Изображения
from email.mime.audio import MIMEAudio

def get_html(url):
    try:
        useragent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.89 Safari/537.36 '}

        r = requests.get(url, headers=useragent, timeout=5)
        return r.text
    except Exception as a:
        print("Не могу соединиться", a)




# присмотреть варианты отправки картинок и документов таким же способом

def send_mail(actual_data, file):
    global msg
    addr_from = "python.spammers@gmail.com"  # Адресат
    addr_to = "python.spammers@gmail.com"  # Получатель
    password = "Berserkdao11"  # Пароль

    with open('mails.txt', 'rb') as fp:
        file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
        file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
        fp.close()
        encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
    file.add_header('Content-Disposition', 'attachment', filename=filename)  # Добавляем заголовки
    msg.attach(file)

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from  # Адресат
    msg['To'] = addr_to  # Получатель
    msg['Subject'] = 'Тестовый показ рассылки для Ивана'  # Тема сообщения

    body = actual_data
    msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст
    msg.attach(file)

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)  # Создаем объект SMTP
    server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()  # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)  # Получаем доступ
    server.send_message(msg)  # Отправляем сообщение
    server.quit()

def get_index():
    url = 'https://ru.investing.com/indices/major-indices'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    all_item = soup.find('table', class_='genTbl closedTbl elpTbl elp20 crossRatesTbl').text
    mos_index = all_item[54:180].split('\n')
    rts_index = all_item[120:180].split('\n')
    return ' | '.join(mos_index[1:8]) + '\n' + '\t' + '\t' + '\t' + ' | '.join(rts_index[3:10])

def get_sberbank():
    url = ['https://www.google.ru/search?q=%D1%86%D0%B5%D0%BD%D0%B0+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9+%D1%82%D0%B0%D1%82'
           '%D0%BD%D0%B5%D1%84%D1%82%D1%8C&newwindow=1&gbv=1&sei=NyzzX4SpDIidrgTLx52QAg ',
           'https://www.google.ru/search?newwindow=1&gbv=1&q=%D1%86%D0%B5%D0%BD%D0%B0+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9'
           '+%D1%81%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA&oq=&aqs=',
           'https://www.google.ru/search?newwindow=1&gbv=1&q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%9C%D0%9C%D0%9A&oq=&aqs=',
           'https://www.google.ru/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%82%D0%B5%D1%81%D0%BB%D0%B0&newwindow=1'
           '&gbv=1&sei=zKkjYNesIavprgT2kIhA']
    j = 0
    li = ['Татнефть ', 'Сбербанк ', 'ММК', 'Тесла']
    for i in url:
        html = get_html(i)
        soup = BeautifulSoup(html, 'lxml')

        all_item = soup.find('div', class_="BNeawe iBp4i AP7Wnd").text
        if j == 0:
            li.insert(1, all_item)
        elif j == 1:
            li.insert(3, all_item)
        elif j == 2:
            li.insert(5, all_item)
        else:
            li.insert(7, all_item)
        j += 1
    return '\n'.join(li)

def main():
    while True:
        # data = get_sberbank() + '\n' + get_index()
        data = ("\n"
                "        Мы обращаемся к тому, кто знаком с туристическим бизнесом не понаслышке. Кто давно занимается торговлей сувенирной продукции. Нечем удивить клиента в прикассовой зоне? Продаёте один и тот же ассортимент из года в год? Ваши устаревшие магниты пылятся годами? Вы вынуждены распродавать их за копейки? \n"
                "Выход есть! Мы предлагаем уникальный продукт, аналогов которому в мире нет – ЖИВОЙ МАГНИТ!!! "
                "Повысьте свои продажи. Удивите своих клиентов. Станьте первым и уникальным среди конкурентов!\n")
    with open('mails.txt', 'rb') as fp:
        file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
        file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
        fp.close()
        encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
        file.add_header('Content-Disposition', 'attachment', filename=filename)  # Добавляем заголовки
        msg.attach(file)
    send_mail(data, file)
        time.sleep(7200)


if __name__ == '__main__':
    main()
