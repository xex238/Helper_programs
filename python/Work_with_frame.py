import cv2 # Подключение opencv
import os # Множество функций для работы с ОС
import glob # Позволяет работать с масками файлов или шаблонами

# Код программы для подбора цветогаммы (я не знаю, как это назвать по-другому :D)
def nothing(x):
    pass

#path = "C:/Users/dima0/OneDrive/Рабочий стол/Учебники/6 семестр/Практика\gamma_2.jpg"
path = "Additional_files\colors.png"
#path = "C:/Users/dima0/OneDrive/Рабочий стол/Учебники/6 семестр/Практика"
#path_2 = "C:/Users/dima0/OneDrive/Рабочий стол/Для себя\Happy.jpg"
#fileList_1 = glob.glob(os.path.join(path, "*.jpg"))
#for filename_1 in fileList_1:
#    print(filename_1)
#cap = cv2.imread(fileList_1[0]) # Один первый кадр
cap = cv2.imread(path) # Один первый кадр
print(cap.shape)
cap = cv2.resize(cap, (700, 350))
cv2.imshow('cap', cap)
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

    mask = cv2.inRange(hsv, (min_b, min_g, min_r), (max_b, max_g, max_r))
    cv2.imshow('mask', mask)

    result = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('result', result)

    if (cv2.waitKey(1) == ord("q")):
        break
