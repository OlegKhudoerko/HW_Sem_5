# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1
# out
# The data is incorrect


# def dd(num: int):
#     if num:
#         return "The data is incorrect"
#
#     return ls
# print(*dd(input()))

import random


def f_rnd(num):
    if not num.isnumeric():
        print("The data is incorrect")
        return ''
        
    ls = ''
    for i in range(int(num)):
        x = 'абв'
        ls += ''.join(random.sample(x, len(x))) + ' '
    return ls

def ls_new(ls):
    return ls.replace('абв ', '')


ls_rnd = f_rnd(input('Number of words: '))
print(ls_rnd)
print(ls_new(ls_rnd))
