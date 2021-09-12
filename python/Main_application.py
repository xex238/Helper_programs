import cv2 # Подключение opencv
import os # Множество функций для работы с ОС
import glob # Позволяет работать с масками файлов или шаблонами

file = open('results.txt', 'w')

path_1 = "C:/Users/dima0/OneDrive/Рабочий стол/Учебники/6 семестр/Практика/trainset"
path_2 = "C:/Users/dima0/OneDrive/Рабочий стол/Учебники/6 семестр/Практика/validationset"
fileList_1 = glob.glob(os.path.join(path_1, "*.avi"))
fileList_2 = glob.glob(os.path.join(path_2, "*.avi"))
# Вывод всех путей до видео на экран
#for filename_1 in fileList_1:
#  print(filename_1)
#for filename_2 in fileList_2:
#  print(filename_2)
    
# Попытка открыть одно видео
#one_video = fileList_1[0] # Берём путь к первому видео из списка
#print(one_video) # Выводим путь на экран

#cap = cv2.VideoCapture(one_video) # Создаём экземпляр класса "видео"
#frame_list = [] # Создаём список с кадрами
#while (cap.isOpened()):
#    ret, frame = cap.read()
#    #print (ret)
#    if (cv2.waitKey(1) & 0xFF == ord('q') or ret == False):
#        break
#    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Чёрно-белый кадр
#    #color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Цветной кадр (перестановка цветов в кадре)
#    color_frame = frame
#    frame_list.append(color_frame) # Запись кадра в массив
#    #cv2.imshow('frame', color_frame) # Воспроизвести кадр

#print(len(frame_list)) # Вывод длины списка кадров

# Вырезание каждого шестого кадра из списка
#new_frame_list = frame_list[0::6]

#print("Количество кадров до обработки - ", len(frame_list))
#print("Количество кадров после обработки - ", len(new_frame_list)) # Вывод в консоль длины нового списка кадров

#first_frame = new_frame_list[40] # Берём определённый кадр из видео
#first_frame = cv2.resize(first_frame, (700, 350))
#cv2.imshow('First frame', first_frame)

# Ожидание нажатия клавиши "q" перед закрытием всех окон
#while(1):
#    if (cv2.waitKey(1) == ord("q")):
#        break

# Поиск переключения светофора
# "Начало" кадра в левом верхнем углу
# Днём красный (днём и ночью примерно одинаковое количество контуров)
#min_red_day = (0, 100, 160)
#max_red_day = (20, 255, 255)
min_red_day_1 = (0, 85, 110)
max_red_day_1 = (20, 255, 255)
min_red_day_2 = (165, 85, 110)
max_red_day_2 = (180, 255, 255)
min_red_day_3 = (255, 255, 255)
max_red_day_3 = (0, 0, 0)

# Днём зелёный (ночью много контуров)
#min_green_day = (50, 150, 0)
#max_green_day = (100, 255, 255)
min_green_day = (40, 85, 110) # С сайта
max_green_day = (91, 255, 255) # С сайта

# Ночью красный (днём много контуров)
min_red_night = (0, 0, 200)
max_red_night = (100, 60, 255)
min_red_night_1 = (255, 255, 255)
max_red_night_1 = (0, 0, 5)
min_red_night_2 = (255, 255, 255)
max_red_night_2 = (0, 0, 5)
min_red_night_3 = (0, 0, 5)
max_red_night_3 = (255, 30, 255)

# Ночью зелёный (днём много контуров)
#min_green_night = (30, 5, 125)
#max_green_night = (115, 255, 255)
min_green_night = (60, 5, 160) # Уточнённые данные (60, 5, 160) (30, 5, 145) - старые
max_green_night = (105, 255, 255)
#min_green_night = (40, 85, 110) # С сайта (одинаково ночью и днём)
#max_green_night = (91, 255, 255) # С сайта (одинаково ночью и днём)

