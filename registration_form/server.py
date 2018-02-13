from flask import Flask, render_template, flash, redirect, request
import re

app = Flask(__name__)
app.secret_key = "QuieroSerProgramador"

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        name = request.form['first_name']
        last_name = request.form['apellido']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not valid_email(email):
            flash('The email you entered was not valid','email')
        elif len(name) <= 0:
            flash("You must enter a first name!",'name')
        elif len(last_name) <= 0:
            flash("You must enter a last name!",'name')
        elif len(password) <= 0:
            flash("Password required!",'password')
        elif (password != confirm_password):
            flash("Passwords do not match",'password')
        elif not valid_password(password):
            flash("Passwords must be greater than 8 chars and contain 1 sym and 1 num",'password')
        else:
            flash("Thank you for entering valid info!")
        return redirect('/')

def valid_email(email):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(email) < 0:
        return False
    return EMAIL_REGEX.match(email)

def valid_password(password):
    if len(password) <= 8:
        return False
    has_symbol = False
    has_num = False
    for symbol in "!@#$%^&*()":
         if symbol in password:
             has_symbol = True
             break
    for num in "0123456789":
        if num in password:
            has_num = True
            break
    return has_symbol and has_num



app.run(debug=True)
