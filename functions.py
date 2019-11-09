import math
from chardet.universaldetector import UniversalDetector
import copy
import random

# Длина слова в коде Хемминга - 53

# Вспомогательные методы
#ord(символ) - символ в его код в ascii
#chr(число) - код ascii в символ
#print(int('1101', base=2)) - перевод из двоичной сс и десятичную

# Считывание текста из файла с заданной кодировкой
def read_file(path, encoding):
    text = ""
    with open(path, "r", encoding = encoding) as f:
        for line in f.readlines():
            text += line
    return text

# Определение кодировки заданного файла
def get_encoding(path):
    detector = UniversalDetector()
    with open(path, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    if (detector.result == None):
        print("Неизвестная кодиковка. Невозможно открыть прочитать текст")
        exit()
    return detector.result

# Кодировка из значения ascii в массив с двоичным кодом
def get_bit_mas(code, word_length):
    bit_mas = []
    for i in range(len(code)):
        s = bin(code[i])
        s = s[2:] # Удаляем первые символы '0b' из двоичной кодировки
        while(len(s) != word_length): # Добавляем 0, если слово короче заданной длины
            #print("Тут проблема")
            s = '0' + s
        for j in range(len(s)):
            bit_mas.append(int(s[j]))
        #print("И тут тоже")
    return bit_mas

# Кодировка из массива с двоичным кодом в значения ascii
def get_ascii_code(bit_mas, word_length):
    code = []
    while(len(bit_mas) != 0):
        value = bit_mas[0:word_length]
        bit_mas = bit_mas[word_length:]
        s = ""
        for i in range(len(value)):
            s = s + str(value[i])
        #print("value = ")
        #print(value)
        code.append(int(s, base = 2))
    return code

# Перевод из значений ascii в текст
def get_text(code, word_length, encoding):
    text = ""
    for i in range(len(code)):
        #print(chr(code[i]))
        text = text + chr(code[i])
    #print(text)

    file_path = "my_file.txt"
    my_file = open(file_path, "w")
    my_file.write(text)
    my_file.close()

    new_encoding = get_encoding(file_path)
    
    print("new_encoding = ")
    print(new_encoding['encoding'])
    print()

    #text = text.decode(encoding['encoding'])
    #text = text.decode(encoding['encoding']) # Ошибка
    return text

# Реализация кода Хемминга
def Hamming_code(bit_mas, length_hamming_word_input, count_of_errors):
    Hamming_mas = [] # Список с готовым кодом

    count_of_iterations = math.ceil(len(bit_mas) / length_hamming_word_input)

    # Считываем одно слово
    for k in range(count_of_iterations):
        #print("k = ", k)
        try:
            value_word = bit_mas[0:length_hamming_word_input]
            bit_mas = bit_mas[length_hamming_word_input:]
        except:
            value_word = bit_mas
            bit_mas = []

        # Вставка контрольных битов (по умолчанию принимают 0)
        counter = 0
        value = 0
        while(value < len(value_word)):
            #print("value = ", value)
            value_word.insert(value, 0)
            counter = counter + 1
            value = (2 ** counter) - 1

        # Установка значений контрольных битов
        counter = 0
        value = 2 ** counter
        while(value - 1 < len(value_word)):
            i = value - 1
            count_of_one = 0
            while(i < len(value_word)):
                for j in range(value):
                    if(value_word[i] == 1):
                        count_of_one = count_of_one + 1
                    i = i + 1
                    if(i >= len(value_word)):
                        break
                i = i + value
            value_word[value - 1] = count_of_one % 2
            counter = counter + 1
            value = 2 ** counter

        ## Генерация и вставка случайного (в заданном диапазоне) количества ошибок
        ##random.seed(1)
        #if(count_of_errors != -1):
        #    probability = count_of_errors * random.random()
        #    #print("Вероятность равна", probability)
        #    value_count_of_errors = round(probability)
        #    print("Количество вставляемых ошибок равно", value_count_of_errors)

        #    for i in range(value_count_of_errors):
        #        number = math.floor(len(value_word) * random.random())
        #        if(value_word[number] == 0):
        #            value_word[number] = 1
        #        elif(value_word[number] == 1):
        #            value_word[number] = 0

        # Генерация и вставка заданного количества ошибок
        if(count_of_errors != -1):
            for i in range(count_of_errors):
                number = math.floor(len(value_word) * random.random())
                if(value_word[number] == 0):
                    value_word[number] = 1
                elif(value_word[number] == 1):
                    value_word[number] = 0

        # Добавление текущего слова в готовый список
        for i in range(len(value_word)):
            Hamming_mas.append(value_word[i])

    return Hamming_mas

# Повторное вычисление кода Хемминга на принимающей стороне
def Repeat_Hamming_code(Hamming_mas, length_hamming_word_input):
    #bit_mas = []
    count_of_true_words = 0
    count_of_false_words = 0
    count_of_corrected_words = 0
    count_of_uncorrected_words = 0

    validation_hamming_mas = []
    Hamming_mas_copy = copy.deepcopy(Hamming_mas)

    length_hamming_word_output = length_hamming_word_input + math.floor(math.log(length_hamming_word_input, 2)) + 1
    
    count_of_iterations = math.ceil(len(Hamming_mas_copy) / length_hamming_word_output)

    for k in range(count_of_iterations):
        try:
            value_word = Hamming_mas_copy[0:length_hamming_word_output]
            Hamming_mas_copy = Hamming_mas_copy[length_hamming_word_output:]
        except:
            value_word = Hamming_mas_copy
            Hamming_mas_copy = []

        # Обнуление контрольных битов
        counter = 0
        value = 0
        while(value < len(value_word)):
            #print("value = ", value)
            value_word[value] = 0
            counter = counter + 1
            value = (2 ** counter) - 1

        # Установка значений контрольных битов
        counter = 0
        value = 2 ** counter
        while(value - 1 < len(value_word)):
            i = value - 1
            count_of_one = 0
            while(i < len(value_word)):
                for j in range(value):
                    if(value_word[i] == 1):
                        count_of_one = count_of_one + 1
                    i = i + 1
                    if(i >= len(value_word)):
                        break
                i = i + value
            value_word[value - 1] = count_of_one % 2
            counter = counter + 1
            value = 2 ** counter

        try:
            first_word = Hamming_mas[k * length_hamming_word_output:(k + 1) * length_hamming_word_output]
        except:
            first_word = Hamming_mas[k * length_hamming_word_output:]

        # Проверяем наличиние ошибок
        if(value_word == first_word):
            count_of_true_words = count_of_true_words + 1
            print("Слово передалось верно")
        else:
            count_of_false_words = count_of_false_words + 1
            print("Слово передалось неверно. Попытка исправить")
            print("count_of_false_words =", count_of_false_words)

            # Находим ошибочный бит
            counter = 0
            value = 0
            number_of_error_bit = 0
            while(value < len(value_word)):
                if(value_word[value] != first_word[value]):
                    number_of_error_bit = number_of_error_bit + (value + 1)
                counter = counter + 1
                value = (2 ** counter) - 1
            number_of_error_bit = number_of_error_bit - 1

            #print("number_of_error_bit = ", number_of_error_bit)

            # Исправляем слово (в текущем и "валидационном" слове)
            if(number_of_error_bit < len(value_word)):
                if(value_word[number_of_error_bit] == 0):
                    first_word[number_of_error_bit] = 1
                    value_word[number_of_error_bit] = 1
                elif(value_word[number_of_error_bit] == 1):
                    first_word[number_of_error_bit] = 0
                    value_word[number_of_error_bit] = 0

            # Пересчитываем контрольные биты
            # Вставка контрольных битов (по умолчанию принимают 0)
            counter = 0
            value = 0
            while(value < len(value_word)):
                #print("value = ", value)
                value_word[value] = 0
                counter = counter + 1
                value = (2 ** counter) - 1

            # Установка значений контрольных битов
            counter = 0
            value = 2 ** counter
            while(value - 1 < len(value_word)):
                i = value - 1
                count_of_one = 0
                while(i < len(value_word)):
                    for j in range(value):
                        if(value_word[i] == 1):
                            count_of_one = count_of_one + 1
                        i = i + 1
                        if(i >= len(value_word)):
                            break
                    i = i + value
                value_word[value - 1] = count_of_one % 2
                counter = counter + 1
                value = 2 ** counter

            if(value_word == first_word):
                count_of_corrected_words = count_of_corrected_words + 1
                print("Слово удалось исправить")
            else:
                count_of_uncorrected_words = count_of_uncorrected_words + 1
                print("Слово не удалось исправить")

        # Убираем контрольные биты
        counter = math.floor(math.log(len(value_word), 2))
        value = (2 ** counter) - 1
        while(counter >= 0):
            value_word.pop(value)
            counter = counter - 1
            value = (2 ** counter) - 1

        for i in range(len(value_word)):
            validation_hamming_mas.append(value_word[i])

    print("validation_hamming_mas = ")
    print(validation_hamming_mas)
    print()

    return validation_hamming_mas, count_of_true_words, count_of_false_words, count_of_corrected_words, count_of_uncorrected_words

# Перевод из десятичной сс в двоичную (число -> список)
def dec_bin(number):
    number_copy = copy.deepcopy(number)
    l = []
    while(number_copy != 0):
        l.append(number_copy % 2)
        number_copy = math.floor(number_copy / 2)
    l.reverse()
    print("Десятичное число:")
    print(l)
    return l

# Перевод из двоичной сс в десятичную (список -> число)
def bin_dec(l):
    l_copy = copy.deepcopy(l)
    number = 0
    for i in range(len(l_copy)):
        number = number + (l_copy[i] * (2 ** (len(l_copy) - i - 1)))
    print("Двоичное число")
    print(number)
    return number