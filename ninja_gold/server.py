from flask import Flask, render_template, session, redirect, request, Markup
from random import randrange
import time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['status'] = []
    return render_template('index.html')

@app.route('/process_money',methods=["POST"])
def process_money():
    if request.form['loc'] == 'farm':
        earned = randrange(10,21)
        session['gold'] += earned
    elif request.form['loc'] == 'cave':
        earned = randrange(5,11)
        session['gold'] += earned
    elif request.form['loc'] == 'house':
        earned = randrange(2,6)
        session['gold'] += earned
    elif request.form['loc'] == 'casino':
        earned = randrange(-50,51)
        session['gold'] += earned
    else:
        earned = 0
        print "error occurred"
        return redirect('/')
    ts = time.time()
    now = datetime.fromtimestamp(ts).strftime("%Y/%m/%d %I:%M %p")
    if earned > 0:
        output = Markup("<p class='pos'>Earned " + str(earned) + " golds from the " + request.form['loc'] +"! (" + now + ")</p>")
    else:
        output = Markup("<p class='neg'>Entered a casino and lost {x} golds... Ouch. ({y})".format(x=earned,y=now))
    session['status'].append(output)
    return redirect('/')


app.run(debug=True)
