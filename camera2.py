import numpy as np
import cv2
import os
from PIL import Image
import pickle
import time

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def rescale_frame(self, frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    def make_480p(self):
        self.video.set(3, 640)
        self.video.set(4, 480)

    def make_1080p(self):
        self.video.set(3, 1920)
        self.video.set(4, 1080)
    
    def get_frame(self):
        face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainner.yml")

        self.make_480p()

        labels = {"person_name": 1}
        with open("labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}

        while True:
            ret, img = self.video.read()
            img = self.rescale_frame(img, percent=75)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

                roi_gray = gray[y:y+h, x:x+w]

                id_, conf = recognizer.predict(roi_gray)
                if conf>=55 and conf <= 100:

                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color = (255, 255, 255)
                    stroke = 2
                    confid = " - %.2f" % conf
                    ret, jpeg = cv2.imencode('.jpg', img)
                    return labels[id_], jpeg.tobytes()
                                                                               
            ret, jpeg = cv2.imencode('.jpg', img)
            return "notfound", jpeg.tobytes()

