import numpy as np
import cv2
import os
from PIL import Image
import pickle

# face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def make_360(self):
    self.video.set(3, 480)
    self.video.set(4, 360)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

cap = cv2.VideoCapture(0)

labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

make_480p()

while True:
    ret, img = cap.read()
    img = rescale_frame(img, percent=75)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf>=65 and conf <= 100:

            print(conf)
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            confid = " - %.2f" % conf
            cv2.putText(img, name + str(confid), (x, y), font, 1, color, stroke, cv2.LINE_AA)

    cv2.imshow('img',img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break