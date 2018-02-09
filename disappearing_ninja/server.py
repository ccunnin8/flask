from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/<color>')
def ninja(color):
    turtle = "notapril"
    if color == "blue":
        turtle = "leonardo"
    elif color == "orange":
        turtle = "michelangelo"
    elif color == "red":
        turtle = "raphael"
    elif color == "purple":
        turtle = "donatello"
    return render_template('ninja.html',turtle=turtle)


app.run(debug=True)