# Обработка всех видео
for filename_1 in fileList_1:
    file.write(os.path.basename(filename_1))
    file.write(' ')
    print(filename_1)
    cap = cv2.VideoCapture(filename_1) # Создаём экземпляр класса "видео"
    frame_list = [] # Создаём список с кадрами
    while (cap.isOpened()):
        ret, frame = cap.read()
        #print (ret)
        if (cv2.waitKey(1) & 0xFF == ord('q') or ret == False):
            break
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Чёрно-белый кадр
        #color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Цветной кадр (перестановка цветов в кадре)
        color_frame = frame
        frame_list.append(color_frame) # Запись кадра в массив
        #cv2.imshow('frame', color_frame) # Воспроизвести кадр

    # Вырезание каждого шестого кадра из списка
    new_frame_list = frame_list[0::6]

    #print("Количество кадров до обработки - ", len(frame_list))
    #print("Количество кадров после обработки - ", len(new_frame_list)) # Вывод в консоль длины нового списка кадров

    first_frame = new_frame_list[0] # Берём определённый кадр из видео
    first_frame = cv2.resize(first_frame, (700, 350))

    first_frame_hsv = cv2.cvtColor(first_frame, cv2.COLOR_BGR2HSV)
    first_frame_hsv = cv2.resize(first_frame_hsv, (700, 350))

    # Попытка определить яркость первого кадра
    light = [0, 0, 0]
    max_light = [0, 0, 0]
    point_x = 250
    point_y = 0
    #cv2.rectangle(first_frame, (point_x, point_y), (point_x + 200, point_y + 100), (0, 255, 0), 2)
    #cv2.imshow('First frame', first_frame)

    while(point_x < 450):
        while(point_y < 100):
            if ((first_frame[point_y, point_x][0] > max_light[0]) and (first_frame[point_y, point_x][1] > max_light[1]) and (first_frame[point_y, point_x][2] > max_light[2])):
                max_light = first_frame[point_y, point_x]
            light = light + first_frame[point_y, point_x]
            point_y = point_y + 1
        point_y = 0
        point_x = point_x + 1
    light = light / 20000
    #print("light = ", light)
    #print("max_light = ", max_light)

    min_red_1 = (0, 0, 0)
    min_red_2 = (0, 0, 0)
    min_red_3 = (0, 0, 0)
    max_red_1 = (0, 0, 0)
    max_red_2 = (0, 0, 0)
    max_red_3 = (0, 0, 0)
    min_green = (0, 0, 0)
    max_green = (0, 0, 0)
    if (light[1] > 100):
        #print("Дневная маска")
        min_red_1 = min_red_day_1
        min_red_2 = min_red_day_2
        min_red_3 = min_red_day_3
        max_red_1 = max_red_day_1
        max_red_2 = max_red_day_2
        max_red_3 = max_red_day_3
        min_green = min_green_day
        max_green = max_green_day
    else:
        #print("Ночная маска")
        min_red_1 = min_red_night_1
        min_red_2 = min_red_night_2
        min_red_3 = min_red_night_3
        max_red_1 = max_red_night_1
        max_red_2 = max_red_night_2
        max_red_3 = max_red_night_3
        min_green = min_green_night
        max_green = max_green_night

    count = 0
    first_switching = -1
    i = 0
    for frame_green in new_frame_list:

        frame_green = cv2.resize(frame_green, (700, 350))
        hsv_green = cv2.cvtColor(frame_green, cv2.COLOR_BGR2HSV)

        mask_green = cv2.inRange(hsv_green, min_green, max_green)

        mask_Er_green = cv2.erode(mask_green, None, iterations = 2)
        mask_Di_green = cv2.dilate(mask_Er_green, None, iterations = 3)
        mask_Di_green = cv2.resize(mask_Di_green, (700, 350))

        # Ищем контуры и складируем их в переменную contours (без исключений)
        contours_green, hierarchy_green = cv2.findContours(mask_Di_green.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if ((len(contours_green) > 0) and (i > 0)):
            frame_red = new_frame_list[i - 1]
            frame_red = cv2.resize(frame_red, (700, 350))
        
            hsv_red = cv2.cvtColor(frame_red, cv2.COLOR_BGR2HSV)

            mask_red_1 = cv2.inRange(hsv_red, min_red_1, max_red_1)
            mask_red_2 = cv2.inRange(hsv_red, min_red_2, max_red_2)
            mask_red_3 = cv2.inRange(hsv_red, min_red_3, max_red_3)
            mask_red = mask_red_1 + mask_red_2 + mask_red_3

            mask_Er_red = cv2.erode(mask_red, None, iterations = 2)
            mask_Di_red = cv2.dilate(mask_Er_red, None, iterations = 3)
            mask_Di_red = cv2.resize(mask_Di_red, (700, 350))

            contours_red, hierarchy_red = cv2.findContours(mask_Di_red.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if (len(contours_red) > 0):

                for contours in contours_green:
                    # Рисуем прямоугольник с искомым объектом на исходном изображении
                    (x, y, w, h) = cv2.boundingRect(contours)
                    #print("Ордината (х) зелёного контура равна ", x)
                    #print("Абсцисса (у) зелёного контура равна ", y)
                    #print("Ширина зелёного контура равна ", w)
                    #print("Высота зелёного контура равна ", h)
                    #cv2.rectangle(frame_green, (x, y), (x + w, y + h), (0, 0, 255), 2)

                for contours in contours_red:
                    (x, y, w, h) = cv2.boundingRect(contours)
                    #print("Ордината (х) красного контура равна ", x)
                    #print("Абсцисса (у) красного контура равна ", y)
                    #print("Ширина красного контура равна ", w)
                    #print("Высота красного контура равна ", h)
                    #cv2.rectangle(frame_red, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    #cv2.imshow("Frame_red", frame_red)
                    #cv2.imshow("Mask_Di_red", mask_Di_red)
                    #print("Количество красных контуров равно ", len(contours_red))

                for contours_g in contours_green:
                    (x_g, y_g, w_g, h_g) = cv2.boundingRect(contours_g)
                    # Сдвиг красного сигнала вниз (при вертикальном расположении светофора)
                    new_x_g_vert = x_g
                    new_y_g_vert = y_g - 2 * h_g
                    # Сдвиг красного сигнала влево (при горизонтальном расположении светофора)
                    #new_x_g_gor = x_g + 2 * w_g
                    #new_y_g_gor = y_g
                    for contours_r in contours_red:
                        (x_r, y_r, w_r, h_r) = cv2.boundingRect(contours_r)
                        #print("Новая ордината (х) красного контура равна ", new_x_g_vert)
                        #print("Новая абсцисса (у) красного контура равна ", new_y_g_vert)
                        if ((new_x_g_vert > 0) and (new_y_g_vert > 0) and (new_x_g_vert + w_g < 700) and (new_y_g_vert + h_g < 350)):
                            if ((x_r + w_r < new_x_g_vert) or (new_x_g_vert + w_g < x_r) or (y_r + h_r < new_y_g_vert) or (new_y_g_vert + h_g < y_r)):
                                # Пересечений нет
                                pass
                            else:
                                #print("Ура, зафиксировано переключение сигнала светофора!")
                                if (count == 0):
                                    first_switching = i*6
                                count = count + 1
                                #print("Кадр, на котором произошло переключение равен: ", i * 6)

        #cv2.imshow("Frame_green", frame_green)
        #cv2.imshow("Mask_Di_green", mask_Di_green)
        #print("Количество зелёных контуров равно ", len(contours_green))
        i = i + 1

        # Ожидание нажатия клавиши "q"
        #while(1):
        #    if (cv2.waitKey(1) == ord("q")):
        #        break
    print("Количество зафиксированных переключений равно ", count)
    print("Кадр, на котором произошло переключение равен ", first_switching)
    file.write(first_switching)
    file.write('\n')
file.close()
