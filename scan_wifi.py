#!/usr/bin/python
import subprocess
import time
from pars_wifi import parsing_data

list_wifi = []
while True:
    try:
        info_wifi = subprocess.run(['nmcli', 'dev', 'wifi'], stdout=subprocess.PIPE)
        with open('out_wifi.txt', 'a') as txt_file:
            txt_file.writelines(info_wifi.stdout.decode('utf-8'))
            time.sleep(60)
        #   TODO: сделать выборку нужных данных из строки с помощью регулярных выражений (MAC,BSSID)
        #   TODO: добавить их в список и преобразовать в множество
    except KeyboardInterrupt as e:
        parsing_data()
        print('Вы завершили сканирование.')
        break
