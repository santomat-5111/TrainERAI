from flask import render_template
from app import gen
from camera import Shoulder
@app.route("/")
def push():
    to_send=gen(Shoulder)
    return render_template("push.html", to_send=to_send)