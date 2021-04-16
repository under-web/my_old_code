import shutil, os

# программа для копирования проектов на флешку
# вариант для улучшения скрипта http://plutonit.ru/view_post.php?id=596

fla = os.path.exists('/run/media/twp2/493E090C0AD7EC96')  # указываем путь и узнаем существует ли он?
if fla == True:
    print('Смонтировано!')  # если да
else:
    print('Не вижу том!')  # если нет

name_dir = input('Введите имя каталога для копирования: ')  # вводим имя новой папки куда будем копировать
dir_in = '/run/media/twp2/493E090C0AD7EC96/' + name_dir  # прибавляем к нашеу пути флешки имя папки
dir_out = '/home/twp2/PycharmProjects'  # указываем откуда будем копировать
try: # пробуем копировать
    shutil.copytree(dir_out, dir_in)  # делаем копию папки со всем содержимым
except FileExistsError:
    print('Скорее всего папка уже существует, переименуйте!')  # если исключение

