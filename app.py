from flask import Flask, render_template, Response, redirect, url_for, send_from_directory
import cv2
import numpy as np
import time

try:
    import queue as queue
except ImportError:
    import Queue as queue

from camera2 import VideoCamera

app = Flask(__name__)
value = "nothing"

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home():
    return render_template("main.html")

@app.route('/blackboard', methods=['GET', 'POST'])
def blackboard():
    return render_template("blackboard.html")

@app.route('/recognition', methods=['GET', 'POST'])
def recognition():
    return render_template("recognition.html")

def gen(camera2):
    while True:
        global person
        person, frame = camera2.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        if person == "liutauras-mazonas" or person == "dragos-costin":
            break
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/person_feed', methods=['GET', 'POST'])
def person_feed():
    if person == "liutauras-mazonas" or person == "dragos-costin":
        return redirect("https://online.manchester.ac.uk/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_92_1", code=302)
    return render_template("blackboard.html", name=person)

@app.route('/video_feed', methods=['GET', 'POST'])
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.config['SERVER_NAME'] = "localhost:5050"  # fine
    app.run("localhost", 5050, debug=True, threaded=True)