# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_ls_code_words.txt'
# Enter the name of the file to dels_code:
# 'text_ls_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_ls_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from os import path

def f_ls_code(file, file_code):
    if path.exists(file) and path.exists(file_code):
        with open(file, encoding='utf-8') as f, \
                open(file_code, "a", encoding='utf-8') as f_codes:

            ls_cod = symbol = ''            
            ls = f.read()
            count = 1
            for i in ls:
                if i != symbol:
                    if symbol:
                        ls_cod += str(count) + symbol
                    count = 1
                    symbol = i
                else:
                    count += 1
            else:
                ls_cod += str(count) + symbol

            f_codes.write(ls_cod)

            print(f"out file 'text_words.txt' =>\n\n{ls}")
            print(f"out file 'text_ls_code_words.txt'\n\n{ls_cod}")           
    else:
        print("The files do not exist in the system!")


def f_ls_decode(file_code):
    if path.exists(file_code):
        with open(file_code, encoding='utf-8') as f:
            ls_decode = count = ''
            ls = f.read()
            for simbol in ls:
                if simbol.isdigit():
                    count += simbol
                else:
                    ls_decode += simbol * int(count)
                    count = ''
        print(ls_decode)        
    else:
        print("The files do not exist in the system!")


msg_1 = 'Enter the name of the file with the text: '
msg_2 = 'Enter the file name to record: '
msg_3 = 'Enter the name of the file to dels_code: '
f_ls_code(input(msg_1), input(msg_2))
f_ls_decode(input(msg_3))

