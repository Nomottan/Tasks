def проверка_почты (recipient, sender):
    for проверка in (recipient, sender):
        if '@' not in проверка:
                return False
        for искомое in (".com", ".ru", ".net"):
            if искомое in проверка:
                return True
    return False
def send_email (message, recipient, sender = "university.help@gmail.com"):
    if recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif not проверка_почты(recipient, sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

