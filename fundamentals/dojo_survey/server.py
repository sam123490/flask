from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'AbaCadABara21345'

@app.route('/')
def index():
    session.clear()
    print(session)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def info():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['organ_donor'] = request.form['organ_donor']
    print(session)
    return redirect('/display')

@app.route('/display')
def display():
    return render_template('display.html', name=session['name'],
                                            location=session['location'],
                                            language=session['language'],
                                            comment=session['comment'],
                                            organ_donor=session['organ_donor'])

if __name__ =="__main__":
    app.run(debug=True)