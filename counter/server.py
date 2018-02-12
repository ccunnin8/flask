from flask import Flask, session, render_template
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    print(session['count'])
    return render_template('index.html')


app.run(debug=True)
