import cv2
import numpy as np
import datetime

def show_img():
    img = cv2.imread(r'homer.jpg')

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
def print_cam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        center = get_color_of_center_pixel(hsv)
        print(center)
        cv2.imshow('gray',gray)
        cv2.imshow('hsv',hsv)
        cv2.imshow('origin',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


def get_color_of_center_pixel(frame):
    height = len(frame)
    center_row = int(height/2)
    width = len(frame[center_row])
    center_column = int(width/2)
    center_pixel = frame[center_row][center_column]
    return tuple(center_pixel)

def save_cam():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while True:
        ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

def filled_plus_on_cam_capture_save():
    a = cv2.VideoCapture(0)
    a.set(3, 640)
    a.set(4, 480)
    ok,img = a.read()
    while ok:
        cv2.imshow('image',img)
        ok,img = a.read()
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        central = [0,0,0]
        central[0],central[1],central[2] = (get_color_of_center_pixel(hsv))
        if central[0] < 30 or central[0]>150:
            color = (0,0,255)
        elif central[0]>=30 or central[0]<90:
            color = (255,0,0)
        else: color = (0,255,0)   

        cv2.rectangle(img, (300,300),(350,150),color,-1)
        
        cv2.rectangle(img, (225,200),(425,250),color,-1)   
        if cv2.waitKey(1) & 0xFF == 27:
            break
     
    cv2.destroyAllWindows()

def video_from_one_file_to_another(input_path,output_path):
    cap  = cv2.VideoCapture(input_path, cv2.CAP_ANY)
    ok,frame = cap.read()
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (w, h))
    while ok:
        out.write(frame)
        ok,frame = cap.read()


def get_hsv(color_code_hsv):
    hue_channel = color_code_hsv[0]
    saturation_channel = color_code_hsv[1]
    #value_channel = color_code_hsv[2]
   
    if (hue_channel > 300 and hue_channel < 360) or (hue_channel>0 and hue_channel<=60):
        return (0,0,255)
    elif (hue_channel >60 and hue_channel<180):
        #return (0,255,0)
        return (255,0,0)
    else:
        return (0,255,0)
        #return (255,0,0)

def phone_connect_video(ip):
    video = cv2.VideoCapture(ip)
    window_name = 'IP Window'

    is_frame_read, frame = video.read()

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("vanya.avi", fourcc, 60, (width, height))

    while is_frame_read:
        cv2.imshow(window_name, frame)
        video_writer.write(frame)
        key = cv2.waitKey(1)

        # клавиша - escape
        if key == 27:
            break

        is_frame_read, frame = video.read()

    video.release()
    cv2.destroyAllWindows()


#show_img()
#read_video('video.mp4',5)
#readIPWriteTOFile()
#print_cam()
save_cam()
#filled_plus_on_cam_capture_save()
#phone_connect_video('https://192.168.81.85:8080/video')