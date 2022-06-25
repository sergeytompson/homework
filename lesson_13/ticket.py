# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

# TODO по "питонячему" будет _from, а не from_, не ошибка, просто так принято
def make_ticket(fio: str, from_: str, to: str, date: str, save_to: str) -> None:
    img = Image.open('images/ticket_template.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Acherus Feral.ttf', size=15)
    draw.text((45, 130), fio, font=font, anchor='lm', fill='#000000')
    draw.text((45, 200), from_, font=font, anchor='lm', fill='#000000')
    draw.text((45, 265), to, font=font, anchor='lm', fill='#000000')
    draw.text((285, 265), date, font=font, anchor='lm', fill='#000000')
    img.show()
    if save_to:
        save_to += '.png'
        img.save(save_to, "PNG")
    img.close()


if __name__ == '__main__':
    make_ticket(input('Введите ФИО: '),
                input('Введите аэропорт вылета: '),
                input('Введите аэропорт прилета: '),
                input('Введите дату: '),
                input('В какой файл сохранить? (Нажмите ENTER, если сохранять не нужно): ')
                )


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
