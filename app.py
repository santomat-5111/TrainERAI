from flask import Flask, render_template, Response
from camera import Shoulder, Video, Leg, Game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type: image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/shoulder')

def shoulder():
    return Response(gen(Shoulder()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/leg')

def leg():
    return Response(gen(Leg()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/game')

def game():
    return Response(gen(Game()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/pull.html')
def pull():
    return render_template('pull.html') 

@app.route('/push.html')
def push():
    return render_template('push.html') 

@app.route('/legs.html')
def legs():
    return render_template('legs.html') 

@app.route('/boxing.html')
def boxing():
    return render_template('boxing.html') 

@app.route('/login.html')
def login():
    return render_template('login.html') 

app.run(debug=True)