from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new',methods=["GET","POST"])
def dojos():
    if request.method == "GET":
        return render_template('dojos.html')
    else:
        return redirect('/')
app.run(debug=True)
