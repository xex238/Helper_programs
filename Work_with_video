import cv2 # Подключение opencv
import os # Множество функций для работы с ОС
import glob # Позволяет работать с масками файлов или шаблонами

# Код программы для подбора цветогаммы (я не знаю, как это назвать по-другому :D)
def nothing(x):
    pass

cap = cv2.VideoCapture(0) # Поток видео
cv2.namedWindow('result')

cv2.createTrackbar('min_b', 'result', 0, 255, nothing)
cv2.createTrackbar('min_g', 'result', 0, 255, nothing)
cv2.createTrackbar('min_r', 'result', 0, 255, nothing)

cv2.createTrackbar('max_b', 'result', 0, 255, nothing)
cv2.createTrackbar('max_g', 'result', 0, 255, nothing)
cv2.createTrackbar('max_r', 'result', 0, 255, nothing)

while(True):
    ret, frame = cap.read()
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
