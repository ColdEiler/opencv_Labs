import cv2
import numpy as np
import datetime

def show_img():
    img = cv2.imread(r'C:/Users/Владислав/OneDrive - FGBOU VO Kubanskiy Gosudarstvennyi Universitet/Рабочий стол/Ацтом/homer.jpg')

    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    cv2.imshow('Display window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_video(video_path, delay):
    video = cv2.VideoCapture(video_path, cv2.CAP_ANY)
    window_name = 'Video Window'

    is_frame_read, frame = video.read()

    while is_frame_read:
        cv2.imshow(window_name, frame)
        cv2.waitKey(delay)

        is_frame_read, frame = video.read()

        key = cv2.waitKey(20)

        # клавиша - escape
        if key == 27:
            cv2.destroyAllWindows()
            break

    video.release()

read_video('C:/Users/Владислав/OneDrive - FGBOU VO Kubanskiy Gosudarstvennyi Universitet/Рабочий стол/Ацтом/video.mp4',5)