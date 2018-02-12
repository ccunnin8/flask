from flask import Flask, jsonify, render_template
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
    data = {
        "image": "static/Ninjas/" + turtle + ".jpg",
        "name": turtle[0].upper() + turtle[1:]
    }
    json = jsonify(data)
    json.status_code = 200

    return json



app.run(debug=True)
