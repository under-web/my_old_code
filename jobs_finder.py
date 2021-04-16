import requests, time
from bs4 import BeautifulSoup
# TODO отладить trud.com
# TODO отладка кода (пробелы, отсутвие ссылок, кривые выдачи, атоопределение количества стриниц)
# TODO   https://python-scripts.com/question/13398 здесь пример отлова ошибок для фунции get_requests
def get_request(gen_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36 '
    }  # поставили поддельный юзер агент
    while True:  # взял в бесконечный цикл чтобы в случае ошибок возвращаться к продолжению работы программы
        try:
            r = requests.get(gen_url, headers=headers, timeout=7)
            if r.status_code == 200:  # проверяем статус подключения
                print("┌( ಠ_ಠ)┘")

            if r.status_code == 404:
                print('Страница не существует!')
            return r.text
        except (
                requests.exceptions.ReadTimeout,
                requests.exceptions.ConnectionError):  # отлавливаем исключения соединения
            print('Read timed out')  # в случае ошибок выводим на экран проблему
            time.sleep(2)


def get_hhru(quest):  #
    print('Данные с сайта hh.ru')

    first_url = 'https://kazan.hh.ru/search/vacancy?L_is_autosearch=false&area=88&clusters=true&enable_snippets=true' \
                '&text= '
    page_url = '&page='
    page_number = 0
    while page_number != 3:  # создали цикл в котором подставляем адреса урл в функцию requests (пока не равно 3)
        gen_url = first_url + quest + page_url + str(page_number)  # собираем полный адрес из нашего запроса и урл
        html = get_request(gen_url)  # передаем в ф-цию реквест наш собранный адрес обозначаем все в пe-ую

        soup = BeautifulSoup(html, 'lxml')  # создаем обьект супа
        data = soup.find('div', class_='vacancy-serp')  # находим общий блок для следующего поиска и перебора

        for i in data:
            try:
                title = i.find('span', class_='g-user-content').text

            except (ValueError, AttributeError, TypeError):  # отлавливаем исключения
                title = ''

            try:
                link = i.find('a').get('href')
            except (ValueError, AttributeError, TypeError):
                link = ''

            try:
                price = i.find('div', class_='vacancy-serp-item__sidebar').text
            except (ValueError, AttributeError, TypeError):
                price = ''
            if title != '':  # проверяем, если в переменной title не пустая строка, то печатаем
                print(title, link, price)
            else:  # если в переменной пустая строка, перейти к следующей итерации
                continue
        page_number += 1


def get_indid(quest):
    print('Данные с сайта ru.indeed.com')

    first_url = 'https://ru.indeed.com/jobs?q='
    last_url = '&l=Казань&start='
    page_number = 0
    while page_number != 2:
        gen_url = first_url + quest + last_url + str(page_number)
        html = get_request(gen_url)

        soup = BeautifulSoup(html, 'lxml')
        data = soup.find_all('td', id='resultsCol')  # общий блок инфы

        for i in data:
            try:
                title = i.find_all('h2', class_='title')  # нашли раздел с интересующей информацией
                for el in title:
                    link = el.find('a').get('href')  # достаем ссылки
                    print(el.text, 'https://ru.indeed.com' + link)  # печать оглавление объявления и ссылки
            except (ValueError, AttributeError):
                title = ''
        page_number += 1


def get_trud(quest):
    print('Данные с сайта trud.com')
    first_url = 'https://www.trud.com/kazan/jobs/page/'
    last_url = '?q='

    page_number = 1
    while page_number != 7:
        gen_url = first_url + str(page_number) + last_url + quest
        html = get_request(gen_url)

        soup = BeautifulSoup(html, 'lxml')
        data = soup.find_all('div', class_='item hover')
        for i in data:
            try:
                title = i.find('a', class_='item-link').text
            except (ValueError, AttributeError):
                title = ''

            try:
                price = i.find('span', class_='link-glyph salary').text
            except (ValueError, AttributeError):
                price = ''
            try:
                link = i.find('a')
            except (ValueError, AttributeError):
                link = ''
            print(link)
        page_number += 1


def get_rabota(quest):
    print('Данные с сайта rabota.ru')

    first_url = 'https://kazan.rabota.ru/vacancy/?query='
    # page_url =
    gen_url = first_url + quest
    html = get_request(gen_url)
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_='infinity-scroll r-serp__infinity-list')
    for i in data:
        try:
            title = i.find('h3').text
        except (ValueError, AttributeError):
            title = ''

        try:
            price = i.find('div', class_='vacancy-preview-card__salary').text
        except (ValueError, AttributeError, TypeError):  # отловил ошибку TypeError
            price = ''
        try:
            link = i.find('a', class_='').get('href')
            link = 'https://kazan.rabota.ru' + link  # решилась проблема с дублированием -'https://kazan.rabota.ru'
        except (ValueError, AttributeError, TypeError):
            link = ''
        print(title.strip(), price.strip(), link)  # использовал метод strip() сразу после .text убрав все пробелы


