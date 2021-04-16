import requests
from bs4 import BeautifulSoup


#####################################################################
# Приложение создано для того что бы быть в курсе последних событий.#
#####################################################################


def get_html(url):
    useragent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.89 Safari/537.36 '}

    r = requests.get(url, headers=useragent, timeout=5)
    return r.text


def get_mk():
    print()
    print('____________________________________________.')
    print('По сообщению сайта: https://www.mk.ru/news/ |')
    print('____________________________________________|')
    print()
    url = 'https://www.mk.ru/news/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    all_item = soup.find('ul', class_='news-listing__day-list')
    for i in all_item:
        try:
            time = i.find('span', class_='news-listing__item-time').text
            print('({}) '.format(time), end='')
        except Exception:
            pass
        try:
            title = i.find('h3', class_='news-listing__item-title').text
            print(title)
        except Exception:
            pass
        try:
            link = i.find('a').get('href')
            print(link + '\n')
        except Exception:
            pass
    print()
    print()
    print()


def get_security():
    print()
    print('___________________________________________________.')
    print('По сообщению сайта: https://www.securitylab.ru/news/')
    print('___________________________________________________|')

    url = 'https://www.securitylab.ru/news/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    all_item = soup.find_all('a', class_='article-card inline-card')
    for i in all_item:
        try:
            time = i.find('time').text
            print('({}) '.format(time), end='')
        except Exception:
            pass
        try:
            title = i.find('h2', class_="article-card-title").text
            print(title)
        except Exception:
            pass

        try:
            link = i.get('href')
            print('https://www.securitylab.ru' + str(link) + '\n')
        except Exception as e:
            print(e)


def get_finance():
    print()
    print('_________________________________________.')
    print('По сообщению сайта: https://www.google.ru|')
    print('_________________________________________|')

    url = ['https://www.google.ru/search?q=%D1%86%D0%B5%D0%BD%D0%B0+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9+%D1%82%D0%B0%D1%82'
           '%D0%BD%D0%B5%D1%84%D1%82%D1%8C&newwindow=1&gbv=1&sei=NyzzX4SpDIidrgTLx52QAg ',
           'https://www.google.ru/search?newwindow=1&gbv=1&q=%D1%86%D0%B5%D0%BD%D0%B0+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9'
           '+%D1%81%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA&oq=&aqs=']
    j = 0
    for i in url:
        html = get_html(i)
        soup = BeautifulSoup(html, 'lxml')

        all_item = soup.find('div', class_="BNeawe iBp4i AP7Wnd").text
        if j == 0:
            print('Татнефть акции: ', all_item)
        else:
            print('Сбербанк акции: ', all_item)
        j += 1


def get_index():
    url = 'https://ru.investing.com/indices/major-indices'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    all_item = soup.find('table', class_='genTbl closedTbl elpTbl elp20 crossRatesTbl').text
    mos_index = all_item[54:180].split('\n')
    rts_index = all_item[120:180].split('\n')
    print(' | '.join(mos_index[1:8]) + '\n' + '\t' + '\t' + '\t' + ' | '.join(rts_index[3:10]))


def get_cybersec():
    print()
    print('______________________________________________________.')
    print('По сообщению сайта: https://iz.ru/tag/kiberbezopasnost|')
    print('______________________________________________________|')

    url = 'https://iz.ru/tag/kiberbezopasnost'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    all_item = soup.find('div', class_='views-infinite-scroll-content-wrapper clearfix')

    for i in all_item:
        try:
            time = i.find('h3').text
            print(time)
        except Exception:
            pass
        try:
            title = i.find('div', class_='lenta_news__day__list__item__title').text
            print(title.strip())
        except Exception:
            pass
        try:
            link = i.find('a').get('href')
            print('https://iz.ru' + link + '\n')
        except Exception:
            pass


def get_kolibri():
    print()
    print('______________________________________________________.')
    print('По сообщению сайта: https://kolibri.press             |')
    print('______________________________________________________|')

    url = 'https://kolibri.press/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    all_item = soup.find('div', class_='td-ss-main-content')
    for i in all_item:
        try:
            title = i.find('h3', class_='entry-title td-module-title').text
            print(title)
        except Exception:
            pass

        try:
            link = i.find('a').get('href')
            if link != 'https://kolibri.press/page/2':
                print(link + '\n')
            else:
                pass
        except Exception:
            pass


def get_haker():
    print()
    print('______________________________________________________.')
    print('По сообщению сайта: https://xakep.ru/tag/news/        |')
    print('______________________________________________________|')

    url = 'https://xakep.ru/tag/news/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    all_item = soup.find('div', class_='bdaia-blocks-container')
    for i in all_item:
        try:
            title = i.find('h3', class_='entry-title').text
            print(title)
        except Exception:
            pass
        try:
            link = i.find('a').get('href')
            print(link + '\n')
        except Exception:
            pass


def get_progger():
    print()
    print('______________________________________________________.')
    print('По сообщению сайта: https://tproger.ru/news/          |')
    print('______________________________________________________|')

    url = 'https://tproger.ru/news/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    all_item = soup.find('div', class_='columns masonry main-page')
    for i in all_item:
        try:
            title = i.find('h2', class_='entry-title').text
            print(title)
        except Exception:
            pass
        try:
            link = i.find('a', class_='article-link').get('href')
            print(link + '\n')
        except Exception:
            pass


def main():
    get_finance()
    get_index()
    get_mk()
    get_security()
    get_cybersec()
    get_kolibri()
    get_haker()
    get_progger()

    # TODO:https://habr.com/ru/news/


if __name__ == '__main__':
    main()
