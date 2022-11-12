from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello! =)'

@app.route('/play')
def level_one():
    return render_template('play.html')

@app.route('/play/<int:num>')
def level_two(num):
    return render_template('cool.html', num=num)

@app.route('/play/<int:num>/<color>')
def level_three(num, color):
    return render_template('awesome.html', num=num, color=color)



if __name__=="__main__":
    app.run(debug=True)