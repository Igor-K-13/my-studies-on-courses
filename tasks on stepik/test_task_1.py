alfabet_e = 'abcdefghijklmnopqrstuvwxyz'
###############
#####


def request_data():
    message = input('Введите ваше сообщение:_')
    word_breakdown(message)


def word_breakdown(text):
    for elem in text.split():
        key = len(elem.strip('''!'?,".'''))
        encrypt(elem, key)


def encrypt(text, key):
    encrypted_text = ''
    for c in text:
        if c.isalpha() and c == c.lower():
            encrypted_text += alfabet_e[(alfabet_e.index(c) + key) % len(alfabet_e)]
        elif c.isalpha() and c == c.upper():
            encrypted_text += alfabet_e[(alfabet_e.index(c.lower()) + key) % len(alfabet_e)].upper()
        else:
            encrypted_text += c

    print(encrypted_text, end=' ')

# test commiklkll
# test commiklkll
# test-222
# uuuuu
# удалось навести порядок с ветками


request_data()