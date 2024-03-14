def encrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i]))
    return encrypted_text


choice = input("Для зашифрования введите 1, для расшифрования введите 2. \nВаш выбор - ")
if choice == '1':
    text = input('Введите текст для шифрования -  ')
    flag = True
    key = ''
    while flag:
        key = input('Введите ключ (той же длины, что и текст) - ')
        if len(key) != len(text):
            print(f'Длина ключа не совпадает с длинной текста. Введите подходящий ключ. '
                  f'Ваш ключ длинной - {len(key)}, длина текста - {len(text)}')
        else:
            flag = False

    text = encrypt(text, key)
    print(f"Зашифрованный текст: {text}")
    with open("encrypt.txt", "w") as file:
        file.write(text)

elif choice == '2':
    flag = True
    while flag:
        text = input('Введите файл из которого считать текст -  ')
        try:
            with open(text, "r") as file:
                text = file.read()
            flag = False
        except:
            continue
    flag = True
    key = ''
    while flag:
        key = input('Введите ключ (той же длины, что и текст) - ')
        if len(key) != len(text):
            print('Длина ключа не совпадает с длинной текста. Введите подходящий ключ'
                  f'Ваш ключ длинной - {len(key)}, длина текста - {len(text)}')
        else:
            flag = False

    text = encrypt(text, key)
    print(f"Расшифрованный текст: {text}")
    with open("decrypt.txt", "w") as file:
        file.write(text)
else:
    print('Вы ввели неверное значение. Повторите ввод')
