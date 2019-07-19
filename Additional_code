# variant 1 (test variant)
path = "C:/Users/dima0/OneDrive/Рабочий стол/Учебники/6 семестр/Практика" # Абсолютный путь к папкам с видео
folders = ["trainset", "validationset"] # Две папки с видео
for i in folders:
  path = os.path.join(path, i)
  os.path.join(path, "*.avi")
  fileList = glob.glob(os.path.join(path, "*.avi"))
#  for filename in fileList:
#    print(filename)


#path_1 = "C:\Users\dima0\OneDrive\Рабочий стол\Учебники\6 семестр\Практика" Нельзя так писать


#print(cv2.__version__) Проверка подключения библиотеки opencv к python


# Плохой способ вывода на экран первой картинки видео
#while (not (0xFF == ord('q'))):
#    cv2.imshow('First frame', new_frame_list[0])


# Плохая попытка воспроизвести видео с помощью списка кадров
#i = 0
#while (cap.isOpened()):
#    cv2.imshow('frame', frame_list[i])
#    i = i + 1


# Тоже плохая попытка воспроизвести видео с помощью списка кадров
#for frames in frame_list:
#    cv2.imshow('frame', frames)


    ## Ищем контуры и складируем их в переменную contours (с исключениями)
    #try:
    #    _, contours, hierarchy = cv2.findContours(mask_Di.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #except Exception:
    #    pass
    #else:    
    #    # Отображаем контуры поверх изображения
    #    cv2.drawContours(frame, contours, -1, (255, 0, 0), 3, cv2.LINE_AA, hierarchy, 1)
    #    cv2.imshow("Contours", frame)


    ## Функция поиска контуров на изображении
    #contours = cv2.findContours(mask_Di, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #contours = contours[1]

    ## Рисуем контур объекта на исходном изображении
    #if contours is (not None):
    #    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    #    cv2.drawContours(frame, contours[0], -1, (255, 0, 255), 3)
    #    cv2.imshow("Contours", frame)

    #    # Рисуем прямоугольник с искомым объектом на исходном изображении
    #    (x, y, w, h) = cv2.boundingRect(contours[0])
    #    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #    cv2.imshow("Rect", frame)


#cap.release() # Освобождение оперативной памяти, занятой переменной "cap"
#cv2.destroyAllWindows() # Закрытие всех открытых окон





# Код программы для подбора цветогаммы (я не знаю, как это назвать по-другому :D)
def nothing(x):
    pass

cap = first_frame # Один первый кадр
cv2.namedWindow('result')

cv2.createTrackbar('min_b', 'result', 0, 255, nothing)
cv2.createTrackbar('min_g', 'result', 0, 255, nothing)
cv2.createTrackbar('min_r', 'result', 0, 255, nothing)

cv2.createTrackbar('max_b', 'result', 0, 255, nothing)
cv2.createTrackbar('max_g', 'result', 0, 255, nothing)
cv2.createTrackbar('max_r', 'result', 0, 255, nothing)

