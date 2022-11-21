from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'pquNb586Y42NWOi9Hai0P'

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(2, 99)
    print(session)
    return render_template('index.html' , num=session['num'], guess=int(session['guess']))

@app.route('/guess_number', methods=['POST'])
def gess_number():
    if 'guess' not in session:
        session['guess'] = request.form['guess']
    else:
        session.pop('guess')
        session['guess'] = request.form['guess']
    # print(session)
    return redirect('/')

'''
/reset deletes session, and redirects to /guess_number but there is no guess availiable so 
we get a key error, we havent guessed so theres no value
'''
@app.route('/reset')
def reset():
    session.pop('num')
    return redirect('/')
    # return redirect('/guess_number')

if __name__ == '__main__':
    app.run(debug=True)