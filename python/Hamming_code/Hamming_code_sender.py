import math
import functions
import socket

# Код для клиента 1

# Часть 1. Считывание текста с файла
path_1 = "Задания.txt" # utf8
path_2 = "План работы.docx" # Неизвестная кодировка

# Определяем кодировку текста в файле
encoding = functions.get_encoding(path_1)
en = encoding['encoding']
print("Кодировка файла - ", en)

# Считываем текст с заданной кодировкой
file_text = functions.read_file(path_1, en) # Исходный файл

print("file =")
print(file_text)
print()

# Часть 2. Переводим текст в список цифр в десятичной СС
file_code = list(file_text.encode(en))

print("file_text = ")
print(file_code)
print()

# Часть 3. Переводим текст из списка цифр в десятичной СС в список цифр в двоичной СС
# Поиск максимального числа
max_length = 0
for i in range(len(file_code)):
    if(file_code[i] > max_length):
        max_length = file_code[i]

print("max_length = ")
print(max_length)
print()

# Поиск длины слова в доичном виде
word_length = math.ceil(math.log(max_length, 2))

print("word_length = ")
print(word_length)
print()

# Преобразование в двоичную СС
bit_mas = functions.get_bit_mas(file_code, word_length)

print("bit_mas = ")
print(bit_mas)
print("len(bit_mas) = ", len(bit_mas))

# Часть 4. Применяем кодировку Хемминга
# Длина слова Хемминга до вставки контрольных битов
length_hamming_word_input = 53
# Длина слова Хемминга после вставки контрольных битов
length_hamming_word_output = length_hamming_word_input + math.floor(math.log(length_hamming_word_input, 2)) + 1

Hamming_mas = functions.Hamming_code(bit_mas, length_hamming_word_input, 2)

print("Hamming_mas = ")
print(Hamming_mas)
print()

print("Длина Hamming_mas = ")
print(len(Hamming_mas))
print()

# Часть 5. Отправляем данные на другой хост в локальной сети

# Отправляем исходный текст
sock_1 = socket.socket()
#sock_1.connect(('192.168.0.102', 9090))
sock_1.connect(('127.0.0.1', 9090))
sock_1.send(bytes(Hamming_mas))
sock_1.close()

# Отправляем значение длины слова для кода Хемминга
sock_2 = socket.socket()
#sock_2.connect(('192.168.0.102', 49100))
sock_2.connect(('127.0.0.1', 49100))
sock_2.send(bytes(functions.dec_bin(length_hamming_word_input)))
sock_2.close()

# Отправляем значение кодировки исходного текста
# Преобразуем данные в необходимый для отправки вид
print("en = ", en)
print("type(en) = ", type(en))
en_code = list(en.encode('utf8'))
print("en_code = ", en_code)
en_bit_mas = functions.get_bit_mas(en_code, 16)
print("en_bit_mas = ", en_bit_mas)

sock_3 = socket.socket()
#sock_3.connect(('192.168.0.102', 49101))
sock_3.connect(('127.0.0.1', 49101))
sock_3.send(bytes(en_bit_mas))
sock_3.close()

# Принимаем значение длины слова для кодировки
sock_4 = socket.socket()
#sock_4.connect(('192.168.0.102', 49102))
sock_4.connect(('127.0.0.1', 49102))
sock_4.send(bytes(functions.dec_bin(word_length)))
sock_4.close()

print("Отправка завершена")

# Часть 6. Приём ответной информации о переданном файле

# Принимаем информацию о количестве правильно принятых слов
sock_1 = socket.socket()
#sock_1.bind(('192.168.0.103', 49110))
sock_1.bind(('127.0.0.1', 49110))
sock_1.listen(1)
conn_1, addr_1 = sock_1.accept()

count_of_true_words = functions.bin_dec(list(conn_1.recv(1024)))

conn_1.close()

# Принимаем информацию о количестве неправильно принятых слов
sock_2 = socket.socket()
#sock_2.bind(('192.168.0.103', 49111))
sock_2.bind(('127.0.0.1', 49111))
sock_2.listen(1)
conn_2, addr_2 = sock_2.accept()

count_of_false_words = functions.bin_dec(list(conn_2.recv(1024)))

conn_2.close()

# Принимаем информацию о количестве исправленных слов
sock_3 = socket.socket()
#sock_3.bind(('192.168.0.103', 49112))
sock_3.bind(('127.0.0.1', 49112))
sock_3.listen(1)
conn_3, addr_3 = sock_3.accept()

count_of_corrected_words = functions.bin_dec(list(conn_3.recv(1024)))

conn_3.close()

# Принимаем информацию о количестве неисправленных слов
sock_4 = socket.socket()
#sock_4.bind(('192.168.0.103', 49113))
sock_4.bind(('127.0.0.1', 49113))
sock_4.listen(1)
conn_4, addr_4 = sock_4.accept()

count_of_uncorrected_words = functions.bin_dec(list(conn_4.recv(1024)))

conn_4.close()

# Вывод на экран полученных данных
print("Количество правильно переданных слов -", count_of_true_words)
print("Количество неправильно переданных слов -", count_of_false_words)
print("Количество исправленных слов -", count_of_corrected_words)
print("Количество неисправленных слов -", count_of_uncorrected_words)
