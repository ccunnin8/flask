from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        red = request.form["red"]
        green = request.form["green"]
        blue = request.form["blue"]
        bg = "background-color: rgb(" + red + "," + green + "," + blue + ")"
        return render_template("index.html",bg=bg)

app.run(debug=True)
