from flask import Flask, render_template, redirect,request, flash
app = Flask(__name__)
app.secret_key = "Flambozle"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=["POST"])
def result():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    # print(name,location,language,comment)
    # return redirect('/result')
    if len(name) <= 0:
        flash("You must enter a name")
        return redirect('/')
    if len(comment) < 120:
        flash("You must enter a comment of 120 characters or greater")
        return redirect('/')
    return render_template('result.html',name=name,location=location,language=language,comment=comment)

app.run(debug=True)
