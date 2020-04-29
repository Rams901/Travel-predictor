import cv2

import numpy as np
import random


import os
import argparse

import datetime




def main(config):
    
    def detect_face(frame, img):
    
        face_img = frame.copy()
        face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2, minNeighbors=5) 
        test = False
        for (x,y,w,h) in face_rects: 

                cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 5)
                y_2, x_1 = y-75, (2*x+w-50)//2
                try:
                    face_img[y_2: img.shape[0]+y_2, x_1: img.shape[1]+x_1, : ] = img
                except:
                    pass
                test = True
        if test == True:
            return face_img, x, y, w, h
        else:
                return face_img
    
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    
    for dir_name, x, y in os.walk("images"):
        labels = y
    labels = ['images/'+i for i in labels]
    labels.pop(labels.index('images/home.png'))
    cap = cv2.VideoCapture(config.ipweb)  
    tic = datetime.datetime.now()
    unlock = False
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #1080
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if (config.enable_record): 
        out = cv2.VideoWriter(config.out_path,cv2.VideoWriter_fourcc(*'DIVX'), 10, (width,height))
    
    while True:
        if not(unlock):
            toc = datetime.datetime.now()
            ret, frame= cap.read()
            index =random.randint(0, len(labels)-1)
            img= cv2.imread(labels[index])
            img = cv2.resize(img, (75, 75))
            try:
                frame, x, y, w, h = detect_face(frame, img)
                cv2.putText(frame,text="Place you'll travel to in",org=(x, y+h+20), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale= 0.8,color=(200,140,0),thickness=2)
                cv2.putText(frame,text="2020",org=(x+35, y+h+80), fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 2,color=(0,30,255),thickness=8)
            except Exception as e:
                frame= detect_face(frame, img)

            cv2.imshow("yo", frame)
            if (toc - tic > datetime.timedelta(seconds = 6)):
                unlock = True
        else:
                ret, frame = cap.read()
                if(config.unlock_home):
                    img = cv2.imread('images/home.png')
                    label = 'images/HOME.png'
                else:
                    img = cv2.imread(labels[index])
                    label = labels[index]
                img = cv2.resize(img, (75, 75))
                    
                try:
                    frame, x, y, w, h = detect_face(frame, img)
                    cv2.putText(frame,text="Congragulations! You're going",org=(x, y+h+20), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale= 0.7,color=(200,140,0),thickness=2)
                    cv2.putText(frame,text=(label.split('/')[1]).split('.')[0],org=(x+35, y+h+80), fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 1.2,color=(0,30,255),thickness=4)
                except Exception as e:
                    frame= detect_face(frame, img)
                cv2.imshow('yo', frame)
        k = cv2.waitKey(2)  & 0xFF
        try:
              out.write(frame)
        except:
              pass
        if k == 27:
            break

    cap.release()
    try:
        out.release()
    except:
        pass
    cv2.destroyAllWindows()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #LINK TO YOUR ANDROID IPWEBCAM SERVER EXAMPE:  http://192.168.135.1:8080/video
    #NO NEED TO TYPE IT IF YOU'RE NOT USING AN EXTERNAL CAMERA
    parser.add_argument('--ipweb', type=str, default=0)
    
    #recording the video:
    parser. add_argument('--enable_record', default=False, action='store_true')
    parser.add_argument('--out_path', type = str, default = 'out.avi')
    
    #ENABLE IF YOU WANT TO ALWAYS GET HOME AS PREDICTION
    parser.add_argument('--unlock_home', default = False, action='store_true')
    config = parser.parse_args()
    main(config)