def get_worki(quest):
    print('Данные с сайта worki.ru')

    first_url = 'https://kazan.worki.ru/?keyWord='
    gen_url = first_url + quest
    html = get_request(gen_url)
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_='JobsFeedPage_feed__2kbg_')
    for i in data:
        try:
            title = i.find('a', class_='jobCard_profession__1OON9').get_text()
        except (ValueError, AttributeError, TypeError):
            title = ''

        try:
            price = i.find('div', class_='salaryText_salary__2O-Nx').text
        except (ValueError, AttributeError, TypeError):
            price = ''

        try:
            link = i.find('a', class_='jobCard_profession__1OON9').get('href')
        except (ValueError, AttributeError, TypeError):
            link = ''
        if title == '':  # избегаем повторения повторения домена в случае исключения
            continue
        else:
            print(title, price, 'https://worki.ru' + link)


def get_jooble(quest):
    print('Данные взяты с сайта ru.jooble.org')

    first_url = 'https://ru.jooble.org/SearchResult?ukw='
    page_url = '&rgns=Казань&p='
    page_number = 1
    while page_number != 10:
        gen_url = first_url + quest + page_url + str(page_number)
        html = get_request(gen_url)
        soup = BeautifulSoup(html, 'lxml')

        data = soup.find_all('div', class_='top-wr')
        for i in data:
            try:
                title = i.find('a', class_='link-position job-marker-js').text
            except (ValueError, AttributeError, TypeError):
                title = ''
            try:
                link = i.find('a', class_='link-position job-marker-js').get('href')
            except (ValueError, AttributeError, TypeError):
                link = ''
            try:
                price = i.find('span', class_='salary').text
            except (ValueError, AttributeError, TypeError):
                price = ''
            print(title.strip(), price.strip(), link)
        page_number += 1


def get_avito(quest):
    print('Данные взяты с сайта avito.ru')

    first_url = 'https://www.avito.ru/kazan/vakansii?q='
    # last_url = '?p='
    page_number = 1

    gen_url = first_url + quest
    html = get_request(gen_url)
    soup = BeautifulSoup(html, 'lxml')
    print(gen_url)
    data = soup.find_all('div', class_='item_table-wrapper')
    for i in data:
        try:
            title = i.find('span', class_='snippet-link-name').text
        except (ValueError, AttributeError, TypeError):
            title = ''
        try:
            link = i.find('a', class_='snippet-link').get('href')
        except (ValueError, AttributeError, TypeError):
            link = ''
        try:
            price = i.find('span', class_='snippet-price').text
        except (ValueError, AttributeError, TypeError):
            price = ''
        print(title.strip(), price.strip(), 'https://www.avito.ru' + link)


def get_gorodr(quest):
    print('Данные взяты с сайта gorodrabot.ru')

    first_url = 'https://kazan.gorodrabot.ru/'
    last_url = '?p='
    page_number = 1

    while page_number != 10:
        gen_url = first_url + quest + last_url + str(page_number)
        html = get_request(gen_url)

        soup = BeautifulSoup(html, 'lxml')
        data = soup.find('div', class_='result-list')

        try:
            title = soup.find_all('a', class_='snippet__title-link link an-vc')
            [print(el.text, el.get('href')) for el in title]  # используем включение списка просим сначала текст(
            # el.text) а потом достаем ссылку
        except (ValueError, AttributeError, TypeError):
            title = ''

        page_number += 1


def get_jobsora(quest):
    print('Данные взяты с сайта ru.jobsora.com')

    first_url = 'https://ru.jobsora.com/работа-'
    last_url = '-казань-республика-татарстан?page='
    page_number = 1
    while page_number != 20:
        gen_url = first_url + quest + last_url + str(page_number)
        html = get_request(gen_url)
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find_all('div', class_='c-result-item c-main-box c-main-box--hovered js-listing-item js-clickable')
        for i in data:
            try:
                title = i.find('a').text
            except (ValueError, AttributeError, TypeError):
                title = ''
            try:
                link = i.find('a').get('href')
            except (ValueError, AttributeError, TypeError):
                link = ''
            try:
                price = i.find('span', class_='c-result-item__marker').text
            except (ValueError, AttributeError, TypeError):
                price = ''
            print(title, price, link)
        page_number += 1


def main():  # функция управления
    quest = input('Введите вакансию для поиска: ')
    get_hhru(quest)
    get_indid(quest)
    get_trud(quest)
    get_rabota(quest)
    get_worki(quest)
    get_jooble(quest)
    get_avito(quest)
    get_gorodr(quest)
    get_jobsora(quest)


if __name__ == '__main__':  # точка входа
    main()