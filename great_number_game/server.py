from flask import Flask, session, render_template, request
from random import randrange
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "GET":
        num = randrange(0,100)
        session['num'] = num
        print num
        return render_template("index.html")
    else:
        guess = int(request.form['guess'])
        compare = ""
        if guess > session['num']:
            compare = ">"
        elif guess < session['num']:
            compare = "<"
        else:
            compare = "="
        return render_template("index.html",compare=compare)

app.run(debug=True)