while(True):
    frame = cap
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", hsv)

    min_b = cv2.getTrackbarPos('min_b', 'result')
    min_g = cv2.getTrackbarPos('min_g', 'result')
    min_r = cv2.getTrackbarPos('min_r', 'result')

    max_b = cv2.getTrackbarPos('max_b', 'result')
    max_g = cv2.getTrackbarPos('max_g', 'result')
    max_r = cv2.getTrackbarPos('max_r', 'result')

    # Размытие матрицы hsv
    #hsv = cv2.blur(hsv, (5, 5))
    #cv2.imshow("Blur", hsv)

    mask = cv2.inRange(hsv, (min_b, min_g, min_r), (max_b, max_g, max_r))
    cv2.imshow('mask', mask)

    # Уменьшение ряби (по умолчанию None - это матрица 3х3) (было 2 и 4 итерации соответственно)
    mask_Er = cv2.erode(mask, None, iterations = 2)
    cv2.imshow("Erode", mask_Er)

    mask_Di = cv2.dilate(mask_Er, None, iterations = 3)
    cv2.imshow("Dilate", mask_Di)

    # Ищем контуры и складируем их в переменную contours (без исключений)
    contours, hierarchy = cv2.findContours(mask_Di.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    frame_2 = frame.copy() # Создаём копию исходного кадра
    # Отображаем контуры поверх изображения
    cv2.drawContours(frame_2, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 1)
    cv2.imshow("Contours", frame_2)
    print(len(contours)) # Выводится на экран количество найденных контуров
    # Если количество найденных контуров зелёного цвета равно нулю, то переходим к следующему кадру.
    # В противном случае смотрим на количество контуров красного цвета на предыдущем кадре.
    # Если количество контуров красного цвета равно нулю, то переходим к следующему кадру

    #result = cv2.bitwise_and(frame, frame, mask = mask)
    result = cv2.bitwise_and(frame, frame, mask = mask_Di) # Применяем не исходную маску, а модифицированную
    cv2.imshow('result', result)

    # Если нажата клавиша "q", то останавливаем цикл while
    if (cv2.waitKey(1) == ord("q")):
        break



                        #if (((x_g >= new_x_r_vert) and (x_g <= new_x_r_vert + w_r) and (y_g >= new_y_r_vert) and (y_g <= new_y_r_vert + h_r)) or
                        #((x_g >= new_x_r_vert) and (x_g <= new_x_r_vert + w_r) and (y_g + h_g >= new_y_r_vert) and (y_g + h_g <= new_y_r_vert + h_r)) or
                        #((x_g + w_g >= new_x_r_vert) and (x_g + w_g <= new_x_r_vert + w_r) and (y_g >= new_y_r_vert) and (y_g <= new_y_r_vert + h_r)) or
                        #((x_g + w_g >= new_x_r_vert) and (x_g + w_g <= new_x_r_vert + w_r) and (y_g + h_g >= new_y_r_vert) and (y_g + h_g <= new_y_r_vert + h_r))):










# Код программы для подбора цветогаммы (обновлённый)
def nothing(x):
    pass

cap = first_frame # Один первый кадр
cv2.namedWindow('result')

cv2.createTrackbar('min_b', 'result', 0, 255, nothing)
cv2.createTrackbar('min_g', 'result', 0, 255, nothing)
cv2.createTrackbar('min_r', 'result', 0, 255, nothing)

cv2.createTrackbar('max_b', 'result', 0, 255, nothing)
cv2.createTrackbar('max_g', 'result', 0, 255, nothing)
cv2.createTrackbar('max_r', 'result', 0, 255, nothing)

i = 0
while(True):
    
    frame = new_frame_list[i]
    frame = cv2.resize(frame, (700, 350))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", hsv)

    min_b = cv2.getTrackbarPos('min_b', 'result')
    min_g = cv2.getTrackbarPos('min_g', 'result')
    min_r = cv2.getTrackbarPos('min_r', 'result')

    max_b = cv2.getTrackbarPos('max_b', 'result')
    max_g = cv2.getTrackbarPos('max_g', 'result')
    max_r = cv2.getTrackbarPos('max_r', 'result')

    # Размытие матрицы hsv
    #hsv = cv2.blur(hsv, (5, 5))
    #cv2.imshow("Blur", hsv)

    mask = cv2.inRange(hsv, (min_b, min_g, min_r), (max_b, max_g, max_r))
    cv2.imshow('mask', mask)

    # Уменьшение ряби (по умолчанию None - это матрица 3х3) (было 2 и 4 итерации соответственно)
    mask_Er = cv2.erode(mask, None, iterations = 2)
    cv2.imshow("Erode", mask_Er)

    mask_Di = cv2.dilate(mask_Er, None, iterations = 3)
    cv2.imshow("Dilate", mask_Di)

    # Ищем контуры и складируем их в переменную contours (без исключений)
    contours, hierarchy = cv2.findContours(mask_Di.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    frame_2 = frame.copy() # Создаём копию исходного кадра
    # Отображаем контуры поверх изображения
    cv2.drawContours(frame_2, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 1)
    cv2.imshow("Contours", frame_2)
    print(len(contours)) # Выводится на экран количество найденных контуров
    # Если количество найденных контуров зелёного цвета равно нулю, то переходим к следующему кадру.
    # В противном случае смотрим на количество контуров красного цвета на предыдущем кадре.
    # Если количество контуров красного цвета равно нулю, то переходим к следующему кадру

    #result = cv2.bitwise_and(frame, frame, mask = mask)
    result = cv2.bitwise_and(frame, frame, mask = mask_Di) # Применяем не исходную маску, а модифицированную
    cv2.imshow('result', result)

    # Если нажата клавиша "q", то останавливаем цикл while
    if (cv2.waitKey(1) == ord("q")):
        break
    if ((cv2.waitKey(1) == ord("w")) and (i > 0)):
        i = i - 1
    if ((cv2.waitKey(1) == ord("e")) and (i < len(frame_list) - 1)):
        i = i + 1







# Поиск переключения светофора
# "Начало" кадра в левом верхнем углу
# Днём красный (днём и ночью примерно одинаковое количество контуров)
min_b_red_day = 0
min_g_red_day = 100
min_r_red_day = 160
max_b_red_day = 20
max_g_red_day = 255
max_r_red_day = 255

# Днём зелёный (ночью много контуров)
min_b_green_day = 50
min_g_green_day = 150
min_r_green_day = 0
max_b_green_day = 100
max_g_green_day = 255
max_r_green_day = 255

# Ночью красный (днём много контуров)
min_b_red_night = 0
min_g_red_night = 0
min_r_red_night = 200
max_b_red_night = 100
max_g_red_night = 60
max_r_red_night = 255

# Ночью зелёный (днём много контуров)
min_b_green_night = 30
min_g_green_night = 5
min_r_green_night = 125
max_b_green_night = 115
max_g_green_night = 255
max_r_green_night = 255

first_frame_hsv = cv2.cvtColor(first_frame, cv2.COLOR_BGR2HSV)
first_frame_hsv = cv2.resize(first_frame_hsv, (700, 350))

i = 0
count = 0
for frame_green in new_frame_list:

    frame_green = cv2.resize(frame_green, (700, 350))
    hsv_green = cv2.cvtColor(frame_green, cv2.COLOR_BGR2HSV)

    mask_green = cv2.inRange(hsv_green, (min_b_green_day, min_g_green_day, min_r_green_day), (max_b_green_day, max_g_green_day, max_r_green_day))

    mask_Er_green = cv2.erode(mask_green, None, iterations = 2)
    mask_Di_green = cv2.dilate(mask_Er_green, None, iterations = 3)
    mask_Di_green = cv2.resize(mask_Di_green, (700, 350))

    # Ищем контуры и складируем их в переменную contours (без исключений)
    contours_green, hierarchy_green = cv2.findContours(mask_Di_green.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if ((len(contours_green) > 0) and (i > 0)):
        frame_red = new_frame_list[i - 1]
        frame_red = cv2.resize(frame_red, (700, 350))
        
        hsv_red = cv2.cvtColor(frame_red, cv2.COLOR_BGR2HSV)

        mask_red = cv2.inRange(hsv_red, (min_b_red_day, min_g_red_day, min_r_red_day), (max_b_red_day, max_g_red_day, max_r_red_day))

        mask_Er_red = cv2.erode(mask_red, None, iterations = 2)
        mask_Di_red = cv2.dilate(mask_Er_red, None, iterations = 3)
        mask_Di_red = cv2.resize(mask_Di_red, (700, 350))

        contours_red, hierarchy_red = cv2.findContours(mask_Di_red.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if (len(contours_red) > 0):

            for contours in contours_green:
                # Рисуем прямоугольник с искомым объектом на исходном изображении
                (x, y, w, h) = cv2.boundingRect(contours)
                print("Ордината (х) зелёного контура равна ", x)
                print("Абсцисса (у) зелёного контура равна ", y)
                print("Ширина зелёного контура равна ", w)
                print("Высота зелёного контура равна ", h)
                cv2.rectangle(frame_green, (x, y), (x + w, y + h), (0, 0, 255), 2)

            for contours in contours_red:
                (x, y, w, h) = cv2.boundingRect(contours)
                print("Ордината (х) красного контура равна ", x)
                print("Абсцисса (у) красного контура равна ", y)
                print("Ширина красного контура равна ", w)
                print("Высота красного контура равна ", h)
                cv2.rectangle(frame_red, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.imshow("Frame_red", frame_red)
                cv2.imshow("Mask_Di_red", mask_Di_red)
                print("Количество красных контуров равно ", len(contours_red))

            for contours_r in contours_red:
                (x_r, y_r, w_r, h_r) = cv2.boundingRect(contours_r)
                if ((w_r + 5 > h_r) and (h_r + 5 > w_r)):
                    # Сдвиг красного сигнала вниз (при вертикальном расположении светофора)
                    new_x_r_vert = x_r
                    new_y_r_vert = y_r + 2 * h_r
                    # Сдвиг красного сигнала влево (при горизонтальном расположении светофора)
                    new_x_r_gor = x_r - 2 * w_r
                    new_y_r_gor = y_r
                    for contours_g in contours_green:
                        (x_g, y_g, w_g, h_g) = cv2.boundingRect(contours_g)
                        print("Новая ордината (х) красного контура равна ", new_x_r_vert)
                        print("Новая абсцисса (у) красного контура равна ", new_y_r_vert)
                        # Проверка на пересечение цветов
                        if ((x_g + w_g < new_x_r_vert) or (new_x_r_vert + w_r < x_g) or (y_g + h_g < new_y_r_vert) or (new_y_r_vert + h_r < y_g)):
                            # Пересечений нет
                            pass
                        else:
                            print("Ура, зафиксировано переключение сигнала светофора!")
                            count = count + 1

                            print("Кадр, на котором произошло переключение равен: ", i * 6)
    cv2.imshow("Frame_green", frame_green)
    cv2.imshow("Mask_Di_green", mask_Di_green)
    print("Количество зелёных контуров равно ", len(contours_green))
    i = i + 1

    # Ожидание нажатия клавиши "q"
    while(1):
        if (cv2.waitKey(1) == ord("q")):
            break
print("Количество зафиксированных переключений равно ", count)





# Более точное определение переключения сигнала светофора
for contours_r in contours_red:
    (x_r, y_r, w_r, h_r) = cv2.boundingRect(contours_r)
    if ((w_r + 5 > h_r) and (h_r + 5 > w_r)):
        # Сдвиг красного сигнала вниз (при вертикальном расположении светофора)
        new_x_r_vert = x_r
        new_y_r_vert = y_r + 2 * h_r
        # Сдвиг красного сигнала влево (при горизонтальном расположении светофора)
        new_x_r_gor = x_r - 2 * w_r
        new_y_r_gor = y_r
        for contours_g in contours_green:
            (x_g, y_g, w_g, h_g) = cv2.boundingRect(contours_g)
            # Проверка на пересечение цветов
            if (((x_g >= new_x_r_vert) and (x_g <= new_x_r_vert + w_r) and (y_g >= new_y_r_vert) and (y_g <= new_y_r_vert + h_r)) or
            ((x_g >= new_x_r_vert) and (x_g <= new_x_r_vert + w_r) and (y_g + h_g >= new_y_r_vert) and (y_g + h_g <= new_y_r_vert + h_r)) or
            ((x_g + w_g >= new_x_r_vert) and (x_g + w_g <= new_x_r_vert + w_r) and (y_g >= new_y_r_vert) and (y_g <= new_y_r_vert + h_r)) or
            ((x_g + w_g >= new_x_r_vert) and (x_g + w_g <= new_x_r_vert + w_r) and (y_g + h_g >= new_y_r_vert) and (y_g + h_g <= new_y_r_vert + h_r))):
                print("Ура, зафиксировано переключение сигнала светофора!")
