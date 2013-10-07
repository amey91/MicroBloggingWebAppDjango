from random import choice

fortunes = []

def init_fortunes():
    file = open('fortune/fortunes.txt')
    fortune_list = file.read().split('%\n')
    file.close()
    for f in fortune_list:
        fortunes.append(f.strip())

def get_fortune():
    return choice(fortunes)


init_fortunes()
