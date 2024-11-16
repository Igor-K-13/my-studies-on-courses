# новый тестовый файл

def word_breakdown(text):
    for elem in text.split():
        key = len(elem.strip('''!'?,".'''))
        encrypt(elem, key)